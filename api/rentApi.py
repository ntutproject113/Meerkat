from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List
import requests
import json
import os

app = FastAPI()

# 允許跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# ===== 設備 mapping =====
equipment_mapping = {}

def fetch_equipment_mapping():
    url = "https://rent.houseprice.tw/api/RentCaseOption/Equipments.GET"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = response.json().get('data', {})
        for category in data.values():
            if isinstance(category, list):
                for item in category:
                    equipment_mapping[item['value']] = item['key']

@app.on_event("startup")
def startup_event():
    fetch_equipment_mapping()

# ===== 根據單一區域 sid 撈租屋 =====
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List
import requests
import json
import os

app = FastAPI()

# ===== CORS 設定 =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== 設備 mapping =====
equipment_mapping = {}

def fetch_equipment_mapping():
    url = "https://rent.houseprice.tw/api/RentCaseOption/Equipments.GET"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = response.json().get('data', {})
        for category in data.values():
            if isinstance(category, list):
                for item in category:
                    equipment_mapping[item['value']] = item['key']

@app.on_event("startup")
def startup_event():
    fetch_equipment_mapping()

# ===== 租屋查詢：支援多個 sid =====
@app.get("/rents_by_sid")
def get_rents_by_sid(
    sids: str,  # 例如 "5-10-8"
    pages: int = Query(3, ge=1, le=10),
    price_min: int = Query(0, ge=0),
    price_max: int = Query(100000, ge=0)
):
    headers = {"User-Agent": "Mozilla/5.0"}
    result = []

    # 拆分多個 sid
    sid_list = sids.split("-")

    for sid in sid_list:
        url_template = f"https://rent.houseprice.tw/api/RentCaseList/Search/21_usage/{sid}_zip/?p={{page}}"

        for page in range(1, pages + 1):
            url = url_template.format(page=page)
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code != 200:
                continue

            data = response.json()
            rent_list = data.get('data', {}).get('rentCaseInfo', [])

            for rent in rent_list:
                rent_price = rent.get('rentPrice', 0)
                # 價格篩選
                if not (price_min <= rent_price <= price_max):
                    continue

                rentId = rent['caseSid']
                rentSeq = rent['seqNo']
                rentApiHref = f"https://rent.houseprice.tw/api/RentCaseDetail/{rentId}"
                response2 = requests.get(rentApiHref, headers=headers, verify=False)

                if response2.status_code != 200:
                    continue

                detailData = response2.json()
                limitInfo = detailData.get('data', {}).get('limitInfo', {})
                jobLimitation = limitInfo.get('jobLimitation', [])

                if any("學生" in str(item) for item in jobLimitation):
                    equipment_ids = [
                        e["id"]
                        for e in detailData.get('data', {}).get('baseInfo', {}).get('equipments', [])
                        if e.get("isSelected")
                    ]
                    equipment_names = [equipment_mapping.get(eid, f"未知設備({eid})") for eid in equipment_ids]

                    rent_result = {
                        'rentName': rent['caseName'],
                        'rentType': rent['purposeName'],
                        'houseType': rent['buildingStyle'],
                        'rentPrice': rent_price,
                        'transportation': rent.get('mrtStationInfos', []),
                        'rentAdress': rent['city'] + rent['district'] + rent['road'],
                        'equipment': equipment_names,
                        'publishDate': rent['publishTime'],
                        'limitInfo': limitInfo,
                        'rentPictureHref': rent['pictureInfo']['coverImageUrl'],
                        'rentHref': f"https://rent.houseprice.tw/house/{rentId}_{rentSeq}"
                    }
                    result.append(rent_result)

    return result

# 靜態檔案（ 給前端抓選單）
app.mount("/data", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "..", "data")), name="data")