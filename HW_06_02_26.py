# Iterator and Generator

'''
1.	Создайте класс RangeIterator, который реализует протокол итератора (__iter__, __next__).
Итератор должен возвращать числа в заданном диапазоне с указанным шагом. После окончания итерации
должно выбрасываться исключение StopIteration.
'''
from symtable import Class
from typing import Iterator

# class RangeIterator:
#
#     def __init__(self, start=0, stop=None, step=1):
#         self.start = start
#         self.stop = stop
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += self.step
#         if self.start < self.stop:
#             return self.start
#         else:
#             raise StopIteration
#
# iterator_my1 = RangeIterator(start=3, stop=99, step=5)
#
# for i in iterator_my1:
#     print(i)

'''
2.	Напишите генераторную функцию fibonacci(limit),
которая возвращает последовательность Фибоначчи до заданного предела. Генерация должна останавливаться, когда значение превышает limit.
'''

# def fibonacci(limit: int) -> None:
#     a, b = 0, 1
#     print(a)
#     while b < limit:
#         print(b)
#         a, b = b, a+b
#
# fibonacci(1000)

'''
3.	Создайте класс LogReader, который читает строки из источника данных и является итерируемым объектом.
Класс должен:
-	поддерживать перебор через for
-	пропускать пустые строки
-	возвращать строки по одной без загрузки всех данных в память
'''

# class LogReader:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if not self.lst:
#             raise StopIteration
#         else:
#             if not self.lst[0]:
#                 del self.lst[0]
#                 return None
#             else:
#                 return self.lst.pop(0)
#
# fl = LogReader(['Привет', '' , 'друг', 'Как дела?'])
#
# for i in fl:
#     if i:
#         print(i)

'''
4.	Напишите генераторную функцию flatten(iterable),
которая принимает вложенную структуру (списки внутри списков) и возвращает элементы в плоском виде.
Решение должно корректно обрабатывать любую глубину вложенности.
Simple input:
[1, [2, 3], [[4], 5], 6]
Simple Output:
1 → 2 → 3 → 4 → 5 → 6
'''

# def flatten(lst: list) -> None:
#     for item in lst:
#         if type(item) != list:
#             print(item , end=' ')
#         else:
#             flatten(item)
#
# flatten([1, [2, 3], [[4], 5], 6])

# Classes

from abc import ABC, abstractmethod

'''
1.	Создайте абстрактный класс PaymentMethod. Объявить абстрактный метод pay(amount).
Реализовать минимум 3 класса-наследника с разной логикой оплаты.
Обеспечить возможность работать с объектами через общий интерфейс.
Проверить полиморфное поведение при вызове pay
'''

# class PaymentMethod(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
#
# class Cash(PaymentMethod):
#     def pay(self, amount):
#         amount = amount
#         print(f"Оплата наличными - {amount}")
#
# class CreditCard(PaymentMethod):
#     def pay(self, amount):
#         amount = amount // 3
#         print(f"Оплата кредитной картой - {amount} ")
#
# class Card(PaymentMethod):
#     def pay(self, amount):
#         amount = amount // 2
#         print(f"Оплата дебетовой картой - {amount} ")
#
# def type_pay(tp, amount):
#     tp.pay(amount)
#
# cash = Cash()
# ccrd = CreditCard()
# crd = Card()
#
# cash.pay(300)
# ccrd.pay(300)
# crd.pay(300)
#
# Ivan = Cash()
# Peter = Card()
#
# type_pay(Ivan, 33)
# type_pay(Peter, 100)

'''
2.	Создайте абстрактный класс Notification. Объявите абстрактный метод send(message). 
Реализуйте минимум 3 класса-наследника, каждый из которых отправляет сообщение по-разному.
'''

# class Notification(ABC):
#     @abstractmethod
#     def send(self, message: str) -> None:
#         pass
#
# class Post(Notification):
#     def send(self, message: str) -> None:
#         message = message.lower()
#         print(f'Положили Ваше сообщение -  {message} - в конверт и отправили почтой!')
#
# class Telegram(Notification):
#     def send(self, message: str) -> None:
#         message = message.upper()
#         print(f'Ваше сообщение - {message} - отправлено телеграммой!')
# class ICQ(Notification):
#     def send(self, message: str) -> None:
#         message = message.replace(' ', ':)')
#         print(f'Ваше сообщение - {message} - отправлено по ICQ')
#
# def mes(tp, message):
#     tp.send(message)
#
# mes(Post(), "Всем привет! Сегодня воскресенье! Учиться, учиться, учиться!")
#
# mes(Telegram(), "Всем привет! Сегодня воскресенье! Учиться, учиться, учиться!")
#
# mes(ICQ(), "Всем привет! Сегодня воскресенье! Учиться, учиться, учиться!")

'''
3.	Создайте класс User с ролью. Реализуйте policy-класс, определяющий доступ к методам. 
Создайте декоратор, который проверяет право пользователя на выполнение метода. 
Продемонстрируйте разрешённый и запрещённый доступ без if внутри метода.
'''

# class Policy:
#     def notify(func):
#         def wrapper(self, role):
#             if role == 'admin':
#                 return func(self, role)
#             else:
#                 print(f"{self.name} - Доступ запрещен!")
#
#         return wrapper
#
# class User():
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
#     def get_role(self):
#         return self.role
#
#     def __str__(self):
#         return f'Имя - {self.name}, роль - {self.role}'
#
#     @Policy.notify
#     def acs_admin(self, role):
#         print(f'Доступ разрешен - {self.name}!')
#
#
# user1 = User(name='Ivan', role='admin')
# get_us1 = user1.get_role()
# print(user1)
#
# user2 = User(name='John', role='user')
# get_us2 = user2.get_role()
# print(user2)
#
# user1.acs_admin(get_us1)
# user2.acs_admin(get_us2)

'''
4.	Создай класс BankAccount, который имеет закрытый баланс __balance. 
Позволяет пополнять deposit и снимать withdraw деньги. Не позволяет снимать больше, чем есть на счету. 
Вводит суточный лимит снятия (например, 5000). Сделайте ограничение по транзакциям, не более 3 – х
'''

# class BankAccount:
#     def __init__(self, balance: float = 0):
#         self.__balance = balance
#         self.daily_limit = 5000
#         self.withdrawals_today = 0
#         self.max_withdrawals = 3
#
#     def deposit(self, amount: float):
#         if self.max_withdrawals > 0:
#             __balance = self.__balance + amount
#             self.max_withdrawals -= 1
#             return f"Успешно внесено - {amount}, баланс равен {__balance}"
#         else:
#             return f'Количество операций в день превышено!'
#
#     def withdraw(self, amount: float):
#         if self.max_withdrawals > 0:
#             if self.withdrawals_today + amount <= self.daily_limit and self.max_withdrawals > 0:
#                 self.daily_limit -= amount
#                 self.withdrawals_today += amount
#                 self.max_withdrawals -= 1
#                 return f'Успешно снято - {amount}, лимит {self.daily_limit}'
#             else:
#                 return f"Невозможно снять запрошенную сумму, остаток по лимиту на день - {self.daily_limit}"
#         else:
#             return f'Количество операций в день превышено!'
#
#     def get_balance(self):
#         return self.__balance
#
# ba = BankAccount(10000)
# # Баланс
# print(ba.get_balance())
# # Внесение
# print(ba.deposit(5000))
# # Снятие
# print(ba.withdraw(15000))
# print(ba.withdraw(1500))
# print(ba.withdraw(500))
# print(ba.withdraw(200))



