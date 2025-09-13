from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from datetime import date, datetime
from db import todo_collection, counters_collection
from model import Priority, TodoCreate, TodoOut
from auth import get_current_user

router = APIRouter(prefix="/todos", tags=["Todos"])

# Helper: MongoDB doc -> Pydantic
def todo_from_mongo(doc) -> TodoOut:
    return TodoOut(
        id=doc["todo_id"],  # 使用自訂 todo_id
        name=doc["name"],
        completed=doc.get("completed", False),
        todo_date=doc.get("todo_date").date() if doc.get("todo_date") else None,
        priority=Priority(doc.get("priority", "medium")),
        tags=doc.get("tags", [])
    )

# 創建 Todo
@router.post("", response_model=TodoOut)
def create_todo(todo: TodoCreate, user: dict = Depends(get_current_user)):
    data = todo.dict(exclude_none=True)
    data["member_id"] = str(user["_id"])
    member_seq = user.get("member_seq")  # 確保拿到 member_seq
    if member_seq is None:
        raise HTTPException(status_code=400, detail="會員序號不存在，請先確認會員資料")

    if "todo_date" in data and isinstance(data["todo_date"], date):
        data["todo_date"] = datetime.combine(data["todo_date"], datetime.min.time())

    # 生成 todo 序號（每個會員獨立）
    seq_doc = counters_collection.find_one_and_update(
        {"_id": f"todo_seq_{member_seq}"},
        {"$inc": {"seq": 1}},
        upsert=True,
        return_document=True
    )
    todo_seq = seq_doc["seq"]

    # todo_id = member序號 + todo序號
    data["todo_id"] = f"{member_seq}-{todo_seq}"

    result = todo_collection.insert_one(data)
    doc = todo_collection.find_one({"_id": result.inserted_id})
    return todo_from_mongo(doc)

# 查詢 Todo
@router.get("", response_model=List[TodoOut])
def list_todos(
    user: dict = Depends(get_current_user),
    todo_date: Optional[date] = None,
    tags: Optional[List[str]] = Query(None),
    priority: Optional[Priority] = None,
    completed: Optional[bool] = None,
):
    query = {"member_id": str(user["_id"])}
    
    if todo_date:
        query["todo_date"] = datetime.combine(todo_date, datetime.min.time())
    if tags:
        query["tags"] = {"$all": tags}
    if priority:
        query["priority"] = priority.value
    if completed is not None:
        query["completed"] = completed

    todos = todo_collection.find(query)
    return [todo_from_mongo(t) for t in todos]

# 更新 Todo
@router.put("/{todo_id}", response_model=TodoOut)
def update_todo(todo_id: str, todo: TodoCreate, user: dict = Depends(get_current_user)):
    data = todo.dict(exclude_none=True)
    if "todo_date" in data and isinstance(data["todo_date"], date):
        data["todo_date"] = datetime.combine(data["todo_date"], datetime.min.time())
    
    result = todo_collection.update_one(
        {"todo_id": todo_id, "member_id": str(user["_id"])},
        {"$set": data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    doc = todo_collection.find_one({"todo_id": todo_id, "member_id": str(user["_id"])})

    return todo_from_mongo(doc)

# 刪除 Todo
@router.delete("/{todo_id}")
def delete_todo(todo_id: str, user: dict = Depends(get_current_user)):
    result = todo_collection.delete_one({"todo_id": todo_id, "member_id": str(user["_id"])})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}
