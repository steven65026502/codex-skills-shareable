# 可公開分享的 Codex Agent Skills

這是給其他 Windows 使用者使用的去識別化技能包，共有 41 個 Agent Skills。內容不含原使用者的姓名、電腦路徑、帳號、私人倉庫、專案資料、憑證、瀏覽器登入狀態或 Codex 記憶。

本倉庫只同步經過審閱的通用檔案，不會直接複製整個本機 Skills 目錄。後續維護必須遵守 [`.github-maintainer.yml`](.github-maintainer.yml) 的公開版、去識別化與驗證規則。

## VS Code 卡在「開啟檔案／建立專案」時

這是 VS Code 尚未開啟資料夾的正常歡迎畫面，不用建立新檔案或新專案。

1. 按 `Ctrl+Shift+P`。
2. 輸入並選擇 `Git: Clone`（複製 Git 存放庫）。
3. 貼上這個 GitHub 倉庫的網址。
4. 選擇電腦上的存放位置。
5. 下載完成後按 `Open`（開啟）。

也可以在 VS Code 終端機執行：

```powershell
git clone <這個倉庫的網址>
cd codex-skills-shareable
code .
```

## 安裝技能

在倉庫資料夾開啟 PowerShell，先預覽：

```powershell
powershell -ExecutionPolicy Bypass -File ".\installers\install-skills.ps1" -WhatIf
```

確認路徑正確後正式安裝：

```powershell
powershell -ExecutionPolicy Bypass -File ".\installers\install-skills.ps1"
```

預設安裝到 `%USERPROFILE%\.agents\skills`。既有技能不會被覆寫；只有明確加上 `-Force` 才會取代同名資料夾。完成後重新啟動 Codex，再用 `/skills` 檢查。

## 內容

- `skills/`：41 個使用者層級技能。
- `installers/install-skills.ps1`：Windows 安裝腳本。
- `mcp/config.example.toml`：不含憑證的 MCP 範例。
- `inventory/SKILLS.md`：完整技能清單。
- `inventory/VALIDATION.md`：驗證與去識別化結果。
- `RECIPIENT_SETUP_PROMPT.md`：可交給收件者 Codex 的設定提示。
- `THIRD_PARTY_NOTICE.md`：第三方來源與授權提醒。

## MCP 與外掛

不要直接覆蓋既有的 `%USERPROFILE%\.codex\config.toml`。請先備份，再從 `mcp/config.example.toml` 挑選需要的區段合併。

Obsidian API key、base URL、GitHub 帳號與倉庫，以及 Cowart、GitHub、Gmail、Canva 等外掛登入，都必須由使用者在自己的電腦重新設定。此倉庫不提供任何 Token、OAuth、Cookie 或登入狀態，也不重新散布外掛快取。

## 已通用化的自訂技能

- `issue-ledger`：保留證據式問題帳本流程，專案範例已改成通用內容。
- `github-maintainer`：保留一般 GitHub 倉庫維護、安全檢查與交接流程。
- `obsidian-github-backup`：不再預設任何 Vault 路徑或 GitHub 倉庫，使用時必須自行輸入。
- 長流程技能改用精簡入口與按需參考文件；小任務不再被迫執行完整流程。
- 會操作外部服務的技能先檢查工具、登入與權限；缺少前提時明確停止，不模擬成功。

## 安全與相容性

所有 41 個技能均已通過技能格式驗證。公開版另做了個人識別字串與常見密鑰格式掃描；詳情見 `inventory/VALIDATION.md`。

## 第三方授權

這個倉庫不是把所有內容改成同一份授權。各技能原有的 `LICENSE`、`NOTICE` 與 `PROVENANCE` 均予以保留。尤其 `huashu-design` 來自 [`alchaincyf/huashu-design`](https://github.com/alchaincyf/huashu-design)，個人／非商業使用與公司／商業使用的條件不同；請先閱讀其內附授權。完整提醒見 `THIRD_PARTY_NOTICE.md`。
