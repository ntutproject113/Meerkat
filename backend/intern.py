import requests as req
import time
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ntutproject113:113wiwibadbad@meetkats.rven60f.mongodb.net/?retryWrites=true&w=majority&appName=Meetkats"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

url0 = "https://www.104.com.tw/jobs/search/list?asc=0&hotJob=0&jobsource=students_intern_PC&keyword=%E8%B3%87%E8%A8%8A%20%E8%B2%A1%E9%87%91&order=12&page={page}&pagesize=30&ro=2&rostatus=1024&showDutyTime=1&tab=intern"
result = []
for page in range(1,4):
    url = url0.format(page=page)
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "Referer": "https://www.104.com.tw/jobs/main/students/?tab=intern&ro=2&pagesize=30&jobsource=students_intern_PC&showDutyTime=1&hotJob=0&rostatus=1024&keyword=%E8%B3%87%E8%A8%8A+%E8%B2%A1%E9%87%91&order=12&asc=0&area=&page={page}"
    ""
    }
    time.sleep(5)
    response= req.get(url, headers=headers)
    if response.status_code == 200:
     data = response.json()
     for job in data['data']['list']:
        jobName=job['jobName']
        jobRo=job['jobRo']
        jobAddrNoDesc=job['jobAddrNoDesc']
        jobAddress=job['jobAddress']
        description=job['description']
        optionEdu=job['optionEdu']
        periodDesc=job['periodDesc']
        salaryLow=job['salaryLow']
        salaryHigh=job['salaryHigh']
        salaryDesc=job['salaryDesc']
        custName=job['custName']
        appearDate=job['appearDate']
        result.append({
            'jobName': jobName,
            'jobRo': jobRo,
            'jobAddrNoDesc': jobAddrNoDesc,
            'jobAddress': jobAddress,
            'description': description,
            'optionEdu': optionEdu,
            'periodDesc': periodDesc,
            'salaryLow': salaryLow,
            'salaryHigh': salaryHigh,
            'salaryDesc': salaryDesc,
            'custName': custName,
            'appearDate': appearDate
        })

db=client.intern
collection=db.internIFM 
internDB=collection.insert_many(result)
print("資料已經寫入MongoDB")


#open("intern.json", "w", encoding="utf-8").write(json.dumps(result, indent=4, ensure_ascii=False))






