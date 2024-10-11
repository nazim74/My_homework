import random
import pandas as pd  # работа с таблицами данных
import numpy as np  # работа с массивами и числовыми вычислениями
import matplotlib.pyplot as plt  # визуализация данных с помощью графиков

# Создаем файл с расширением CSV
num_rows = 100  # Общее количество строк
num_high_rating = int(num_rows * 0.2)  # 20% от общего количества строк для высоких рейтингов

# Генерируем возраст от 18 до 65 для 80% записей
ages = [random.randint(18, 65) for _ in range(num_rows - num_high_rating)]
# Генерируем зарплату в зависимости от возраста: базовая зарплата (возраст * 1000) + случайное значение от 15,000 до 70,000
salaries = [age * 1000 + random.randint(15_000, 70_000) for age in ages]
# Генерируем рейтинг: основан на возрасте (возраст / 6) + случайное значение от 0 до 2
ratings = [round(age / 6 + random.uniform(0, 2), 2) for age in ages]

# Генерация 20% записей с высоким рейтингом, но низким возрастом
for _ in range(num_high_rating):
    age = random.randint(18, 25)  # Генерируем низкий возраст от 18 до 25
    salary = random.randint(20000, 30000)  # Генерируем низкую зарплату от 20,000 до 30,000
    rating = round(random.uniform(8, 10))  # Генерируем высокий рейтинг от 8 до 10
    ages.append(age)  # Добавляем возраст в список
    salaries.append(salary)  # Добавляем зарплату в список
    ratings.append(rating)  # Добавляем рейтинг в список

ids = range(1, num_rows + 1)  # Генерируем последовательные ID от 1 до num_rows

# Создание DataFrame из данных
df = pd.DataFrame({
    'ID': ids,
    'Age': ages,
    'Salary': salaries,
    'Rating': ratings
})

# Запись данных в файл CSV
df.to_csv('data.csv', index=False)  # Сохраняем DataFrame в CSV-файл без индекса

print("Файл data.csv успешно создан!")

# Чтение CSV файла
df = pd.read_csv('data.csv')

print("Первые 5 строк данных:")
print(df.head())  # Вывод первых 5 строк данных

# Описание данных (статистика)
print("\nОписание данных:")
print(df.describe())  # Вывод статистического описания данных

# Подсчет затрат на зарплату до повышения
total_salary_before = df['Salary'].sum()
print("\nЗатраты на зарплату в месяц до повышения:", total_salary_before)

# Фильтр для повышения зарплаты
# Увеличиваем зарплату на 10% тем, у кого зарплата ниже 50000 а рейтинг выше 7
df['Salary'] = df.apply(lambda row: row['Salary'] * 1.1 if row['Salary'] < 50000 and row['Rating'] > 7 else row['Salary'], axis=1)

# Подсчет затрат на зарплату после повышения
total_salary_after = df['Salary'].sum()
print("Затраты на зарплату в месяц после повышения:", total_salary_after)

# Расчет увеличения общих затрат на зарплату
increase_in_salary = total_salary_after - total_salary_before
print(f"Общее увеличение затрат на зарплату после повышения: {increase_in_salary}:.2f")

# Расчеты с использованием NumPy
salaries_np = np.array(df['Salary'])  # Преобразуем столбец зарплаты в массив NumPy

print("\nСтатистика по зарплате:")
print(f"Средняя зарплата: {np.mean(salaries_np):.2f}")  # Вывод средней зарплаты
print(f"Стандартное отклонение зарплаты: {np.std(salaries_np):.2f}")  # Вывод стандартного отклонения зарплаты

# # Вывод данных для повышения зарплаты
# print("\nДанные после повышения зарплаты:")
# print(df[df['Salary'] > 50000])  # Показываем только тех, кто получил повышение

# Использование matplotlib для визуализации данных
# Построение графиков
plt.figure(figsize=(10, 6))  # размера окна

# Линейный график зависимости возраста и рейтинга
plt.subplot(2, 1, 1)  # Разделение окна на 2 строки, 1 колонка, выбираем первую
plt.plot(sorted(ages), sorted(ratings), marker='o')  # Сортируем данные по возрасту и рейтингу и строим линейный график
plt.title("Линейный график зависимости возраста и рейтинга")  # Заголовок
plt.xlabel("Возраст")  # Подпись для оси X
plt.ylabel("Рейтинг")  # Подпись для оси Y

# Построение точечного графика
plt.subplot(2, 1, 2)
plt.scatter(df['Salary'], df['Rating'], color='blue', alpha=0.7)  # Строим график зависимости зарплаты и рейтинга
plt.title("Зависимость рейтинга от зарплаты")
plt.xlabel("Зарплата")
plt.ylabel("Рейтинг")

# Поиск человека с самой высокой зарплатой
highest_salary = df.loc[df['Salary'].idxmax()]

# Поиск человека с самым высоким возрастом
highest_age = df.loc[df['Age'].idxmax()]

print("Человек с самой высокой зарплатой:")
print(highest_salary)

print("\nЧеловек с самым высоким возрастом:")
print(highest_age)

# Вывод графиков
plt.tight_layout()  # Автоматическое выравнивание графиков
plt.show()  # Показать все графики
