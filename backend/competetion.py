import requests
import json
url="https://api.bhuntr.com/tw/cms/bhuntr/contest?language=tw&target=competition&limit=24&page={page}&sort=mixed&timeline=notEnded&location=taiwan"
result = []
for page in range(1):
    response=requests.get(url.format(page=page))
    if response.status_code == 200:
        data = response.json()
        competitions = data.get('payload',{}).get('list',[])
        for n in range(len(competitions)):
            cpName = competitions[n].get('title', '無名稱')
            cpIdentifyLimit= competitions[n].get('identifyLimit', '無限制')
            cpPrizeTop=competitions[n].get('prizeTop', '無最高獎金')
            cpStartTime= competitions[n].get('startTime', '無開始時間')
            cpEndTime= competitions[n].get('endTime', '無截止時間')
            cpOrganizer = competitions[n].get('organizerTitle', '無主辦單位')
            cpHref="https://bhuntr.com/tw/competitions/"+competitions[n].get('alias', '無連結')
            cpPrizeFields = competitions[n].get('prizeFields', {}).get('bundles', [])
            cpPrize = []
            cpPrizeFields = competitions[n].get('prizeFields', {}).get('bundles', [])

            for cpPrizeField in cpPrizeFields:
                # 取得分類名稱（例如：第一名、第二名）
                cpPrizeName2 = cpPrizeField.get('machineName', '')
                cpPrizeName = competitions[n].get('translatePrizeFields', {}).get(cpPrizeName2, {}).get('displayName', '')

                details = cpPrizeField.get('details', [])
                
                # 初始化獎項內容
                prize_data = {
                    'cpPrizeName': cpPrizeName,
                    'cpPrizeName2': None,
                    'cpPrizeValue': None
                }

                for detail in details:
                    machineName = detail.get('machineName', '')
                    displayName = competitions[n].get('translatePrizeFields', {}).get(machineName, {}).get('displayName', '')
                    value = detail.get('value', None)

                    # 如果這筆是獎狀類型，記到 cpPrizeName2
                    if displayName and prize_data['cpPrizeName2'] is None:
                        prize_data['cpPrizeName2'] = displayName

                    # 如果這筆是金額，記到 cpPrizeValue
                    if value is not None:
                        prize_data['cpPrizeValue'] = value

                # 加入整合後的獎項
                cpPrize.append(prize_data)
            if cpIdentifyLimit['university']:
                cpPrize=cpPrize if cpPrize else '請至官網查看'
                result.append({
                    'cpName': cpName,
                    'cpIdentifyLimit': cpIdentifyLimit,
                    'cpPrizeTop': cpPrizeTop,
                    'cpStartTime': cpStartTime,
                    'cpEndTime': cpEndTime,
                    'cpOrganizer': cpOrganizer,
                    'cpPrize': cpPrize,
                    'cpHref': cpHref
                })

with open("competition.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)