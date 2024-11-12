import sqlite3


# Функция для инициализации базы данных
def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Создание таблицы Products, если она еще не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


# Функция для получения всех продуктов
def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Получаем все записи из таблицы Products
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products


# Заполнение таблицы продуктами (только при первом запуске) потом закомментировать
def add_sample_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Примерные записи для заполнения таблицы
    products = [
        ("Product 1", "Пластинка 1", 100),
        ("Product 2", "Пластинка 2", 200),
        ("Product 3", "Пластинка 3", 300),
        ("Product 4", "Пластинка 4", 400)
    ]

    # Вставка записей
    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)
    conn.commit()
    conn.close()


# Инициализация базы данных и добавление данных
if __name__ == "__main__":
    initiate_db()
    add_sample_products()
