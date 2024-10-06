import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0  # Изначальный баланс банка
        self.lock = threading.Lock()  # Замок для управления потоками

    def deposit(self):
        for i in range(100):
            # Генерация случайного числа
            amount = random.randint(50, 500)
            # Пополнение баланса
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")

            # Если баланс больше или равен 500 и замок заблокирован, разблокируем его
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            # пауза
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            # Генерация случайного числа для снятия средств
            amount = random.randint(50, 500)
            print(f"Запрос на: {amount}")

            # Проверяем, достаточно ли средств на балансе
            if amount <= self.balance:
                # Снимаем средства
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                # Блокируем поток, если недостаточно средств
                self.lock.acquire()

            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
