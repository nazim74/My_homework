class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

    def __eq__(self, other): # для равенства == вызываем его когда используем оператор ==
        if isinstance(other, House): # проверка объекта на то, что после запятой, если да то вернет True
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        return False

    def __lt__(self, other):  # для оператора меньше < вызываем также как __eq__
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        return False

    def __le__(self, other): # <=
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        return False

    def __gt__(self, other): # >
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        return False

    def __ge__(self, other): # >=
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        return False

    def __ne__(self, other): # !=
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
        return True

    def __add__(self, value): # +
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value): # складываем то что слева от знака +
        return self.__add__(value)

    def __iadd__(self, value): # +=
        return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2, '                       #этажи не равны')  # False  def __eq__

h1 = h1 + 10  # def __add__ добавляем этажи
print(h1)
print(f"{h1 == h2}                      #теперь этажи равны") # True def __eq__

h1 += 10  # def __iadd__ добавляем этажи
print(h1)

h2 = 10 + h2  # def __radd__ добавляем этажи
print(h2)

print(h1 > h2)  # False def __gt__
print(h1 >= h2)  # True def __ge__
print(h1 < h2)  # False def __lt__
print(h1 <= h2)  # True def __le__
print(h1 != h2)  # False def __ne__

# https://habr.com/ru/articles/186608/
