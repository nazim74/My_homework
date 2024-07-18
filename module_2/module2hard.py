def find_password(n):
    password = []
    for i in range(1, n):  # создаем цикл для подбора первого числа от 1 до 20
        if n >= 21 or n <= 2:  # проверяем что введены числа в заданном диапазоне
            print('Число не в заданном диапазоне ')
            break
        for j in range(i + 1, n):  # создаем цикл для подбора второго числа с шагом 1
            if n % (i + j) == 0:  # проверяем кратность суммы чисел (i + j) n
                password.append(f" {i}+{j}")  # добавляем числа в список
    valid_password = ''.join(password)  # объединяем пары в строку
    return valid_password


n = int(input("Введите число от 3 до 20: "))
valid_password = find_password(n)
print(valid_password)
