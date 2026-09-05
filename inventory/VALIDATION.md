# 公開版驗證紀錄

驗證日期：2026-09-05

## 結果

- 技能目錄：41
- 包含 `SKILL.md`：41
- 技能格式驗證：41/41 通過（UTF-8 模式）
- `agents/openai.yaml`：21 個，結構、短描述與預設提示檢查通過
- Markdown 本地連結：0 個失效
- 腳本靜態解析：
  - Python：77 個，0 個錯誤
  - JavaScript / MJS / CJS：21 個，0 個錯誤
  - PowerShell：10 個，0 個錯誤
  - Shell：8 個，0 個錯誤
- `ui-ux-pro-max`：
  - 搜尋命令可執行
  - 12 個領域資料檔、22 個技術棧資料檔及 `ui-reasoning.csv` 通過資料驗證
  - 可攜式安裝測試：130 tests、7,923 subtests 通過
  - 固定上游版本完整測試：157 tests、7,936 subtests 通過
- `zotero-skills`：42 個核心、模擬整合與安全測試通過；測試未連線或修改真實 Zotero
- 安裝腳本：`-WhatIf` 預覽 41 個技能，沒有建立目標資料夾
- `git diff --check`：通過
- 公開內容掃描：不包含原使用者姓名、使用者名稱、個人絕對路徑、私人倉庫或專案名稱
- 憑證與狀態掃描：不包含 API key、OAuth token、Cookie、`auth.json`、瀏覽器狀態、Codex 記憶或本機備份
- 大型本機環境：不包含外掛快取、`node_modules`、NotebookLM 虛擬環境、登入資料或測試快取
- 第三方授權：保留各技能原有的 `LICENSE`、`NOTICE` 與來源資訊；根目錄不覆蓋各自條款

## 本次通用化調整

- 縮小容易誤觸的描述，補上相近 Skills 的明確邊界。
- `design-system`、`ui-styling`、`huashu-design`、`playwright-interactive`、`humanizer-zh-tw`、`notebooklm` 等長流程改為精簡入口，詳細規則按需要讀取。
- 保留 Word、Obsidian、Zotero、外部服務及刪除操作的安全與權限限制。
- CI 修復區分唯讀診斷和使用者已明確授權的修正，避免重複批准流程。
- 研究 Skills 補上輸出 schema、完成條件、驗證方式與部分失敗處理。
- Figma、NotebookLM、research-hub、互動式瀏覽器和模型委派流程會先檢查工具與登入；缺少前提時停止，不模擬成功。
- 修正失效參考連結、作者電腦絕對路徑和與當前 host 綁定的操作前提。
- `ui-ux-pro-max` 從固定公開上游提交更新資料與腳本。
- `zotero-skills` 補回公開上游的腳本與操作參考，公開版只從環境變數讀取憑證。
- Shell 腳本統一使用 LF，避免 WSL Bash 因 CRLF 解析失敗。
- 新增 `.github-maintainer.yml`，讓後續同步持續執行去識別化、授權保留和發佈前驗證。

## 限制

- Windows 執行系統 `quick_validate.py` 時應使用 `python -X utf8`，避免預設 CP950 解碼 UTF-8 Skill 文件。
- 未對真實 Zotero、NotebookLM、Figma 或其他外部帳號執行寫入測試。
- 未進行 Astra、Sol、Luna 的速度或輸出品質基準測試，因此不宣稱模型效果已提升。
