from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import json
import os

app = FastAPI(
    title="實習職缺靜態 API",
    description="提供透過爬蟲產生的靜態 JSON 清單",
    version="1.0.0"
)

# 掛載 static 資料夾（正確路徑）
app.mount("/data", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "..", "data")), name="data")

# 讀取 JSON 檔到記憶體，加快存取速度
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "intern.json"))
if not os.path.exists(JSON_PATH):
    raise FileNotFoundError(f"{JSON_PATH} 不存在，請先放入爬蟲輸出檔案")

with open(JSON_PATH, encoding="utf-8") as f:
    intern_list = json.load(f)

# Pydantic 模型定義（可選，若要自動校驗回傳結構）
class Intern(BaseModel):
    jobName: str
    jobRo: str
    jobAddrNoDesc: str
    jobAddress: str
    description: str
    optionEdu: str
    periodDesc: str
    salaryLow: str
    salaryHigh: str
    salaryDesc: str
    custName: str
    appearDate: str

class ResponseModel(BaseModel):
    success: bool
    count: int
    data: list[Intern]

@app.get("/api/internapi", response_model=ResponseModel)
async def get_interns():
    """
    回傳所有實習職缺清單 (靜態 JSON)
    - success: API 回傳狀態
    - count: 資料筆數
    - data: 職缺清單
    """
    return {
        "success": True,
        "count": len(intern_list),
        "data": intern_list
    }

@app.get("/api/internapi/{index}", response_model=Intern)
async def get_intern_by_index(index: int):
    """
    依索引取得單筆職缺
    - index: 從 0 開始的陣列位置
    """
    try:
        return intern_list[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="職缺索引不存在")

# 若要更新 JSON，可額外提供觸發端點，但建議以排程外部執行爬蟲覆蓋檔案
# @app.post("/api/intern/refresh")
# async def refresh_interns():
#     # 呼叫爬蟲腳本並重讀 intern.json
#     ...

# 啟動： uvicorn app:app --host 0.0.0.0 --port 8000
