from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as f:  # as f автоматически закрывает файл
        for i, string in enumerate(strings, start=1):
            byte_count = len(string)
            position = f.tell()  # получаем позицию курсора
            f.write(string + ' \n')  # добавляем строчку и перенос
            print(f"Строка № {i}: {string}, Количество байтов: {byte_count} Позиция: {position}")
            strings_positions[(i, position)] = string  # создаем кортеж где string каждая следующая строка

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
