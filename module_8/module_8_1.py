def add_everything_up(a, b):
    try:
        result = a + b
        if isinstance(result, float):
            return str(round(result, 3))  # выводим только 3 знака после запятой
        return result
    except TypeError:
        return str(a) + str(b)
    # finally:
    #     print("The end")

# Пример кода
print(add_everything_up(123.456, ' строка'))
print(add_everything_up('яблоко ', 4215))
print(add_everything_up(123.456, 7))
