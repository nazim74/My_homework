class Vehicle:
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self._model = model
        self._engine_power = engine_power
        self._color = color
        self._COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']


class Sedan(Vehicle):
    def __init__(self, *args, **kwargs):  # принимаем все аргументы при создании объекта класса sedan
        super().__init__(*args, **kwargs)  # передаем все аргументы в родительский класс

    def get_model(self):
        return f"Модель: {self._model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self._engine_power} лошадей"

    def get_color(self):
        return f"Цвет: {self._color}"

    # def print_info(self):
    #     print(self._model, self._engine_power, self._color)
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in self._COLOR_VARIANTS):
            self._color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')  # недопустимый
vehicle1.set_color('BLACK')  # допустимый
vehicle1.owner = 'Vasyok'  # смена владельца

# Проверяем, что поменялось
vehicle1.print_info()
