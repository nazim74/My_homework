import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.total_enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.total_enemies > 0:  # Пока есть враги
            time.sleep(1)
            self.days += 1  # Увеличиваем дни

            # Уменьшаем количество врагов на силу рыцаря
            self.total_enemies -= self.power
            if self.total_enemies < 0:
                self.total_enemies = 0  # врагов не может быть меньше 0

            # Вывод хода сражения с правильным склонением
            if self.days == 1:
                day_word = "день"
            elif 2 <= self.days <= 4:
                day_word = "дня"
            else:
                day_word = "дней"
            print(f"{self.name}, сражается {self.days} {day_word}..., осталось {self.total_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней!")

first_knight = Knight('Sir Lancelot', 10)  # Первый рыцарь
second_knight = Knight('Sir Galahad', 20)  # Второй рыцарь

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
