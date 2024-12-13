from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Список пользователей
users: List['User'] = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# GET запрос: возвращает всех пользователей
@app.get("/users", summary="Get Users")
async def get_users():
    return users

# POST запрос: добавляет нового пользователя
@app.post("/user/{username}/{age}", summary="Post User")
async def add_user(
    username: str = Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser"),
    age: int = Path(ge=18, le=120, description="Enter age", example=24)
):
    new_id = users[-1].id + 1 if users else 1  # Определяем id
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

# PUT запрос: обновляет данные пользователя
@app.put("/user/{user_id}/{username}/{age}", summary="Update User")
async def update_user(
    user_id: int = Path(description="Enter User ID", example=1),
    username: str = Path(min_length=5, max_length=20, description="Enter username", example="UrbanProfi"),
    age: int = Path(ge=18, le=120, description="Enter age", example=28)
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# DELETE запрос: удаляет пользователя
@app.delete("/user/{user_id}", summary="Delete User")
async def delete_user(
    user_id: int = Path(description="Enter User ID", example=2)
):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
