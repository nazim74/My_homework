def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

# Можно оборачивать несколько функций
@is_prime
def multiply_three(a, b, c):
    return a * b * c


# Пример использования
result = sum_three(2, 3, 6)
print(result)
result = sum_three(2, 3, 7)
print(result)
result = multiply_three(7, 3.4, 8)
print(result)