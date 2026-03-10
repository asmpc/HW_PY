'''
1.	Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию
изменения этих переменных. Добавить функцию, которая находит сумму значений этих переменных,
и функцию, которая находит наибольшее значение из этих двух переменных.
'''
from unicodedata import digit

# class TwoValues(object):
#     def __init__(self, a, b):
#         self.a = self.b = 0
#         if type(a) in (int, float) or type(b) in (int, float):
#             self.a, self.b = a, b
#
#     def get_value(self):
#         return self.a, self.b
#
#     def set_value(self, a, b):
#         if type(a) in (int, float):
#             self.a = a
#         else:
#             print(f'Недопустимое значение переменной - a!')
#         if type(b) in (int, float):
#             self.b = b
#         else:
#             print(f'Недопустимое значение переменной - b!')
#
#     def sum_value(self):
#         # print(f'Сумма переменных {self.a} и {self.b} равна {self.a + self.b}')
#         # Можно выводить в print
#         return self.a + self.b
#
#     def max_value(self):
#         return max(self.a, self.b)

# vals1 = TwoValues(a = 11, b = 22)    # инициализируем экземпляр класса
# print(vals1.a)    # выводит значение переменной a
# print(vals1.b)    # выводит значение переменной b
# print(vals1.get_value())   # выводит значение переменных
# print(vals1.__dict__)    # выводит поименованное значение переменных объекта vals
# print(TwoValues.__dict__)    # выводит все атрибуты класса

# print(vals1.sum_value())    # выводит в консоль сумму переменных
# print(vals1.max_value())   # выводит в консоль max переменную из двух
# vals1.set_value("asb", 16)    # вызов функции для задания новых значений переменных
# print(vals1.get_value())

'''
2.	Описать класс, реализующий десятичный счетчик, который может увеличивать или 
уменьшать свое значение на единицу в заданном диапазоне. Предусмотреть инициализацию счетчика 
значениями по умолчанию и произвольными значениями. Счетчик имеет два метода: увеличения и уменьшения,
 — и свойство, позволяющее получить его текущее состояние. 
 Написать программу, демонстрирующую все возможности класса.
'''

# class Counter(object):
#
#     DEFAULT_COUNT = 0
#     MAXCOUNT = 1000
#     MINCOUNT = 0
#
#     @classmethod
#     def validate_x(cls, x):
#         if type(x) == int:
#             if cls.MINCOUNT <= x <= cls.MAXCOUNT:
#                 return x
#         else:
#             print('Ошибочное значение счетчика, пределы ограничены - 0<=x<=1000')
#             return cls.DEFAULT_COUNT
#
#
#     def __init__(self, x = DEFAULT_COUNT):
#        if self.validate_x(x):
#             self.x = x
#        else:
#            self.x = Counter.DEFAULT_COUNT
#
#     def get_count(self):
#         return self.x
#
#     def up_count(self):
#         if self.x < self.MAXCOUNT:
#             self.x += 1
#             return self.x
#         else:
#             print("Ошибка счетчика - значение = max(1000)")
#
#     def down_count(self):
#         if self.x > self.MINCOUNT:
#             self.x -= 1
#             return self.x
#         else:
#             print("Ошибка счетчика - значение = min(0)")
#
#     def set_count(self, x):
#         self.x = x
#         return self.x

# cnt1 = Counter(30)
# cnt2 = Counter('a')
# cnt3 = Counter()
# cnt4 =  Counter(999)
# cnt5 = Counter(3)
# print(cnt1.get_count())
# print(cnt2.get_count())
# print(cnt3.get_count())
# print(cnt4.get_count())
# cnt1.up_count()
# print(cnt1.get_count()
# cnt2.up_count()
# cnt1.down_count()
# cnt1.down_count()
# cnt2.down_count()
# cnt2.down_count()
# cnt1.set_count(255)
# print(cnt1.get_count())
# cnt4.up_count()
# cnt4.up_count()
# cnt5.down_count()
# cnt5.down_count()
# cnt5.down_count()
# print(cnt5.get_count())
# cnt5.down_count()
# cnt5.down_count()

'''
3.	Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов, 
поиска продуктов по названию, добавления их в магазин и удаления продуктов из него.
'''

