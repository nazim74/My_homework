from fastapi import FastAPI, Path
from typing import Annotated

# Создание приложения FastAPI
app = FastAPI()

# Маршрут главной страницы
@app.get("/")
async def main_page():
    return "Главная страница"

# Маршрут страницы администратора
@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

# Маршрут для страниц пользователей по ID с валидацией
@app.get("/user/{user_id}")
async def user_page(
    user_id: Annotated[
        int,
        Path(ge=1, le=100, description="Enter User ID", example=1)
    ]
):
    return f"Вы вошли как пользователь № {user_id}"

# Маршрут для информации о пользователе с валидацией
@app.get("/user/{username}/{age}")
async def user_info(
    username: Annotated[
        str,
        Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")
    ],
    age: Annotated[
        int,
        Path(ge=18, le=120, description="Enter age", example=24)
    ]
):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}."

