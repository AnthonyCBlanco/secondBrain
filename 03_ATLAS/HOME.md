# 🏡 HOME MOC

## 📁 Spaces
- [[School MOC]] 
- [[Personal MOC]] 
- [[Projects MOC]]

## 🎯 Active Focus
- [[Outline]]
- [[SUMMER 2026]]

## ⏱️ Quick Access
- `="[[" + dateformat(date(today), "yyyy-MM-dd") + "|DAILY NOTE]]"`

---
## 🗂️ Vault Overview
```dataview
TABLE length(rows.file.name) AS "Notes Count"
FROM "01_SPACES"
WHERE !contains(file.name, "MOC")
GROUP BY split(file.folder, "/")[1] AS "Space"
```