# class Shop(object):
#
#     variables = {}    # Словарь продуктов Shop
#
#     @classmethod
#     def validate(cls, name):
#         if name not in cls.variables:
#             return name
#
#     def __init__(self, name, price, quantity):
#         if self.validate(name):
#             self.name = name
#             self.price = price
#             self.quantity = quantity
#             self.variables[name] = {'Цена': price, 'Кол-во': quantity}
#         else:
#             print(f'Продукт с именем - {name} - существует, '
#                   f'\nизмените название или измените соответствующие параметры у существующего!')
#
#     def set_product(self, name, price, quantity):
#             self.name = name
#             self.price = price
#             self.quantity = quantity
#             Shop.variables[name] = {price, quantity}
#
#     def get_product(self):
#         return self.name, self.price, self.quantity
#
#     @classmethod
#     def search_product(cls, name):
#         if name in cls.variables:
#             return name, cls.variables[name]
#         else:
#             return "Продукта с таким названием в магазине нет!"
#
#     def __str__(self):
#         return f"Название - {self.name}, Цена - {self.price}, Количество - {self.quantity}"
#
#
#     def del_product(self, name):
#         del Shop.variables[name]
#         print(f'Продукт {name} - удален из словаря продуктов!')
#
#     def __del__(self):
#         del self


# product1 = Shop(name = "Банан", price = 100, quantity = 10)
# product2 = Shop(name = "Апельсин", price = 130, quantity = 30)
# product3 = Shop(name = "Авокадо", price = 230, quantity = 10)
# product4 = Shop(name = "Манго", price = 330, quantity = 8)
# product5 = Shop(name = "Яблоко зеленое", price = 30, quantity = 60)
# product6 = Shop(name = "Яблоко красное", price = 40, quantity = 50)

# print(Shop.variables)  # Выводит весь словарь продуктов Shop
# print(product1.name)  # Выводит атрибут имя - name экземпляра класса
# print(product1.price)  # Выводит атрибут цена - price экземпляра класса
# print(product1.quantity)  # Выводит атрибут кол-во - quantity экземпляра класса
# print(product1.__dict__)  # Выводит все атрибуты экземпляра класса в виде словаря
# print(product2.name)
# print(product2.price)
# print(product2.quantity)
# print(product2.get_product())  # Возвращает все атрибуты экземпляра класса

# # валидатор не позволяет создать продукт с именем из словаря
# product7 = Shop(name = "Банан", price = 80, quantity = 15)

# product1.set_product(name = "Банан", price = 40, quantity = 3)  # изменяем значения атрибутов экземпляра класса
# print(product1.get_product())
# print(Shop.variables)

# print(Shop.search_product(name = 'Хлеб'))  # Поиск наименования продукта в словаре продуктов магазина

# print(Shop.search_product(name = 'Банан'))
# product1.del_product(name = 'Банан') # удаляет продукт из словаря, НЕ удаляет экземпляр класса
# del product1    # удаляет экземпляр класса
# print(product1.get_product())
# print(Shop.variables)

# создание нового продукта с name ранее удаленным из списка
# product7 = Shop(name = "Банан", price = 80, quantity = 15)
# print(product7)     # строковое описание экземпляра класса

'''
4.	Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
Каждая копилка имеет ограниченную вместимость, которая выражается целым числом –
количеством монет(capacity -вместимость), которые можно положить в копилку.
Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность
добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет,
не превышая ее вместимость.
Класс должен иметь следующий вид:
class MoneyBox:
    def__init__(self, capacity) :
    #конструктор с аргументом- вместимость копилки
    def can_add(self,v)
    #True, если можно добавить v монет, False иначе
    def add(self,v)
    #положить v монет в копилку
При создании копилки, число монет в ней равно 0.
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
'''

# class MoneyBox:
#     DEFAULT_QUANTITY = 0
#
#     def __init__(self, capacity, quantity=DEFAULT_QUANTITY):
#         self.capacity = capacity
#         self.quantity = quantity
#
#     def get_quantity(self):
#         return (f'Количество монет в копилке - {self.quantity}, \nможно положить - {self.capacity - self.quantity}')
#
#     def can_add_coin(self, v: int):
#         if v + self.quantity <= self.capacity:
#             return True
#         else:
#             return False
#
#     def add_coin(self, v: int):
#         if self.can_add_coin(v) == True:
#             self.quantity = self.quantity + v
#         else:
#             print(f'В копилку нельзя поместить - {v} монет,'
#                   f' \nможно положить - {self.capacity - self.quantity} ,'
#                   f' заведите ещё одну копилку:)')
#
#
# coinbox1 = MoneyBox(200)
# coinbox2 = MoneyBox(300)
# coinbox3 = MoneyBox(400)
#
# print(coinbox1.__dict__)
# print(coinbox1.get_quantity())
# coinbox1.add_coin(145)
# print(coinbox1.get_quantity())
# coinbox1.add_coin(100)
# print(coinbox2.get_quantity())
# print(coinbox2.get_quantity())
# coinbox2.add_coin(1370)
# coinbox2.add_coin(170)
# print(coinbox2.get_quantity())

