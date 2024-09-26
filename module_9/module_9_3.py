first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# вычисление разницы длин строк, если их длины не равны
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# сравнение длин строк на одинаковых позициях без zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))