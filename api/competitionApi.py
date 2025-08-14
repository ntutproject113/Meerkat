# main.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from typing import Optional
import requests
import os
import json
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

# ✅ 原本的查詢 API
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
    data = response.json()

    return {
        "request_url": url,
        "result": data
    }

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