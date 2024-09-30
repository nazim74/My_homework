first = 'Мама мыла раму'
second = 'Рамена мало было'

# Сравнение букв на одинаковых позициях
result = list(map(lambda x, y: x == y, first, second))
print(result)


# Запись данных в файл
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as example_file:
            for data in data_set:
                example_file.write(str(data) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
write('строка', [1, 2, 3], {'ключ': 'значение'})

# Случайный выбора слова
from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Не знаю')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