'''
1.	Задача на взаимодействие между классами. Разработать систему «Интернет-магазин». 
Товаровед добавляет информацию о Товаре. Клиент делает заявку на товар, если товар есть в наличие в 
магазине то покупатель оплачивает товар иначе товаровед делает запрос на склад о наличии товара.
'''

# class Market:
#     instock = {}
#     outstock = {}
#
#     def __init__(self, pname: str, price: int, quantity: int):
#         self.pname = pname
#         self.price = price
#         self.quantity = quantity
#         self.instock[pname] = {"Цена": price, "Количество": quantity}
#
#     def __str__(self):
#         return f"Название: {self.pname}, Цена: {self.price}, Количество: {self.quantity}"
#
#     def get_pr(self):
#         return self.pname, self.price, self.quantity
#
#     @classmethod
#     def validate(cls, pname: str):
#         if pname not in cls.instock:
#             return True
#
#     def set_pr(self, pname: str, price: int, quantity: int):
#         if self.validate(pname) != True:
#             self.pname = pname
#             self.price = price
#             self.quantity = quantity
#             a = self.instock.get(pname)['Цена']
#             b = self.instock.get(pname)['Количество']
#             self.instock[pname] = {"Цена": ((a * b) + (price * quantity)) // (b + quantity), "Количество": quantity + b}
#         else:
#             print(f'Карточки такого товара - {pname}, нет в магазине, сначала создайте карточку товара.')
#
#     @classmethod
#     def request(cls):
#         if len(cls.outstock) != 0:
#             print(f"Необходимо сформировать запрос на склад, на товары {cls.outstock}!")
#             return True
#         else:
#             print(f"Отсутствуют позиции для запроса на склад!")
#             return False
#
#
# class Manager(Market):
#     def __init__(self, name: str):
#         self.name = name
#
#     def request(self):
#         if super().request() == True:
#             print(f'Запрос на поставку товаров сформировал - {self.name} и направил на склад, ожидаем ответ!')
#
#
# class Customer(Market):
#
#     def __init__(self, cname: str, cash: int = 0):
#         self.cname = cname
#         self.cash = cash
#
#     def __str__(self):
#         return f"Имя: {self.cname}, Cash: {self.cash}"
#
#     def deal(self, pname, quantity):
#         if pname in super().instock:
#             if self.cash > super().instock.get(pname)['Цена']:
#                 if quantity <= super().instock.get(pname)['Количество']:
#                     super().instock.get(pname)['Количество'] = super().instock.get(pname)['Количество'] - quantity
#                     self.cash = self.cash - super().instock.get(pname)['Цена']
#                     return f"Сделка успешно состоялась!"
#                 else:
#                     need = quantity - super().instock.get(pname)['Количество']
#                     super().outstock[pname] = need
#                     return (f"В наличии: {super().instock.get(pname)['Количество']}!"
#                             f" \nЗапросим на складе: {need}. \nВы можете оформить заказ на кол-во из наличия! ")
#             else:
#                 return (f"У Вас, {self.cname}, не хватает {super().instock.get(pname)['Цена'] - self.cash}."
#                         f"\nПополните Cash!")
#         else:
#             return f"Такого товара - {pname} - нет в продаже!"
#
#
# product1 = Market(pname="ноутбук", price=50000, quantity=3)
# product2 = Market(pname="планшет", price=25000, quantity=7)
# product3 = Market(pname="наушники", price=10000, quantity=3)
# product4 = Market(pname="телевизор", price=70000, quantity=2)
# product5 = Market(pname="робот-пылесос", price=35000, quantity=1)
# product6 = Market(pname="монитор", price=30000, quantity=4)
#
# customer1 = Customer(cname="John", cash=100000)
# customer2 = Customer(cname="Alice", cash=80000)
# customer3 = Customer(cname="John", cash=10000)
#
# # print(product1)
# # print(customer1)
# # print(Market.instock)
# print(customer1.deal("ноутбук", quantity=4))
# # print(Market.instock)
# print(customer2.deal('монитор', quantity=3))
# # print(customer2)
# print(customer3.deal('планшет', quantity=1))
# # print(customer3)  # Информация по покупателю, остаток Cash
# print(customer1.deal("iphone", quantity=1))
#
# product5.set_pr(pname='робот-пылесо', price=36000, quantity=3)  # Поставка товара
# product5.set_pr(pname='робот-пылесос', price=36000, quantity=3)
# # print(Market.instock)  # Список товаров в наличии в магазине
# # print(Market.outstock)  # Список товаров для запроса на склад
#
# manhead = Manager("Ivan")  # Руководитель отдела закупки магазина
# manhead.request()  # Запрос руководителя отдела закупки

