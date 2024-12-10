from fastapi import FastAPI
from typing import Optional

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

# Маршрут для страниц пользователей по ID
@app.get("/user/{user_id}")
async def user_page(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

# Маршрут для информации о пользователе
@app.get("/user")
async def user_info(username: Optional[str] = "Неизвестно", age: Optional[int] = 0):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}."
