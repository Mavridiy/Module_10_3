import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0  # Изначальный баланс банка
        self.lock = threading.Lock()  # Создаем объект Lock для блокировки потоков

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)  # Случайная сумма для пополнения
            with self.lock:  # Блокируем доступ к балансу
                self.balance += amount
                print(f'Пополнение: {amount}. Баланс: {self.balance}')
                if self.balance >= 500 and not self.lock.locked():
                    self.lock.release()  # Разблокируем, если баланс >= 500
            time.sleep(0.001)  # Имитация задержки

    def take(self):
        for i in range(100):
            amount = random.randint(50, 500)  # Случайная сумма для снятия
            print(f'Запрос на:  {amount}')
            with self.lock:  # Блокируем доступ к балансу
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Снятие: {amount}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')

            time.sleep(0.001)  # Имитация задержки





bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')