'''
2.	Задача на взаимодействие между классами. Разработать систему «Вступительные экзамены».
Абитуриент регистрируется на Факультет, сдает Экзамены. Преподаватель выставляет Оценку.
Система подсчитывает средний бал и определяет Абитуриента, зачисленного в учебное заведение.
'''

# class University:
#     _passcore = {}
#     _examdict = {}
#     _examgrades = {}
#
#     def __init__(self, name: str, age: str) -> None:
#         self.name = name
#         self.age = age
#
#     def __init__(self, name_faculty: str, avggrade: int) -> None:
#         self.name_faculty = name_faculty
#         self._passcore[name_faculty] = avggrade
#
#     def get(self):
#         return self._passcore
#
#     def validate_age(self, age: int) -> bool:
#         if int(self.age) > 16:
#             return True
#         else:
#             return False
#
#     def exams_app(self, exam: str):
#         if self.validate_age(self.age):
#             # ntr = exam + " " + self.name
#             self._examdict[exam + " " + self.name] = exam
#             # self._examdict[ntr] = exam
#             print("Вы допущены к экзамену.")
#             print("Экзамен состоялся, ожидайте результат!")
#         else:
#             print("Вы слишком молоды, приходите в следующем году!")
#
#     def check_teach(self):
#         if self.exam in str(self._examdict):
#             print("Есть результаты тестирования для проверки!")
#             return True
#         else:
#             print("Нет результатов тестирования для проверки!")
#             return False
#
#     def fingrade(self):
#         if self.check_teach():
#             for key, value in self._examdict.items():
#                 if value == self.exam:
#                     self._examgrades[key] = int(input(f"Введите оценку для {key}: "))
#         else:
#             print('Никто не сдавал тестирование по Вашему предмету!')
#
#
# class Teacher(University):
#     def __init__(self, name: str, exam: str) -> None:
#         self.name = name
#         self.exam = exam
#
#     def __str__(self) -> str:
#         return f'Имя: {self.name}, Предмет: {self.exam}'
#
#
# class Applicant(University):
#     def __init__(self, name: str, age: str) -> None:
#         self.name = name
#         self.age = age
#
#     def __str__(self) -> str:
#         return f'Имя: {self.name}, Возраст: {self.age}'
#
#     def sum_grade(self, fac: str):
#         sumgrade = 0
#         for key, value in University._examgrades.items():
#             if self.name in key:
#                 sumgrade += value
#         if fac in self._passcore:
#             if self._passcore[fac] <= sumgrade:
#                 print(f'Ваш средний балл = {sumgrade}')
#                 print(f"Вы, {self.name}, зачислены на факультет - {fac}!")
#             else:
#                 print(f'Ваш средний балл = {sumgrade}')
#                 print(f'{self.name}, Ваш средний балл ниже необходимого, '
#                       f'\nВы не можете быть зачислены на факультет - {fac}!')
#
#
# # Факультеты и средний бал для зачисления
# fac1 = University(name_faculty='law', avggrade=12)
# fac2 = University(name_faculty='it', avggrade=14)
# fac3 = University(name_faculty='journalism', avggrade=12)
# # print(University._passcore)
# # Абитуриенты: Имя и возраст
# app1 = Applicant(name='Ann', age='18')
# app2 = Applicant(name='Ivan', age='17')
# app3 = Applicant(name='Alex', age='15')
# # print(app1)
#
# teach1 = Teacher(name='MR. Smith', exam='history')
# teach2 = Teacher(name='MR. Brown', exam='maths')
# teach3 = Teacher(name='MR. Dodd', exam='language')
# # print(teach1)
#
# # Запись абитуриента на экзамены
# app1.exams_app(exam='history')
# app2.exams_app(exam='maths')
# app3.exams_app(exam='history')
# app3.exams_app(exam='language')
# app3.exams_app(exam='maths')
# app1.exams_app(exam='language')
# app2.exams_app(exam='language')
# app1.exams_app(exam='maths')
# app2.exams_app(exam='history')
#
# # Проверка словаря тестирования на наличие в нём предметов для проверки преподавателем
# # teach2.check_teach()
# # teach3.check_teach()
# # teach1.check_teach()
# # print(University._examdict)
#
# # Проверка преподавателем экзаменов абитуриентов и выставление оценок - вводим в консоли
# teach1.fingrade()
# teach2.fingrade()
# teach3.fingrade()
# # Словарь оценок результатов тестирования
# # print(University._examgrades)
#
# # Проверка среднего балла и зачисления на факультет
# app1.sum_grade(fac="it")
# app2.sum_grade(fac="law")
# app3.sum_grade(fac="it")
