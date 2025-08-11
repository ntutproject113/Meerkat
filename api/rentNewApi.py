from fastapi import FastAPI, Query, Path    
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
import requests
import os
import json

app = FastAPI(title="租屋資訊 API", description="封裝 houseprice.tw API")

# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 載入地區資料
def load_rent_area():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "../data/rentArea.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# 取得租屋資訊
@app.get("/rents")
def get_rents(
    area_ids: str = Query(..., description="地區 ID，逗號分隔，如 27,26,15"),
    price: Optional[int] = Query(10000, description="價格篩選，預設10000 表示不限"),
    casetype: Optional[int] = Query(1, description="房型類別，預設 1"),
    page: int = Query(1, description="頁碼，從 1 開始"),
):


    base_url = (
        f"https://rent.houseprice.tw/api/RentCaseList/Search/"
        f"21_usage/{area_ids.replace(',', '-')}_zip/-{price}_price/{casetype}_casetype/?p={page}"
    )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }

    response = requests.get(base_url, headers=headers, verify=False)
    result = []

    if response.status_code == 200:
        data = response.json()
        rent_list = data.get("data", {}).get("rentCaseInfo", [])

        for rent in rent_list:
            rentId = rent.get("caseSid")
            rentName = rent.get("caseName")
            rentSeq = rent.get("seqNo")
            rentType = rent.get("purposeName")
            rentCity = rent.get("city") or "NA"
            rentDistrict = rent.get("district") or ""
            rentRoad = rent.get("road") or ""
            rentAddress = rentCity + rentDistrict + rentRoad
            transportation = rent.get("mrtStationInfos", [])
            rentPrice = rent.get("rentPrice")
            houseType = rent.get("buildingStyle")
            publishDate = rent.get("publishTime")
            pictureInfo = rent.get("pictureInfo")
            rentPictureHref = pictureInfo.get("coverImageUrl") if pictureInfo else None

            # 外部來源（如 591）
            caseFromList = rent.get("caseFromList")
            if rentSeq is None and caseFromList:
                for external in caseFromList:
                    result.append({
                        "rentSeq": "外部來源",
                        "rentName": external.get("caseName") or rentName,
                        "rentType": rentType,
                        "houseType": houseType,
                        "rentPrice": external.get("totalPrice") or rentPrice,
                        "transportation": transportation,
                        "rentAddress": rentAddress,
                        "equipmentIds": [],
                        "publishDate": publishDate,
                        "limitInfo": {"note": "資料來自外部網站"},
                        "rentPictureHref": rentPictureHref,
                        "rentHref": external.get("caseUrl"),
                    })
                continue

            # 站內房源
            rentHref = f"https://rent.houseprice.tw/house/{rentId}_{rentSeq}"
            rentApiHref = f"https://rent.houseprice.tw/api/RentCaseDetail/{rentId}"

            response2 = requests.get(rentApiHref, headers=headers, verify=False)
            if response2.status_code == 200:
                detailData = response2.json()
                baseInfo = detailData.get("data", {}).get("baseInfo", {})
                equipments = baseInfo.get("equipments") or []
                equipmentIds = [item["id"] for item in equipments if item.get("isSelected")]

                limitInfo = detailData.get("data", {}).get("limitInfo", {})
                jobLimitation = limitInfo.get("jobLimitation", [])

                if not jobLimitation or any("學生" in str(item) for item in jobLimitation):
                    result.append({
                        "rentSeq": rentSeq,
                        "rentName": rentName,
                        "rentType": rentType,
                        "houseType": houseType,
                        "rentPrice": rentPrice,
                        "transportation": transportation,
                        "rentAddress": rentAddress,
                        "equipmentIds": equipmentIds,
                        "publishDate": publishDate,
                        "limitInfo": limitInfo,
                        "rentPictureHref": rentPictureHref,
                        "rentHref": rentHref,
                    })

    return {
        "request_url": base_url,
        "total_count": len(result),
        "result": result
    }
@app.get("/areas/tree")
def get_area_tree():
    """取得整縣市區域"""
    data = load_rent_area()
    return data
# 取得地區清單
@app.get("/areas/{city_sid}")
def get_area_sids(city_sid: str = Path(..., description="縣市 cityNumber")):
    """根據縣市 cityNumber，回傳該縣市所有區域 sid 清單"""
    data = load_rent_area()
    for city in data:
        if city["cityNumber"] == city_sid:
            sids = [area["sid"] for area in city.get("areaList", [])]
            return {"city": city["cityName"], "sids": sids}
    return {"error": "cityNumber not found"}
