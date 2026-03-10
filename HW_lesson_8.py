#1.	Опишите конструкцию отлова ошибок, так чтобы выводило, какую ошибку вы сделали. Код представлен ниже:
# x = (1, 2, 5, 7)
# x = x  / 2
# print(x)

# try:
#     x = (1, 2, 5, 7)
#     x = x / 2
#     print(x)
# except Exception as exc:
#     print(type(exc), exc.args)
# # max класс сложности - O(1)

# 2. Напишите программу, которая будет ловить IndexError,
# когда вы пытаетесь взять индекс элемента, которого нет в списке.

# lstnumb = [1,2,3,4,5,6,7,8,9,10]
# indlst = int(input("Введите индекс элемента: "))
#
# try:
#     print(lstnumb[indlst])
# except IndexError:
#     print("IndexError")
# # max класс сложности - O(1)

'''
3.	Напишите программу, которая вычисляет площадь треугольника по формуле Герона,
однако если пользователь введёт длину хоть одной стороны треугольника равную 0,
то программа должна бросить исключение ArithmeticError.
'''

# try:
#     a = int(input('Введите сторону a треугольника: '))
#     b = int(input('Введите сторону b треугольника: '))
#     c = int(input('Введите сторону c треугольника: '))
# # если try перенести сюда, то при вводе не int выпадет ошибка, а не выдаст исключение
#     if a != 0 and b != 0 and c!=0:
#         p = (a + b + c) / 2
#         S = (p *(p-a)*(p-b)*(p-c))**0.5
#         print(f"Площадь треугольника = {S}")
#     else:
#         raise ArithmeticError("ArithmeticError") # при вводе 0 - бросает ArithmeticError
#
# except Exception as exc:    # срабатывает как на ArithmeticError, так и на любую другую ошибку
#     print(type(exc), exc.args)
# # max класс сложности - O(1)

'''
4.	Дан список. Пользователь не знает его размер. Программа должна бросить исключение TypeError, 
когда пользователь пытается удалить элемент которого нет в списке.
'''

# lstnumb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# try:
#     lstnumb.remove(int(input("Введите элемент для удаления из списка: ")))
#     print(lstnumb)
# except:
#     print('TypeError')
# # max класс сложности - O(1)

'''
5.	Дан словарь, который содержит некоторые ключи и значения по этим ключам, пользователь не знает этих ключей. 
Бросьте ошибку KeyError в том случае когда пользователь пытается просмотреть значение по ключу, которого нет в словаре.
'''

# dictnumb = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3', 'key4' : 'value4', 'key5' : 'value5'}
# keyreq = input('Введите нужный ключ: ')
#
# try:
#     print(dictnumb[keyreq])
# except KeyError:
#     print('KeyError')
# # max класс сложности - O(1)

'''
6.	Дана строка, содержащая числа, разделённые пробелами. Нужно вывести их сумму. 
Если хотя бы один элемент не является числом — перехватить исключение и пропустить его. "10 5 abc 3" → 18
'''

# Первый способ с for:

# strsum = input("Введите строку: ")
# lstsum = list(strsum.split())
# numb = 0
# sumnumb=0
#
# for i in range(len(lstsum)):  # класс сложности - O(N)
#     try:
#         numb = int(lstsum[i])
#         sumnumb += numb
#         i=i+1
#     except ValueError:
#         continue
# print(f'Сумма = {sumnumb}')
# # max класс сложности - O(N)

# Второй способ с while:

# strsum = input("Введите строку: ")
# lstsum = list(strsum.split())
# i=0
# numb = 0
# sumnumb=0
#
# while i < len(lstsum):    # класс сложности - O(N)
#     try:
#         numb = int(lstsum[i])
#         sumnumb = sumnumb + numb
#         i=i+1
#     except ValueError:
#         i = i + 1
#         continue
# print(f'Сумма = {sumnumb}')
# # max класс сложности - O(N)

# 7.    Написать алгоритм, считающий частоту букв в строке. Если входные данные — не строка, выбросить TypeError.

# strnew = input("Введите строку: ")
# strnew = strnew.replace(' ', '')
# try:
#     if strnew.isalpha():
#         strnew = strnew + " "
#         for i in range(1, len(strnew)):   # класс сложности - O(N)
#             if strnew[i] != strnew[i-1]:
#                 print(strnew[i-1], strnew.count(strnew[i-1]))
#     else:
#         raise TypeError
# except TypeError:
#     print('TypeError')
# # max класс сложности - O(N)

'''
8.	Реализовать алгоритм бинарного поиска. Если входной список не отсортирован, выбросить ValueError.
Если искомого элемента нет, вернуть None.
'''

# lstin = [1, 2, 3, 5, 7, 9, 11, 12, 13, 14, 15, 17, 19, 20, 21, 22, 23, 28, 30, 45, 48]
#
# try:
#     if lstin == sorted(lstin) :
#         def binsearch (list, item):   # Бинарный поиск из Грокаем алгоритмы
#             low = 0
#             high = len(list)-1
#
#             while low <= high:
#                 mid = (low+high)//2
#                 guess = list[mid]
#                 if guess == item:
#                     return mid
#                 if guess > item:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             return None
#     else:
#         raise ValueError
#
#     print(f'Index искомого элемента - {binsearch(lstin, int(input('Введите искомый элемент: ')))}')
#
# except ValueError:
#     print('ValueError')
# # max класс сложности - O(logN)



