from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from enum import Enum
from datetime import date

#  User Model
class UserCreate(BaseModel):
    username: str = Field(..., example="meerkat123")
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    username: str = Field(..., example="meerkat123")
    password: str

class UserOut(BaseModel):
    username: str
    email: EmailStr

#  Profile Model 
class PlanAfterGraduationEnum(str, Enum):
    study = "升學"
    work = "就業"
    unsure = "不清楚"

class ProfileCreate(BaseModel):
    name: str
    gender: str = Field(..., pattern="^(男|女)$")  # 僅允許 "男" 或 "女"
    phone: str
    school: str
    department: str
    grade: str
    interests: Optional[List[str]] = []
    skills: Optional[List[str]] = []
    plan_after_graduation: PlanAfterGraduationEnum = Field(..., example="升學")

class ProfileOut(ProfileCreate):
    member_id: str

#Todo Model 
class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

# 前端送給後端的資料
class TodoCreate(BaseModel):
    name: str = Field(..., example="背 20 個單字")
    completed: Optional[bool] = False
    todo_date: Optional[date] = Field(default_factory=date.today)
    priority: Optional[Priority] = Field(default=Priority.medium, description="任務優先級", example="high/medium/low")
    tags: List[str] = Field(default_factory=list)

# 後端回傳給前端的資料（包含 todo_id）
class TodoOut(TodoCreate):
    id: str = Field(..., description="Todo ID, 格式 memberSeq-todoSeq，例如 1-3")
