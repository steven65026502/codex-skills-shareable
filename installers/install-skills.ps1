[CmdletBinding(SupportsShouldProcess)]
param(
    [string]$SourceRoot,
    [string]$TargetRoot = (Join-Path $env:USERPROFILE '.agents\skills'),
    [switch]$Force
)

if ([string]::IsNullOrWhiteSpace($SourceRoot)) {
    $SourceRoot = Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) '..\skills'
}

$source = [System.IO.Path]::GetFullPath($SourceRoot)
$target = [System.IO.Path]::GetFullPath($TargetRoot)

if (-not (Test-Path -LiteralPath $source -PathType Container)) {
    throw "Skill source folder not found: $source"
}

if (-not (Test-Path -LiteralPath $target)) {
    if ($PSCmdlet.ShouldProcess($target, 'Create skill target directory')) {
        New-Item -ItemType Directory -Path $target -Force | Out-Null
    }
}

$skills = Get-ChildItem -LiteralPath $source -Directory -Force |
    Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') }

foreach ($skill in $skills) {
    $destination = Join-Path $target $skill.Name

    if ((Test-Path -LiteralPath $destination) -and -not $Force) {
        Write-Warning "Skipped existing skill: $destination (use -Force to replace files)"
        continue
    }

    if ($PSCmdlet.ShouldProcess($destination, "Install skill $($skill.Name)")) {
        if (-not (Test-Path -LiteralPath $destination)) {
            New-Item -ItemType Directory -Path $destination -Force | Out-Null
        }
        Copy-Item -Path (Join-Path $skill.FullName '*') -Destination $destination -Recurse -Force
        Write-Host "Installed: $($skill.Name)"
    }
}

Write-Host "Done. Restart Codex, then use /skills to verify."
