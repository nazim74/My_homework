first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(s) for s in first_strings if len(s) >= 5]

# 2. Список слов одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# 3. Словарь, где ключ — строка, значение — длина, только если длина строки чётная
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)