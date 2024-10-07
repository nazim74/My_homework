import time
import random
from queue import Queue
from threading import Thread

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # ожидание рандомное
        time_to_eat = random.randint(3, 10)
        time.sleep(time_to_eat) # остановка потока на рандомное время

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue() # создаем очередь

    def guest_arrival(self, *guests):
        for guest in guests:
            seated = False
            for table in self.tables:
                if table.guest is None:  # Если стол свободен
                    table.guest = guest # посадили за стол
                    guest.start()  # Запускаем поток гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    seated = True
                    break
            if not seated:  # Если все столы заняты
                self.queue.put(guest) # ставим гостя в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        """ Пока в очереди есть гости или заняты столы """
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables: # проверяем каждый стол
                if table.guest is not None and not table.guest.is_alive(): # поток завершен, но гость за столом
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                    if not self.queue.empty():  # Если очередь не пуста
                        next_guest = self.queue.get() # берем следующего гостя
                        table.guest = next_guest # сажаем за стол
                        next_guest.start() # запускаем новый поток
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            time.sleep(1)

        print("Все гости обслужены, кафе закрыто.")

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
