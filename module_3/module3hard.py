def calculate_structure_sum(data_structure):
    def summa(data):
        total = 0  # Промежуточная сумма
        if isinstance(data, dict):  # Проверяем, является ли data словарем
            for key, value in data.items():  # Перебираем пары ключ-значение в dict
                if isinstance(key, (int, str)):  # Проверяем, является ли ключ строкой или числом
                    total += len(key) if isinstance(key, str) else key  # Если key строка - добавляем длину строки, если число - его значение
                total += summa(value)  # Вызываем функцию summa и добавляем результат к total
        elif isinstance(data, (list, tuple, set)):  # Проверяем является ли data списком, кортежем, множеством
            for i in data:  # Перебираем все элементы data
                total += summa(i)
        elif isinstance(data, int):  # Проверяем, является ли data числом
            total += data  # Если data - число, добавляем его к total
        elif isinstance(data, str):  # Проверяем, является ли data строкой
            total += len(data)  # Если data - строка, добавляем ее длину к total
        return total  # Возвращаем итоговую сумму

    return summa(data_structure)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
