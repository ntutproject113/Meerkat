# member.py
from fastapi import APIRouter, HTTPException, Response, Depends
from db import members_collection, profiles_collection, counters_collection
from model import UserCreate, UserLogin, UserOut, ProfileCreate, ProfileOut
from auth import hash_password, verify_password, create_access_token, get_current_user
from datetime import datetime

router = APIRouter(prefix="/members", tags=["Members"])

# 註冊會員
@router.post("/register", response_model=UserOut)
def register(user: UserCreate):
    if members_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="使用者名稱已存在")
    if members_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email 已被使用")

    hashed_pw = hash_password(user.password)

    # 生成 member_seq（全局序號）
    seq_doc = counters_collection.find_one_and_update(
        {"_id": "member_seq"}, 
        {"$inc": {"seq": 1}}, 
        upsert=True, 
        return_document=True
    )
    member_seq = seq_doc["seq"]

    result = members_collection.insert_one({
        "username": user.username,
        "email": user.email,
        "password": hashed_pw,
        "member_seq": member_seq,   # 新增 member_seq
        "created_at": datetime.utcnow()
    })

    profiles_collection.insert_one({
        "member_id": str(result.inserted_id),
        "name": "",
        "gender": "",
        "phone": "",
        "school": "",
        "department": "",
        "grade": "",
        "interests": [],
        "skills": [],
        "plan_after_graduation": "升學"
    })

    return {"username": user.username, "email": user.email, "member_seq": member_seq}  # 回傳 member_seq

# 登入會員
@router.post("/login")
def login(user: UserLogin, response: Response):
    db_user = members_collection.find_one({"username": user.username})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="帳號或密碼錯誤")

    token = create_access_token({"username": user.username})
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="lax",
        max_age=60*60*24
    )
    return {"message": "登入成功"}

# 取得會員帳號資訊
@router.get("/me", response_model=dict)
def get_me(user: dict = Depends(get_current_user)):
    profile = profiles_collection.find_one({"member_id": str(user["_id"])})

    if not profile:
        raise HTTPException(status_code=404, detail="Profile 不存在")

    profile_out = ProfileOut(**profile)
    user_out = UserOut(
        username=user.get("username"),
        email=user.get("email")
    )

    return {"user": user_out, "profile": profile_out}

# 更新會員詳細資料
@router.post("/profile", response_model=ProfileOut)
def update_profile(profile: ProfileCreate, user: dict = Depends(get_current_user)):
    profiles_collection.update_one(
        {"member_id": str(user["_id"])},
        {"$set": profile.dict(exclude_none=True)}
    )
    updated = profiles_collection.find_one({"member_id": str(user["_id"])})
    return ProfileOut(**updated)
