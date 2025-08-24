# API 文件 – Competition & Rent API

## 概述

此專案整合兩大功能 API：

1. **Competition API** – 提供比賽清單與分類資訊。
2. **Rent API** – 提供租屋清單與地區資訊，封裝自 houseprice.tw API。

所有 API 均採用 **FastAPI** 實作，支援 CORS，方便前端（如 Vue / React）直接串接。

# **1. Competition API**

## 1.1 `/contests` – 取得比賽清單

**方法**

```
GET /contests
```

**查詢參數**

| 名稱         | 型別       | 預設值        | 必填 | 說明               | 可選值                                                                             |
| ---------- | -------- | ---------- | -- | ---------------- | ------------------------------------------------------------------------------- |
| `page`     | `int`    | `1`        | 否  | 頁碼（從 1 開始）       | 1, 2, 3, ...                                                                    |
| `timeline` | `string` | `notEnded` | 否  | 比賽時間狀態           | `notEnded`（尚未結束）<br>`submitProcessing`（投稿中）<br>`nearWinnerAnnouncement`（近期得獎宣布） |
| `location` | `string` | `taiwan`   | 否  | 比賽地點             | 例如 `taiwan`, `global`                                                           |
| `category` | `string` | `null`     | 否  | 比賽分類 ID，可多個用逗號分隔 | 例如 `119`, `119,120,121`                                                         |

**範例**

```bash
# 範例 1：取得第 2 頁，投稿中的比賽（台灣地區）
GET /contests?page=2&timeline=submitProcessing&location=taiwan&category=119%2C120%2C121
# 範例 2：取得分類 119 和 120 的比賽
GET /contests?category=119,120
```

**回應格式**

```json
{
  "request_url": "https://api.bhuntr.com/tw/cms/bhuntr/contest?...",
  "result": {
    "data": [
      {
        "id": 123,
        "title": "設計大賽",
        "deadline": "2025-08-31",
        "location": "Taiwan",
        "category": "119"
      }
    ]
  }
}
```

---

## 1.2 `/categories` – 取得比賽分類

**方法**

```
GET /categories
```

**查詢參數**

| 名稱       | 型別       | 預設值    | 必填 | 說明   | 可選值            |
| -------- | -------- | ------ | -- | ---- | -------------- |
| `format` | `string` | `tree` | 否  | 回傳格式 | `tree`, `list` |

**範例**

```bash
GET /categories?format=tree
```

**回應格式**

```json
[
  {
    "id": "119",
    "name": "平面設計",
    "children": [
      { "id": "120", "name": "海報設計" },
      { "id": "121", "name": "LOGO 設計" }
    ]
  }
]
```

---

# **2. Rent API**

## 2.1 `/rents` – 取得租屋資訊

**方法**

```
GET /rents
```

**查詢參數**

| 名稱         | 型別       | 預設值                          | 必填 | 說明                                             |
| ---------- | -------- | ---------------------------- | -- | ---------------------------------------------- |
| `area_ids` | `string` | `5-10-8-12-9-3-7-4-6-1-2-11` | 否  | 地區 ID，使用 `-` 分隔，如 `27-26-15`                   |
| `price`    | `int`    | `15000`                      | 否  | 價格上限                                           |
| `casetype` | `string` | `0`                          | 否  | 房型類別：0=不限，1=整層住家，2=獨立套房，3=分租套房，4=雅房，可多選如 `1-2` |
| `page`     | `int`    | `1`                          | 否  | 頁碼（從 1 開始）                                     |
| `fee`      | `bool`   | `true`                       | 否  | 是否包含管理費                                        |

**範例**

```bash
# 範例 1：取得台北市第 2 頁，不限房型，含管理費
GET /rents?page=2&area_ids=1-2-3&price=20000&casetype=0&fee=true

# 範例 2：取得新北市套房（不含管理費）
GET /rents?area_ids=5-6&casetype=2&fee=false
```

**回應格式**

```json
{
  "request_url": "https://rent.houseprice.tw/api/RentCaseList/Search/...",
  "total_count": 12,
  "result": [
    {
      "rentSeq": 123,
      "rentName": "捷運旁套房",
      "rentType": "獨立套房",
      "houseType": "電梯大樓",
      "rentPrice": 15000,
      "transportation": [],
      "rentAddress": "台北市信義區信義路",
      "equipmentIds": [1, 2, 3],
      "publishDate": "2025-08-15",
      "limitInfo": {},
      "rentPictureHref": "https://...jpg",
      "rentHref": "https://rent.houseprice.tw/house/123_456"
    }
  ]
}
```

---

## 2.2 `/areas/tree` – 取得地區樹狀資料

**方法**

```
GET /areas/tree
```

**範例**

```bash
GET /areas/tree
```

**回應格式**

```json
[
  {
    "cityNumber": "1",
    "cityName": "台北市",
    "areaList": [
      { "sid": "101", "name": "中正區" },
      { "sid": "102", "name": "大同區" }
    ]
  }
]
```

---

## 2.3 `/areas/{city_sid}` – 根據縣市取得區域 SID

**方法**

```
GET /areas/{city_sid}
```

**參數**

| 名稱         | 型別       | 必填 | 說明              |
| ---------- | -------- | -- | --------------- |
| `city_sid` | `string` | 是  | 縣市編號 cityNumber |

**範例**

```bash
GET /areas/1
```

**回應格式**

```json
{
  "city": "台北市",
  "sids": ["101", "102", "103"]
}
```


