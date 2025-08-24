from fastapi import FastAPI, Query
from typing import List, Optional
import json
import os

app = FastAPI(title="Scholarship API", description="提供大學生的獎助學金查詢 API")

def load_scholarship():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "../data/schoolarship.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
    
# 自動分類函式
def categorize(item):
    name = item["ContentPlaceHolder1_divName"]
    other = item.get("ContentPlaceHolder1_divOther", "")

    if "急難" in name or "濟助" in name:
        category = "急難救助"
    elif "技藝" in name or "體育" in name or "藝術" in name:
        category = "才藝技藝"
    elif "服務學習" in name:
        category = "服務學習"
    elif "資訊" in name or "研究" in name:
        category = "資訊/研究計畫"
    elif "清寒" in item.get("ContentPlaceHolder1_divQualification", ""):
        category = "清寒助學"
    else:
        category = "一般獎學金"

    # 地區
    # 地區判斷
    addr = item.get("ContentPlaceHolder1_divAddress", "不拘")

    north_keywords = ["台北", "臺北","新北", "基隆", "宜蘭", "新竹", "桃園"]
    central_keywords = ["台中","臺中", "彰化", "苗栗", "南投", "雲林"]
    south_keywords = ["台南", "高雄", "屏東", "嘉義"]
    east_keywords = ["花蓮", "台東","臺東"]

    if any(kw in addr for kw in north_keywords):
        region = "北部"
    elif any(kw in addr for kw in central_keywords):
        region = "中部"
    elif any(kw in addr for kw in south_keywords):
        region = "南部"
    elif any(kw in addr for kw in east_keywords):
        region = "東部"
    elif "不拘" in addr:
        region = "全國"
    else:
        region = "其他"


    return category, region


@app.get("/scholarships")
def get_scholarships(
    category: Optional[str] = Query(None, description="獎學金類別（急難救助、才藝技藝、資訊/研究計畫、清寒助學）"),
    region: Optional[str] = Query(None, description="地區（北部、中部、南部、東部、全國）"),
    identity: Optional[str] = Query(None, description="獎助身分（低收入戶、中低收入戶、原住民、身心障礙、不拘...）"),
    qualification: Optional[str] = Query(None, description="獎助資格（清寒、成績優良、服務學習、特殊境遇...）"),
    sort: Optional[str] = Query(None, description="金額排序（asc=由小到大, desc=由大到小）")
):
    results = []
    scholarships = load_scholarship()

    for item in scholarships:
        category_label, region_label = categorize(item)

        # 數字處理
        min_amt = int(item.get("min_amount", "0").replace(",", "").replace("無法擷取", "0"))
        max_amt = int(item.get("max_amount", "0").replace(",", "").replace("無法擷取", "0"))
        avg_amt = (min_amt + max_amt) // 2

        # 篩選條件
        if category and category != category_label:
            continue
        if region and region != region_label:
            continue
        if identity and identity not in item.get("ContentPlaceHolder1_divIdentity", ""):
            continue
        if qualification and qualification not in item.get("ContentPlaceHolder1_divQualification", ""):
            continue

        # 加入分類資訊
        item["category"] = category_label
        item["region"] = region_label
        item["avg_amount"] = avg_amt
        results.append(item)

    # 排序
    if sort == "asc":
        results = sorted(results, key=lambda x: x["avg_amount"])
    elif sort == "desc":
        results = sorted(results, key=lambda x: x["avg_amount"], reverse=True)

    return {"count": len(results), "data": results}