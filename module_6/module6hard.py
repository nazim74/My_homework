import math


class Figure:
    sides_count = 0

    def __init__(self, __color, *sides):
        if not self.__is_valid_color(*__color):
            __color = (255, 255, 255)  # Начальный цвет - белый
        self.__color = list(__color)
        self.filled = True

        if not self.__is_valid_sides(*sides):
            sides = [1] * self.sides_count
        self.__sides = list(sides)

    def get_color(self):
        return self.__color

    #
    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(x, int) and x > 0 for x in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.cal_radius()

    def cal_radius(self):
        circumference = self.get_sides()[0]
        radius = circumference / (2 * math.pi)
        return round(radius, 2)

    def get_square(self):
        area = math.pi * self.__radius ** 2
        return round(area, 2)


c_1 = Circle([2, 2, 2], 15)
print(f"Площадь круга = {c_1.get_square()}")
print(f"Радиус круга = {c_1.cal_radius()}")


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        S_tr = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return round(S_tr, 2)


t_1 = Triangle([111, 111, 111], 3, 5, 3)
print(f"Площадь треугольника = {t_1.get_square()}")


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1] * 12
        else:
            sides = [sides[0]] * 12  # Преобразуем в 12 одинаковых сторон
        super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


cube_1 = Cube((222, 222, 222), 22)
print(cube_1.get_volume())

# Код для проверки:

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
