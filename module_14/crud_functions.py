import sqlite3

# Функция для инициализации базы данных
def initiate_db():
    # Подключение к базе данных (или создание, если она не существует)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Создание таблицы Products, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    # Создание таблицы Users, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    ''')

    conn.commit()  # Сохраняем изменения
    conn.close()  # Закрываем соединение с базой данных

# Функция для получения всех продуктов из таблицы Products
def get_all_products():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')  # Получаем все записи из Products
    products = cursor.fetchall()  # Сохраняем все записи в переменной products
    conn.close()  # Закрываем соединение с базой данных
    return products

# Функция для добавления нового пользователя в таблицу Users
def add_user(username, email, age):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Добавляем запись с переданными данными и балансом 1000
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance) 
        VALUES (?, ?, ?, 1000)
    ''', (username, email, age))
    conn.commit()  # Сохраняем изменения
    conn.close()  # Закрываем соединение с базой данных

# Функция для проверки наличия пользователя в таблице Users
# def is_included(username):
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     # Проверяем, есть ли пользователь с указанным именем
#     cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
#     result = cursor.fetchone()  # Получаем первую запись, если она есть
#     conn.close()  # Закрываем соединение с базой данных
#     return result is not None  # Возвращаем True, если запись найдена, иначе False

# Функция для проверки наличия пользователя в таблице Users
def is_included(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Приводим имя пользователя к нижнему регистру перед проверкой
    cursor.execute('SELECT * FROM Users WHERE LOWER(username) = ?', (username.lower(),))
    result = cursor.fetchone()
    conn.close()
    return result is not None


# Заполнение таблицы продуктами (только при первом запуске)
def add_sample_products():
    conn = sqlite3.connect('database.db')  # Исправлено на database.db
    cursor = conn.cursor()

    # Проверка, пустая ли таблица Products
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:  # Если таблица пустая, добавляем примеры
        products = [
            ("Product 1", "Пластинка 1", 100),
            ("Product 2", "Пластинка 2", 200),
            ("Product 3", "Пластинка 3", 300),
            ("Product 4", "Пластинка 4", 400)
        ]
        cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)
        conn.commit()

    conn.close()

# Инициализация базы данных и добавление данных
if __name__ == "__main__":
    initiate_db()
    add_sample_products()  # Добавляет продукты только при первом запуске
