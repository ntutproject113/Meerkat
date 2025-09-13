# API 文件 – Competition, Rent, Members & Todo API

## 概述

此專案整合四大功能 API：

1. **Competition API** – 提供比賽清單與分類資訊。
2. **Rent API** – 提供租屋清單與地區資訊，封裝自 houseprice.tw API。
3. **Members API** – 提供會員註冊、登入與個人資料操作。
4. **Todo API** – 提供會員個人 Todo 清單操作。

所有 API 均採用 **FastAPI** 實作，支援 CORS，方便前端（如 Vue / React）直接串接。

---

# **1. Competition API**

## 1.1 `/contests` – 取得比賽清單

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
GET /contests?page=2&timeline=submitProcessing&location=taiwan&category=119%2C120%2C121
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
GET /rents?page=2&area_ids=1-2-3&price=20000&casetype=0&fee=true
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

```
GET /areas/tree
```

```bash
GET /areas/tree
```

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

```
GET /areas/{city_sid}
```

| 名稱         | 型別       | 必填 | 說明              |
| ---------- | -------- | -- | --------------- |
| `city_sid` | `string` | 是  | 縣市編號 cityNumber |

```bash
GET /areas/1
```

```json
{
  "city": "台北市",
  "sids": ["101", "102", "103"]
}
```

---

# **3. Members API**

## /members/register – 註冊會員

```
POST /members/register
```

```json
{
  "username": "testuser",
  "email": "test@test.com",
  "password": "123456"
}
```

```json
{
  "username": "testuser",
  "email": "test@test.com",
  "member_seq": 1
}
```

---

## /members/login – 登入會員

```
POST /members/login
```

```json
{
  "username": "testuser",
  "password": "123456"
}
```

```json
{
  "message": "登入成功"
}
```

---

## /members/me – 取得會員資訊

```
GET /members/me
```

```bash
GET /members/me
```

```json
{
  "user": {
    "username": "testuser",
    "email": "test@test.com"
  },
  "profile": {
    "member_id": "64f1234567",
    "name": "",
    "gender": "",
    "phone": "",
    "school": "",
    "department": "",
    "grade": "",
    "interests": [],
    "skills": [],
    "plan_after_graduation": "升學"
  }
}
```

---

## /members/profile – 更新會員詳細資料

```
POST /members/profile
```

```json
{
  "name": "小明",
  "phone": "0912345678",
  "school": "臺灣大學"
}
```

```json
{
  "member_id": "64f1234567",
  "name": "小明",
  "gender": "",
  "phone": "0912345678",
  "school": "臺灣大學",
  "department": "",
  "grade": "",
  "interests": [],
  "skills": [],
  "plan_after_graduation": "升學"
}
```

---

# **4. Todo API**

# Todo API

## /todos – 新增 Todo

```
POST /todos
```

```json
{
  "name": "買牛奶",
  "completed": false,
  "todo_date": "2025-09-09",
  "priority": "medium",
  "tags": ["shopping", "daily"]
}
```
回傳id等資料
```json
{
  "id": "1-1",
  "name": "買牛奶",
  "completed": false,
  "todo_date": "2025-09-09T00:00:00",
  "priority": "medium",
  "tags": ["shopping", "daily"]
}
```

---

## /todos – 查詢 Todo

```
GET /todos
```

| 名稱          | 型別        | 必填 | 說明                     |
| ----------- | --------- | -- | ---------------------- |
| `todo_date` | `string`  | 否  | 篩選指定日期，格式 YYYY-MM-DD   |
| `tags`      | `array`   | 否  | 篩選包含所有標籤               |
| `priority`  | `string`  | 否  | 篩選優先度: low/medium/high |
| `completed` | `boolean` | 否  | 篩選完成狀態                 |

```bash
GET /todos?todo_date=2025-09-09&tags=shopping,daily&priority=medium&completed=false
```

```json
[
  {
    "id": "1-1",
    "name": "買牛奶",
    "completed": false,
    "todo_date": "2025-09-09T00:00:00",
    "priority": "medium",
    "tags": ["shopping", "daily"]
  }
]
```

---

## /todos/{todo\_id} – 更新 Todo

```
PUT /todos/{todo_id}
```

| 名稱        | 型別       | 必填 | 說明             |
| --------- | -------- | -- | -------------- |
| `todo_id` | `string` | 是  | Todo ID，例如 1-1 |

```json
{
  "name": "買牛奶+麵包",
  "completed": true,
  "priority": "high",
  "tags": ["shopping", "daily"]
}
```
回傳
```json

{
  "id": "1-1",
  "name": "買牛奶+麵包",
  "completed": true,
  "todo_date": "2025-09-09T00:00:00",
  "priority": "high",
  "tags": ["shopping", "daily"]
}
```

---

## /todos/{todo\_id} – 刪除 Todo

```
DELETE /todos/{todo_id}
```

| 名稱        | 型別       | 必填 | 說明             |
| --------- | -------- | -- | -------------- |
| `todo_id` | `string` | 是  | Todo ID，例如 1-1 |

```bash
DELETE /todos/1-1
```

```json
{
  "message": "Todo deleted"
}
```
