def all_variants(text):
    length = len(text)

    for _ in range(length):
        for __ in range(_ + 1, length + 1):
            yield text[_:__]


# Пример работы функции
a = all_variants("abc")
for i in a:
    print(i)
