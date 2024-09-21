def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        if isinstance(item, (int, float)):  # Проверяем, является ли элемент числом
            result += item
        else:
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple)):
            raise TypeError

        total_sum, incorrect_data = personal_sum(numbers)

        # Если корректных данных нет, возвращаем 0
        if len(numbers) - incorrect_data == 0:
            return 0

        average = total_sum / (len(numbers) - incorrect_data)
        return average

    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Примеры вызовов функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
