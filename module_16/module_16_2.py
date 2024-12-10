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

# Маршрут для страниц пользователей по ID с валидацией user_id
@app.get("/user/{user_id}")
async def user_page(
    user_id: Annotated[
        int,
        Path(
            title="Enter User ID",
            description="ID пользователя, который должен быть целым числом от 1 до 100",
            ge=1,
            le=100,
            example=1,
        ),
    ]
):
    return f"Вы вошли как пользователь № {user_id}"

# Маршрут для информации о пользователе с валидацией username и age
@app.get("/user/{username}/{age}")
async def user_info(
    username: Annotated[
        str,
        Path(
            title="Enter username",
            description="Имя пользователя должно быть строкой длиной от 5 до 20 символов",
            min_length=5,
            max_length=20,
            example="UrbanUser",
        ),
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            description="Возраст пользователя должен быть числом от 18 до 120",
            ge=18,
            le=120,
            example=24,
        ),
    ],
):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}."
