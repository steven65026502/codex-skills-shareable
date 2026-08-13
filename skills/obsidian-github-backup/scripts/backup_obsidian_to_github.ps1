param(
    [Parameter(Mandatory = $true)]
    [string]$VaultPath,
    [Parameter(Mandatory = $true)]
    [string]$RepositoryFullName,
    [string]$Branch = "main",
    [string]$CommitMessage = ""
)

$ErrorActionPreference = "Stop"

function Invoke-Git {
    $gitArgs = $args
    & git @gitArgs
    if ($LASTEXITCODE -ne 0) {
        throw "git $($gitArgs -join ' ') failed with exit code $LASTEXITCODE"
    }
}

function Get-GitHubToken {
    param([string]$Owner)

    $inputText = @"
protocol=https
host=github.com
username=$Owner

"@
    $credential = $inputText | git credential-manager get
    $map = @{}
    $credential -split "`n" | ForEach-Object {
        if ($_ -match "^(.*?)=(.*)$") {
            $map[$matches[1]] = $matches[2]
        }
    }
    if (-not $map["password"]) {
        throw "GitHub Credential Manager did not return a token. Sign in to GitHub from Git first."
    }
    return $map["password"]
}

function Ensure-PrivateGitHubRepo {
    param([string]$FullName)

    $parts = $FullName.Split("/")
    if ($parts.Count -ne 2) {
        throw "RepositoryFullName must be owner/repo, got: $FullName"
    }
    $owner = $parts[0]
    $repo = $parts[1]
    $token = Get-GitHubToken -Owner $owner
    $headers = @{
        Authorization = "Bearer $token"
        "User-Agent" = "codex-obsidian-backup"
        Accept = "application/vnd.github+json"
    }

    $repoUri = "https://api.github.com/repos/$owner/$repo"
    try {
        $existing = Invoke-RestMethod -Uri $repoUri -Headers $headers -Method Get
        if (-not $existing.private) {
            $body = @{ private = $true } | ConvertTo-Json
            $updated = Invoke-RestMethod -Uri $repoUri -Headers $headers -Method Patch -Body $body -ContentType "application/json"
            return @{ FullName = $updated.full_name; Private = [bool]$updated.private; Action = "made_private" }
        }
        return @{ FullName = $existing.full_name; Private = [bool]$existing.private; Action = "exists" }
    }
    catch {
        $status = $null
        if ($_.Exception.Response) {
            $status = $_.Exception.Response.StatusCode.value__
        }
        if ($status -ne 404) {
            throw
        }
        $body = @{
            name = $repo
            private = $true
            description = "Private backup of an Obsidian vault"
            auto_init = $false
        } | ConvertTo-Json
        $created = Invoke-RestMethod -Uri "https://api.github.com/user/repos" -Headers $headers -Method Post -Body $body -ContentType "application/json"
        return @{ FullName = $created.full_name; Private = [bool]$created.private; Action = "created" }
    }
}

function Ensure-GitIgnoreRule {
    param([string]$VaultRoot)

    $gitignore = Join-Path $VaultRoot ".gitignore"
    $required = @(
        ".git/",
        ".obsidian/plugins/obsidian-local-rest-api/data.json",
        "Thumbs.db",
        "Desktop.ini",
        ".DS_Store",
        ".trash/",
        "*.tmp",
        "*.temp"
    )

    if (Test-Path -LiteralPath $gitignore) {
        $existing = Get-Content -LiteralPath $gitignore -ErrorAction Stop
    }
    else {
        $existing = @()
    }

    $changed = $false
    foreach ($rule in $required) {
        if ($existing -notcontains $rule) {
            $existing += $rule
            $changed = $true
        }
    }

    if ($changed -or -not (Test-Path -LiteralPath $gitignore)) {
        $utf8 = New-Object System.Text.UTF8Encoding($false)
        [System.IO.File]::WriteAllText($gitignore, (($existing | Where-Object { $_ -ne "" }) -join "`n") + "`n", $utf8)
    }
}

$vault = (Resolve-Path -LiteralPath $VaultPath).Path
$repoInfo = Ensure-PrivateGitHubRepo -FullName $RepositoryFullName
if (-not $repoInfo.Private) {
    throw "Repository $RepositoryFullName is not private. Aborting backup."
}

Ensure-GitIgnoreRule -VaultRoot $vault

Push-Location $vault
try {
    if (-not (Test-Path -LiteralPath ".git")) {
        Invoke-Git init -b $Branch
    }

    $remoteUrl = "https://github.com/$RepositoryFullName.git"
    $remoteExists = $false
    & git remote get-url origin *> $null
    if ($LASTEXITCODE -eq 0) {
        $remoteExists = $true
    }
    if ($remoteExists) {
        Invoke-Git remote set-url origin $remoteUrl
    }
    else {
        Invoke-Git remote add origin $remoteUrl
    }

    Invoke-Git add -A

    $trackedSecret = & git ls-files ".obsidian/plugins/obsidian-local-rest-api/data.json"
    if ($trackedSecret) {
        throw "Sensitive Local REST API data file is tracked. Remove it from Git before backup."
    }

    $privateKeyMatches = & git grep --cached -n -I "BEGIN RSA PRIVATE KEY"
    if ($LASTEXITCODE -eq 0 -and $privateKeyMatches) {
        throw "Staged content contains an RSA private key. Aborting backup."
    }

    $githubTokenMatches = & git grep --cached -n -I -E "ghp_|github_pat_"
    if ($LASTEXITCODE -eq 0 -and $githubTokenMatches) {
        throw "Staged content appears to contain a GitHub token. Aborting backup."
    }

    $porcelain = & git status --porcelain
    if (-not $porcelain) {
        Write-Output "No changes to back up."
        Write-Output "Repository: $($repoInfo.FullName)"
        Write-Output "Private: $($repoInfo.Private)"
        exit 0
    }

    if (-not $CommitMessage) {
        $CommitMessage = "Back up Obsidian vault $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
    }
    Invoke-Git commit -m $CommitMessage
    Invoke-Git push -u origin $Branch

    $sha = (& git rev-parse --short HEAD).Trim()
    $count = (& git ls-files | Measure-Object).Count
    Write-Output "Backed up Obsidian vault."
    Write-Output "Repository: $($repoInfo.FullName)"
    Write-Output "Private: $($repoInfo.Private)"
    Write-Output "Commit: $sha"
    Write-Output "Tracked files: $count"
    Write-Output "Excluded: .obsidian/plugins/obsidian-local-rest-api/data.json"
}
finally {
    Pop-Location
}
