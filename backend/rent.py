import requests
import json

url0 = "https://rent.houseprice.tw/api/RentCaseList/Search/21_usage/5_zip/?p={page}"
result = []

for page in range(1, 2):
    url = url0.format(page=page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        data = response.json()
        rent_list = data.get('data', {}).get('rentCaseInfo', [])

        for rent in rent_list:
            rentId = rent.get('caseSid')
            rentName = rent.get('caseName')
            rentSeq = rent.get('seqNo') 
            rentType = rent.get('purposeName')
            rentCity = rent.get('city') or "NA"
            rentDistrict = rent.get('district') or ""
            rentRoad = rent.get('road') or ""
            rentAddress = rentCity + rentDistrict + rentRoad
            transportation = rent.get('mrtStationInfos', [])
            rentPrice = rent.get('rentPrice')
            houseType = rent.get('buildingStyle')
            publishDate = rent.get('publishTime')
            pictureInfo = rent.get('pictureInfo')
            rentPictureHref = pictureInfo.get('coverImageUrl') if pictureInfo else None

            # 判斷是否為外部來源（591 等）
            caseFromList = rent.get('caseFromList')
            if rentSeq is None and caseFromList:
                for external in caseFromList:
                    result.append({
                        'rentSeq': "外部來源",
                        'rentName': external.get('caseName') or rentName,
                        'rentType': rentType,
                        'houseType': houseType,
                        'rentPrice': external.get('totalPrice') or rentPrice,
                        'transportation': transportation,
                        'rentAdress': rentAddress,
                        'equipmentIds': [], 
                        'publishDate': publishDate,
                        'limitInfo': {"note": "資料來自外部網站，無限制資訊"},
                        'rentPictureHref': rentPictureHref,
                        'rentHref': external.get('caseUrl'),  # 指向外部網站
                    })
                continue  # 已處理，跳過以下內部API查詢

            # 處理站內房源（可用 RentCaseDetail）
            rentSeq = rentSeq 
            rentHref = f"https://rent.houseprice.tw/house/{rentId}_{rentSeq}"
            rentApiHref = f"https://rent.houseprice.tw/api/RentCaseDetail/{rentId}"

            response2 = requests.get(rentApiHref, headers=headers, verify=False)

            if response2.status_code == 200:
                detailData = response2.json()
                baseInfo = detailData.get('data', {}).get('baseInfo', {})
                equipments = baseInfo.get('equipments') or []
                equipmentIds = [item["id"] for item in equipments if item.get("isSelected")]

                limitInfo = detailData.get('data', {}).get('limitInfo', {})
                jobLimitation = limitInfo.get('jobLimitation', [])

                if not jobLimitation or any("學生" in str(item) for item in jobLimitation):
                    result.append({
                        'rentSeq': rentSeq,
                        'rentName': rentName,
                        'rentType': rentType,
                        'houseType': houseType,
                        'rentPrice': rentPrice,
                        'transportation': transportation,
                        'rentAdress': rentAddress,
                        'equipmentIds': equipmentIds,
                        'publishDate': publishDate,
                        'limitInfo': limitInfo,
                        'rentPictureHref': rentPictureHref,
                        'rentHref': rentHref,
                    })

with open("rent.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
