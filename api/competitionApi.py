from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from typing import Optional
import requests
import os
import json
from datetime import datetime, timezone, timedelta

class FormatEnum(str, Enum):
    tree = "tree"
    flat = "flat"
    map = "map"

app = FastAPI()

# 加入 CORS 中介層
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔧 輔助函式：載入分類資料
def load_category_data():
    current_dir = os.path.dirname(__file__)            
    file_path = os.path.join(current_dir, "../data/competionType.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)




@app.get("/contests")
def get_contests(
    page: int = 1,
    timeline: str = "notEnded",
    location: str = "taiwan",
    category: Optional[str] = Query(None, description="例如：119,120,121"),
):
    base_url = "https://api.bhuntr.com/tw/cms/bhuntr/contest"
    category_param = f"&category={category}" if category else ""

    url = (
        f"{base_url}?language=tw&target=competition"
        f"&limit=24&page={page}&sort=mixed"
        f"&timeline={timeline}&location={location}"
        f"{category_param}"
    )

    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "無法取得資料", "status_code": response.status_code}

    data = response.json()
    competitions = data.get("payload", {}).get("list", [])

    # 台灣時區 UTC+8
    tz = timezone(timedelta(hours=8))

    result = []
    for comp in competitions:
        cpName = comp.get("title", "無名稱")
        cpIdentifyLimit = comp.get("identifyLimit", {})
        cpPrizeTop = comp.get("prizeTop", "無最高獎金")
        cpStartTime = comp.get("startTime", None)
        cpEndTime = comp.get("endTime", None)
        cpOrganizer = comp.get("organizerTitle", "無主辦單位")
        cpHref = "https://bhuntr.com/tw/competitions/" + comp.get("alias", "無連結")

        # 轉換時間戳記 -> 可讀日期
        def ts_to_str(ts):
            if ts:
                return datetime.fromtimestamp(ts, tz).strftime("%Y-%m-%d %H:%M:%S")
            return None

        cpStartTimeStr = ts_to_str(cpStartTime)
        cpEndTimeStr = ts_to_str(cpEndTime)

        # 整理獎項資訊
        cpPrize = []
        cpPrizeFields = comp.get("prizeFields", {}).get("bundles", [])
        for cpPrizeField in cpPrizeFields:
            cpPrizeName2 = cpPrizeField.get("machineName", "")
            cpPrizeName = comp.get("translatePrizeFields", {}).get(cpPrizeName2, {}).get("displayName", "")

            details = cpPrizeField.get("details", [])
            prize_data = {
                "cpPrizeName": cpPrizeName,
                "cpPrizeName2": None,
                "cpPrizeValue": None
            }

            for detail in details:
                machineName = detail.get("machineName", "")
                displayName = comp.get("translatePrizeFields", {}).get(machineName, {}).get("displayName", "")
                value = detail.get("value", None)

                if displayName and prize_data["cpPrizeName2"] is None:
                    prize_data["cpPrizeName2"] = displayName
                if value is not None:
                    prize_data["cpPrizeValue"] = value

            cpPrize.append(prize_data)

        # 僅限大學生的比賽才輸出
        if cpIdentifyLimit.get("university"):
            result.append({
                "cpName": cpName,
                "cpIdentifyLimit": cpIdentifyLimit,
                "cpPrizeTop": cpPrizeTop,
                "cpStartTime": cpStartTimeStr,
                "cpEndTime": cpEndTimeStr,
                "cpOrganizer": cpOrganizer,
                "cpPrize": cpPrize if cpPrize else "請至官網查看",
                "cpHref": cpHref
            })

    return {"request_url": url, "result": result}

@app.get("/categories")
def get_categories(
    format: FormatEnum = Query(
        FormatEnum.tree, description="資料格式選項", example="tree"
    )
):
    data = load_category_data()

    if format == FormatEnum.flat:
        flat = []
        for cat in data:
            flat.append({"id": cat["id"], "name": cat["translateTitle"]["tw"]})
            if cat.get("children"):
                for child in cat["children"]:
                    flat.append({"id": child["id"], "name": child["translateTitle"]["tw"]})
        return flat

    elif format == FormatEnum.map:
        mapping = {}
        for cat in data:
            mapping[cat["id"]] = cat["translateTitle"]["tw"]
            if cat.get("children"):
                for child in cat["children"]:
                    mapping[child["id"]] = child["translateTitle"]["tw"]
        return mapping

    else:
        return data
