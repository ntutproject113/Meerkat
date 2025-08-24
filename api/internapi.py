from fastapi import FastAPI, Query
from typing import Optional  
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
import requests
import os
import json

app = FastAPI(title="實習api")
# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class CategoryEnum(str, Enum):
    areas = "areas"
    industries = "industries"
    jobcats = "jobcats"

def load_json(filename: str):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "../data", filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def flatten_tree(data, result):
    for item in data:
        result[item["no"]] = item["des"]
        if "n" in item and isinstance(item["n"], list):
            flatten_tree(item["n"], result)
    return result

CATEGORY_FILE_MAP = {
    "areas": "internArea.json",
    "industries": "internIndustry.json",
    "jobcats": "internJobCat.json"
}
@app.get("/jobs")
def get_jobs(
    keyword:  Optional[str]  = Query("%E8%B3%87%E6%9D%90", description="搜尋關鍵字"),
    page: int = Query(1, description="頁碼"),
    asc: int = Query(0, description="排序方向，0=降冪、1=升冪"),
    order: int = Query(12, description="排序方式"),
    edu: int = Query(4, description="大學學歷以上"),
    area: str = Query(6001000000, description="工作地區代碼"),
    jobcat: Optional[str] = Query(None, description="職務分類代碼"),
):
    result = []
    url_template = (
        "https://www.104.com.tw/jobs/search/api/jobs?"
        "asc={asc}&hotJob=0&jobsource=students_intern_PC&keyword={keyword}&"
        "order={order}&page={page}&pagesize=30&rostatus=1024&showDutyTime=1&tab=intern"
    )
    if edu:
        url_template += f"&edu={edu}"
    if area:
        url_template += f"&area={area}"
    if jobcat:
        url_template += f"&jobcat={jobcat}"

    url = url_template.format(keyword=keyword, page=page, asc=asc, order=order)

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.104.com.tw/jobs/main/students/"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for job in data.get('data', []):
            job_doc = {
                'jobNo': job.get('jobNo', ''),
                'jobName': job.get('jobName', ''),
                'jobRo': job.get('jobRo', ''),
                'jobCat': job.get('jobCat', ''),
                'major': job.get('major', '不拘'),
                'jobAddrNoDesc': job.get('jobAddrNoDesc', ''),
                'jobAddress': job.get('jobAddress', ''),
                'description': job.get('description', ''),
                'optionEdu': job.get('optionEdu', ''),
                'periodDesc': job.get('periodDesc', '不拘'),
                'salaryLow': job.get('salaryLow', 0),
                'salaryHigh': job.get('salaryHigh', 0),
                'salaryDesc': job.get('salaryDesc', ''),
                'custName': job.get('custName', ''),
                'appearDate': job.get('appearDate', ''),
                'jobUrl': job.get('link', {}).get('job', '')  
            }
            result.append(job_doc)
    return {"page": page, "count": len(result), "jobs": result}
@app.get("/{category}")
def get_category_tree(category: CategoryEnum):
    return load_json(CATEGORY_FILE_MAP[category.value])

# 取得展平的 map 對照表
@app.get("/map/{category}")
def get_category_map(category: CategoryEnum):
    data = load_json(CATEGORY_FILE_MAP[category.value])
    return flatten_tree(data, {})

