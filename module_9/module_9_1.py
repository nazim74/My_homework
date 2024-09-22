def apply_all_func(int_list, *functions):
    # Создаем пустой словарь для хранения результатов
    results = {}

    # Перебираем все переданные функции
    for func in functions:
        # Вызываем функцию с передачей списка int_list и сохраняем результат
        results[func.__name__] = func(int_list)

    # Возвращаем словарь с результатами
    return results

# Примеры вызова функции с различными функциями
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
