from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
app=FastAPI()
app.mount("/data", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "..", "data")), name="data")
