from fastapi import FastAPI,Path,Query
from typing import Annotated
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse 

app=FastAPI()#產生物件
"""@app.get("/")
def index():
    return ("test/test.html")"""
@app.get("/HELLO")
def hello(name:Annotated[str,Query(min_length=2,max_length=10)]):
    message = f"Hello, {name}!"
    return {"message": message}
@app.get("/square/{number}")
def square(number:Annotated[int,Path(ge=1)]):
    number = int(number)
    return {"result": number * number}
@app.get("/mut")
def mut(
    n1:Annotated[int,Query(ge=0,le=15)],
    n2:Annotated[int,Query(ge=0,le=15)]):
    n1 = int(n1)
    n2 = int(n2)
    return {"result": n1 * n2}

app.mount("/", StaticFiles(directory="test", html=True))