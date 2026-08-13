# 公開版驗證紀錄

驗證日期：2026-08-13

## 結果

- 技能目錄：41
- 包含 `SKILL.md`：41
- 技能格式驗證：41/41 通過
- 安裝腳本：支援 `-WhatIf`，預設不覆寫既有技能
- 公開內容：不包含原使用者的絕對路徑、帳號、私人倉庫名稱或專案資料
- 憑證：不包含 API key、OAuth token、Cookie、`auth.json`、瀏覽器狀態或 Codex 記憶
- 大型來源：不包含外掛快取、`node_modules`、NotebookLM 虛擬環境或登入資料
- 第三方授權：保留技能資料夾原有的 `LICENSE`、`NOTICE` 與 `PROVENANCE`；根目錄不覆蓋各自條款

## 通用化調整

- `issue-ledger` 的特定專案與資料庫範例已換成一般範例。
- `obsidian-github-backup` 不再內建 Vault 路徑、GitHub 使用者或倉庫；兩個值改成必要參數。
- `github-maintainer` 保留可跨倉庫使用的維護規則。
- `design-system` 與 `ui-styling` 的技能名稱改為標準小寫連字號格式。
- 舊版頂層 metadata 已調整成目前驗證器接受的格式。
- `ui-ux-pro-max` 原本缺少連結目標；已從其公開上游固定提交補入 `data` 與 `scripts`，並保留 MIT 授權與來源紀錄。
- 已排除測試產生的 `.coverage` 狀態檔。

## 注意事項

技能中可能包含各自的第三方授權或依賴。根目錄未宣告一份涵蓋所有內容的統一授權；重新發布或商業使用前，請逐項查看來源檔案與 `THIRD_PARTY_NOTICE.md`。
