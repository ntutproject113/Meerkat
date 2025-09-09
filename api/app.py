from fastapi import FastAPI
from member import router as member_router
from todoList import router as todo_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="啟蒙")
# 掛載不同的 API


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 掛載 router
app.include_router(member_router)
app.include_router(todo_router)
