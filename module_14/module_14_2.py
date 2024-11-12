import sqlite3

# Создаем БД и подключаемся к ней
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Создаем таблицу Users, IF NOT EXISTS если она ещё не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Очищаем таблицу, если там уже есть данные (это для повторного запуска кода)
cursor.execute('DELETE FROM Users')

# Заполняем таблицу 10 записями
users = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]
cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users)

# Обновляем balance у каждой второй записи, начиная с первой на 500
cursor.execute('UPDATE Users SET balance = 500 WHERE id IN (1, 3, 5, 7, 9)')

# Удаляем каждую 3-ю запись, начиная с 1-й
cursor.execute('DELETE FROM Users WHERE id IN (1, 4, 7, 10)') # id=6 удалиться уже тут

# Дополнение кода
# Удаление пользователя с id=6, хотя он уже удален
cursor.execute('DELETE FROM Users WHERE id = 6')

# Подсчет общего количества записей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Подсчет среднего баланса всех пользователей
if total_users > 0:
    print(all_balances / total_users)

# Подсчет среднего баланса всех пользователей при помощи AVG
cursor.execute('SELECT AVG(balance) FROM Users')
average_balance = cursor.fetchone()[0]

print(average_balance)

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
