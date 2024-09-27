import os
import time
import tkinter as tk
from tkinter import filedialog, ttk, messagebox


# Функция для выбора директории
def choose_directory():
    directory = filedialog.askdirectory()
    if directory:
        display_files(directory)


# Функция для отображения файлов и папок в Treeview
def display_files(directory):
    # Очистка дерева перед обновлением
    tree.delete(*tree.get_children())

    # Добавление корневой директории в дерево
    root_node = tree.insert("", tk.END, text=directory, values=(directory, "Папка"), open=True)
    walk_directory(directory, root_node)


# Рекурсивная функция для обхода папок и вложений
def walk_directory(directory, parent_node):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            # Добавление папки в дерево
            dir_node = tree.insert(parent_node, tk.END, text=dir_name, values=(dir_path, "Папка"))
            # Рекурсивный вызов для отображения вложенных папок
            walk_directory(dir_path, dir_node)

        for file_name in files:
            file_path = os.path.join(root, file_name)
            filetime = os.path.getmtime(file_path)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(file_path)
            # Добавление файла в дерево
            tree.insert(parent_node, tk.END, text=file_name, values=(file_path, f"{filesize} байт", formatted_time))
        break  # Останавливаем рекурсию, чтобы не углубляться в подкаталоги


# Функция для открытия выбранного файла или папки
def open_selected():
    selected_item = tree.selection()  # Получаем выбранный элемент
    if not selected_item:
        messagebox.showwarning("Предупреждение", "Пожалуйста, выберите файл или папку.")
        return

    # Получаем путь из данных выбранного элемента
    item_path = tree.item(selected_item, 'values')[0]

    # Если это папка, отобразим её содержимое
    if os.path.isdir(item_path):
        display_files(item_path)
    # Если это файл, откроем его
    elif os.path.isfile(item_path):
        open_file(item_path)


# Функция для открытия файла
def open_file(file_path):
    if os.path.exists(file_path):
        try:
            os.startfile(file_path)  # Для Windows
        except AttributeError:
            try:
                # Для macOS и Linux
                if os.name == 'posix':
                    os.system(f"open '{file_path}'")  # macOS
                else:
                    os.system(f"xdg-open '{file_path}'")  # Linux
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")
    else:
        messagebox.showerror("Ошибка", "Файл не существует.")


# Создание главного окна
root = tk.Tk()
root.title("Файловый проводник с навигацией")
root.geometry("800x500")

# Кнопка для выбора директории
button_directory = tk.Button(root, text="Выбрать директорию", command=choose_directory)
button_directory.pack(pady=10)

# Создание таблицы для отображения файлов и папок
tree = ttk.Treeview(root, columns=("path", "size", "modified"), show="headings")
tree.heading("path", text="Путь")
tree.heading("size", text="Размер")
tree.heading("modified", text="Дата изменения")

tree.column("path", width=300)
tree.column("size", width=100)
tree.column("modified", width=150)

tree.pack(fill=tk.BOTH, expand=True)

# Кнопка для открытия файла или папки
button_open = tk.Button(root, text="Открыть", command=open_selected)
button_open.pack(pady=10)

# Запуск главного цикла приложения
root.mainloop()
