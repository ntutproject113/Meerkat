import requests
import json
url0="https://rent.houseprice.tw/api/RentCaseList/Search/21_usage/5-10-8-12-9-3-7-4-6-1-2-11_zip/?p={page}"
result = []
for page in range(1, 4):
    url = url0.format(page=page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()     
        rent_list = data.get('data', {}).get('rentCaseInfo', [])
        for rent in rent_list:
            rentId=rent['caseSid']
            rentName=rent['caseName']
            rentSeq=rent['seqNo']
            rentType=rent['purposeName']
            rentCity=rent['city']
            rentDistrict=rent['district']
            rentRolad=rent['road']
            rentAdress=rentCity+rentDistrict+rentRolad
            transportation =rent.get('mrtStationInfos', [])
            rentPrice=rent['rentPrice']
            houseType=rent['buildingStyle']
            publishDate=rent['publishTime']
            rentPictureHref=rent['pictureInfo']['coverImageUrl']
            rentHref='https://rent.houseprice.tw/house/'+str(rentId)+'_'+str(rentSeq)
            rentApiHref='https://rent.houseprice.tw/api/RentCaseDetail/'+str(rentId)
            response2 = requests.get(rentApiHref, headers=headers, verify=False)
            if response2.status_code == 200:
                detailData= response2.json()
                equipments = detailData.get('data', {}).get('baseInfo', {}).get('equipments', {})
                equipmentIds = [item["id"] for item in equipments if item["isSelected"]]
                limitInfo =  detailData.get('data', {}).get('limitInfo', {})
                jobLimitation= limitInfo.get('jobLimitation', [])
                if any("學生" in str(item) for item in jobLimitation):
                    result.append({
                        'rentName': rentName,
                        'rentType': rentType,
                        'houseType': houseType,
                        'rentPrice': rentPrice,
                        'transportation': transportation,
                        'rentAdress': rentAdress,
                        'equipmentIds': equipmentIds,
                        'publishDate': publishDate,
                        'limitInfo': limitInfo,
                        'rentPictureHref':rentPictureHref,
                        'rentHref': rentHref,
                        
                        
                    })
print(result)
open("rrent.json", "w", encoding="utf-8").write(json.dumps(result, indent=4, ensure_ascii=False))
print(data)
