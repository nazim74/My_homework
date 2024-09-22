def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            # Проверка, является ли элемент числом
            if isinstance(item, (int, float)):
                result += item
            else:
                raise TypeError
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Проверка, является ли numbers строкой
        if isinstance(numbers, str):
            # Перебираем каждый символ строки, чтобы обработать некорректные данные
            personal_sum(list(numbers))  # передаём строку как список символов
            return 0  # Так как строка не содержит чисел, результат 0

        # Проверка, является ли numbers списком или кортежем
        if not isinstance(numbers, (list, tuple)):
            raise TypeError

        # Вызов функции personal_sum для подсчёта суммы и некорректных данных
        total_sum, incorrect_data = personal_sum(numbers)

        # Если количество корректных данных равно нулю, возвращаем 0
        if len(numbers) - incorrect_data == 0:
            return 0

        # Вычисляем среднее арифметическое
        average = total_sum / (len(numbers) - incorrect_data)
        return average

    except ZeroDivisionError: # Обрабатываем ошибку деления на ноль
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка с символами
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
