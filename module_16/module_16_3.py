from fastapi import FastAPI, Path
from typing import Annotated
# from starlette.middleware.base import BaseHTTPMiddleware
# from starlette.responses import JSONResponse

# Создание приложения FastAPI
app = FastAPI()

# Middleware для добавления заголовка Content-Type с UTF-8
# class UTF8Middleware(BaseHTTPMiddleware):
#     async def dispatch(self, request, call_next):
#         response = await call_next(request)
#         if isinstance(response, JSONResponse):
#             response.headers["Content-Type"] = "application/json; charset=utf-8"
#         return response
#
# app.add_middleware(UTF8Middleware)

# Имитация базы данных
users = {"1": "Имя: Example, возраст: 18"}

# GET запрос: возвращает всех пользователей
@app.get("/users", summary="Get Users")
async def get_users():
    return users

# POST запрос: добавляет нового пользователя
@app.post("/user/{username}/{age}", summary="Post User")
async def add_user(
    username: Annotated[
        str,
        Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")
    ],
    age: Annotated[
        int,
        Path(ge=18, le=120, description="Enter age", example=24)
    ]
):
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

# PUT запрос: обновляет данные пользователя
@app.put("/user/{user_id}/{username}/{age}", summary="Update User")
async def update_user(
    user_id: Annotated[
        str,
        Path(description="Enter User ID", example="1")
    ],
    username: Annotated[
        str,
        Path(min_length=5, max_length=20, description="Enter username", example="UrbanProfi")
    ],
    age: Annotated[
        int,
        Path(ge=18, le=120, description="Enter age", example=28)
    ]
):
    if user_id not in users:
        return f"User {user_id} not found"
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"

# DELETE запрос: удаляет пользователя
@app.delete("/user/{user_id}", summary="Delete User")
async def delete_user(
    user_id: Annotated[
        str,
        Path(description="Enter User ID", example="2")
    ]
):
    if user_id not in users:
        return f"User {user_id} not found"
    del users[user_id]
    return f"User {user_id} has been deleted"
