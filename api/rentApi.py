from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# 這裡用 Query 參數，預設抓3頁，可改變
@app.get("/rents")
def get_student_rents(pages: int = Query(3, ge=1, le=10, description="要抓取的頁數，1~10頁")):
    url_template = "https://rent.houseprice.tw/api/RentCaseList/Search/21_usage/5-10-8-12-9-3-7-4-6-1-2-11_zip/?p={page}"
    headers = {"User-Agent": "Mozilla/5.0"}

    result = []

    for page in range(1, pages + 1):  # 依外部傳入的頁數動態決定抓幾頁
        url = url_template.format(page=page)
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code != 200:
            continue

        data = response.json()
        rent_list = data.get('data', {}).get('rentCaseInfo', [])

        for rent in rent_list:
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
                    e["id"] for e in detailData.get('data', {}).get('baseInfo', {}).get('equipments', [])
                    if e.get("isSelected")
                ]
                equipment_names = [equipment_mapping.get(eid, f"未知設備({eid})") for eid in equipment_ids]

                rent_result = {
                    'rentName': rent['caseName'],
                    'rentType': rent['purposeName'],
                    'houseType': rent['buildingStyle'],
                    'rentPrice': rent['rentPrice'],
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
