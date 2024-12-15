from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

# Подключаем папку с шаблонами
templates = Jinja2Templates(directory="templates")

# Список пользователей
users: List['User'] = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# GET запрос: отображает список пользователей с помощью шаблона
@app.get("/", response_class=HTMLResponse, summary="Show Users List")
async def get_users_page(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# GET запрос: отображает информацию о пользователе с помощью шаблона
@app.get("/user/{user_id}", response_class=HTMLResponse, summary="Show User Details")
async def get_user(request: Request, user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})

# GET запрос: возвращает всех пользователей в JSON формате
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
# Запуск приложения
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)