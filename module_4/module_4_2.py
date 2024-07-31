def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()

try:
    inner_function()
except Exception as e:
    print(f"inner_function не может быть вызвана из глобального пространства имен: {e}")





# Перехваченная ошибка представляет собой объект класса, унаследованного от "BaseException". С помощью ключевого слова
# as
#  можно записать этот объект в переменную, чтобы обратиться к нему внутри блока
# except

