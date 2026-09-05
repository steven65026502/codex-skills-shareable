---
name: huashu-design
description: 用 HTML 製作高保真互動原型、動態視覺 Demo 或設計方向比較。適用於使用者明確要求 HTML 原型、可操作 mockup、動畫展示、設計變體或專家視覺評審；不適用於一般前端功能、PPTX 製作或只需文字建議的任務。影片、配音、音樂及浮水印只在明確要求時加入。
---

# 花叔 Design

用 HTML 作為載體，交付符合任務媒介的高保真視覺作品。入口只負責判斷路徑；細節按需要讀取，避免小任務被完整製作流程綁住。

## 路由

- 互動產品原型或可點擊 mockup：讀 `references/workflow.md`、`references/react-setup.md`，需要裝置框架再讀 `references/design-context.md`。
- 動畫或連續視覺敘事：讀 `references/animations.md` 與 `references/animation-best-practices.md`。
- HTML 幻燈片：只有使用者明確要 HTML deck 時讀 `references/slide-decks.md`；PPTX 改用 slides，圖片型商務簡報改用 imagegen-scene-ppt。
- 設計變體：讀 `references/design-styles.md` 與 `references/tweaks-system.md`。
- 專家評審：讀 `references/critique-guide.md`，只做評審時不要先重做成品。
- 影片、GIF、配音或音訊：僅在使用者明確要求相應輸出時，才讀 `references/video-export.md`、`references/voiceover-pipeline.md` 或 `references/audio-design-rules.md`。
- 原始完整手冊：只有上述文件不足時才讀 `references/full-guide.md`。

## 快速工作流

1. 從使用者需求與現有專案判斷媒介、尺寸、互動範圍與交付檔。
2. 需求已足夠時直接製作；只有會改變整體方向的選擇才詢問。
3. 優先沿用現有框架、資產與設計語言。外部圖像、字型或服務需要可用來源；不可假裝已取得。
4. 做最小可用版本後，依任務風險驗證互動、響應式版面、動畫及匯出結果。
5. 修正已確認問題，再交付檔案、驗證結果與尚未驗證項目。

## 邊界

- 不自動加入浮水印、品牌標記、音樂、音效、配音或影片匯出。
- 不因需求模糊就強制生成三個 Demo；可先提出最多三個文字方向，只有需要視覺比較時才製作變體。
- 不把一般前端 CRUD、單一 CSS 修正或靜態文字建議升級為完整設計流程。
- 不宣稱已通過 Playwright、60 fps、跨瀏覽器或行動裝置檢查，除非實際執行。
- 使用者提供的既有內容、品牌規則與權限限制優先。

## 完成條件

- 指定交付檔可開啟，核心互動或動畫可重現。
- 已在要求的視窗尺寸或輸出格式做相稱檢查，並保存必要證據。
- 沒有未經要求的音訊、浮水印、追蹤碼或外部依賴。
- 若工具、瀏覽器、資產或轉碼器缺失，停止受影響步驟，保留可用產物，清楚報告未完成範圍與可重跑命令。
