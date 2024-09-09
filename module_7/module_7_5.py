import os
import time

# Путь к директории, которую нужно обойти
directory = "."

# Обход директории с помощью os.walk
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формирование полного пути к файлу
        filepath = os.path.join(root, file)

        # Получение времени последнего изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получение размера файла
        filesize = os.path.getsize(filepath)

        # Получение родительской директории
        parent_dir = os.path.dirname(filepath)

        # Вывод информации о файле
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
