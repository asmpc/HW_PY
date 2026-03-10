'''
1. Напишите функцию m(a, b), вычисляющую минимум двух чисел.
С помощью вашей функции найдите минимальное четырёх чисел.
'''


# def min_2_numb(a: int, b: int) -> int:
#     '''
#     :param a: any number
#     :param b: any number
#     :return: min number between a and b
#     '''
#     if a < b:
#         min_num = a
#     else:
#         min_num = b
#     return min_num
#
#
# try:
#     print('Вводим 4 числа, получаем минимальное')
#     print()
#     # отлавливаем ошибку пользователя, если ввёл не число
#     num1 = int(input("Введите число: "))
#     num2 = int(input("Введите число: "))
#     num3 = int(input("Введите число: "))
#     num4 = int(input("Введите число: "))
#
#     min_num = min_2_numb(num1, num2)
#     min_num = min_2_numb(min_num, num3)
#     min_num = min_2_numb(min_num, num4)
#
#     print(f'Минимальное число = {min_num}')
# except ValueError:
#     print('Ошибка, ввели не число!')
# # max класс сложности - O(1)

'''
2.	Дано натуральное число n > 1. Проверьте, является ли оно совершенным.
Программа должна вывести слово YES, если число совершенное и NO, в противном случае.
'''


# def perfect_number(n: int) -> str:
#     '''
#     :param n:  any number > 1
#     :return: if n is perfect, return "YES" or return "NO"
#     '''
#     s = True
#     for i in range(2, n):  # класс сложности - O(N)
#         if n % i == 0:
#             s += i
#             i += 1
#         else:
#             i += 1
#     if n == s:
#         print("YES")
#     else:
#         print("NO")
#
#
# try:
#     # отлавливаем ошибку ввода числа пользователем
#     print('''Ввести натуральное число n > 1. Если оно является совершенным,
# программа должна вывести слово YES, в противном случае NO''')
#     print()
#     n = int(input('Введите натуральное число n > 1: '))
#     if n <= 1:
#         raise ValueError
#     perfect_number(n)
# except ValueError:
#     print("Ошибка ввода числа!")
# # max класс сложности - O(N)

'''
3.	Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. 
Ищем число Фиббоначи через цикл! Рекурсию не использовать! 
'''


# def fib(n: int) -> int:
#     '''
#     :param n: number to calculate fibonacci number
#     :return: fibonacci number
#     '''
#     numfib = False
#     if n == 0:
#         return n
#     elif n == 1:
#         return n
#     else:
#         n_1 = 1
#         n_2 = 0
#         for i in range(2, n + 1):  # класс сложности - O(N)
#             numfib = n_1 + n_2
#             n_2 = n_1
#             n_1 = numfib
#     return numfib
#
#
# try:
#     # Отлавливаем ошибку ввода числа пользователем
#     print('Ищем число Фиббоначи')
#     print()
#     n = int(input("Введите n >= 0: "))
#     if n < 0:
#         raise ValueError
#     else:
#         print(f'Число Фиббоначи от {n} = {fib(n)}')
# except ValueError:
#     print('Ошибка ввода числа!')
# # max класс сложности - O(N)

'''
4.	Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x 
и возвращающую самое маленькое целое число y, такое что:     
-y больше или равно x                                                                                  
-y делится нацело на 5
'''


# def closest_mod_5(x: int) -> int:
#     '''
#     :param x: any number
#     :return: number that closest mod 5
#     '''
#     y = x
#     if y >= x and y % 5 == 0:
#         return y
#     else:
#         if y % 5 == 1:
#             y += 4
#             return y
#         elif y % 5 == 2:
#             y += 3
#             return y
#         elif y % 5 == 3:
#             y += 2
#             return y
#         elif y % 5 == 4:
#             y += 1
#             return y
#
#
# print('''Введите целое число x, функция вернет самое маленькое целое число y, такое что:
# -y больше или равно x
# -y делится нацело на 5''')
# print()
# x = int(input('Введите целое число x: '))
# print(f'Для x = {x} минимальное число y = {closest_mod_5(x)}')
# # max класс сложности - O(1)

'''
5.	В языке Python есть некоторые ограничения на имена переменных. Имена переменных
-могут состоять только из цифр, букв и знаков подчеркивания.
-не могут начинаться с цифры.
Программист вводит строки с именами переменных. Для каждой переменной нужно вывести "Можно использовать",
если ее имя корректно, или "Нельзя использовать", если это не так. Определив все нужные переменные,
программист заканчивает ввод строкой "Поработали, и хватит".
Для проверки каждой строки используйте функцию check_variable(v). Для простоты будем считать,
что программист использует только латинские буквы.  Не может содержать : ! @ # $ % ^ & * ()
'''


# def check_variable(v: str) -> str:
#     '''
#     :param v: name of variable to check
#     :return: can use or not
#     '''
#     lstsmb = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
#     for i in lstsmb:  # класс сложности - O(N)
#         if i in v:
#             s = True
#             break
#         else:
#             s = False
#     if v == "Поработали, и хватит":
#         return ''
#     if v.isdigit() == False and v.islower() == True and s == False and v[0].isdigit() == False:
#         print("Можно использовать")
#         v = input('Введите имя переменной: ')
#         check_variable(v)
#         if v == "Поработали, и хватит":
#             return ''
#     else:
#         print("Нельзя использовать")
#         v = input('Введите имя переменной: ')
#         check_variable(v)
#         if v == "Поработали, и хватит":
#             return ''
#
#
# print('''Введите имена переменных, если их можно использовать Вы получите соответствующий ответ.
# Хотите закончить работу, введите - Поработали, и хватит''')
# print()
# v = input('Введите имя переменной: ')
# print(check_variable(v))
# # max класс сложности - O(N)

# 6.	Сгенерировать список нечётных двузначных чисел.

# lstnew_2 = [el for el in range(10, 100) if el % 2 != 0]
# print(lstnew_2)
# # max класс сложности - O(N)

# 7.	Сгенерировать список всех трёхзначных чисел кратных 5 и 3.

# lstnew_3 = [el for el in range(100, 1000) if el % 5 == 0 and el % 3 == 0]
# print(lstnew_3)
# # max класс сложности - O(N)

'''8.	Дан список, упорядоченный по не убыванию элементов в нем. 
Напишите функцию которая определяет количество в нем различных элементов. set функцию не использовать. 
'''

# # lst_elem_sort = [1, 2, 3, 'as', 'ert', 3, 4, 5, 6, 2, 3, "as", "for", 'three', 5, 7, 8, 9]
# lst_elem_sort = [1, 2, 2, 3, 5, 6, 6, 6, 6, 6, 7, 7, 9, 23, 56, 56, 78]
#
#
# def dif_elem_sum(lst_elem_sort: list) -> int:
#     '''
#     :param lst_elem_sort: any list
#     :return: sum different elements of list
#     '''
#     lst_elem_dif = []
#     for elem in lst_elem_sort:  # класс сложности - O(N)
#         if elem not in lst_elem_dif:
#             lst_elem_dif.append(elem)
#     sumelem = len(lst_elem_dif)
#     return sumelem
#
#
# print('''Дан список элементов. Функция определяет количество в нем различных элементов.''')
# print(lst_elem_sort)
# print()
# print(f'Количество различных элементов списка = {dif_elem_sum(lst_elem_sort)}')
# # max класс сложности - O(N)

'''
9.	Напишите программу, на вход которой подаётся список чисел одной строкой. 
Программа должна для каждого элемента этого списка вывести сумму двух его соседей. 
Для элементов списка, являющихся крайними, одним из соседей считается элемент, 
находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", 
то на выход ожидается список "13 6 9 15 7" (без кавычек).Если на вход пришло только одно число, надо вывести его же. 
Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
'''

# print('''На вход подаётся список чисел одной строкой.
# Программа для каждого элемента этого списка выводит сумму двух его соседей''')
# print()
# try:
#     # Отлавливаем ошибку ввода пользователем списка чисел
#     lstnum = list(map(int, input('Введите список чисел одной строкой, через пробел: ').split()))
#
#     new_list = []
#     if len(lstnum) == 1:
#         print(f'У одного числа нет соседей :( новый список - {lstnum[0]}')
#     else:
#         for el in lstnum:  # класс сложности - O(N)
#             if el == lstnum[0]:
#                 el = lstnum[1] + lstnum[-1]
#                 new_list.append(el)
#             elif el != lstnum[-1]:
#                 indbef = lstnum.index(el) - 1
#                 indaft = lstnum.index(el) + 1
#                 el = lstnum[indbef] + lstnum[indaft]
#                 new_list.append(el)
#             else:
#                 el = lstnum[-2] + lstnum[0]
#                 new_list.append(el)
#         # lstnum из int - циклом item переводим в str и join в new_str
#         new_str = ' '.join(str(item) for item in new_list)  # класс сложности - O(N)
#         print(f'Новый список чисел  - {new_str}')
# except Exception as exc:
#     print("Ошибка ввода списка чисел!", type(exc))
# # max класс сложности - O(N) + O(N) = O(2N) = O(N)

# 10. Дан список, состоящий из строк. Отсортировать его по длине слов. Сначала должны идти длинные слова затем короткие.

# def sort_wrd_len(lststr: list) -> list:
#     '''
#     :param lststr: list of str (any words)
#     :return: list of str sorted by len(word)
#     '''
#     newdict = dict()
#     for el in lststr:  # класс сложности - O(N)
#         cnt = len(el)
#         newdict[el] = cnt
#         lstkeys = sorted(newdict, key=newdict.get, reverse=True)
#     return lstkeys
#
#
# print('''Дан список, состоящий из строк. Отсортировать его по длине слов.
# Сначала должны идти длинные слова затем короткие.''')
# print()
# lststr = list(map(str, input("Введите список, состоящий из слов, одной строкой, через пробел: ").split()))
# # alpha alnum swapcase join after capitalize sigma boy mother art available
# print(f"Отсортированный список выглядит так: \n{sort_wrd_len(lststr)}")
# # max класс сложности - O(N)

# 11.	Дан список состоящий из слов. Отсортировать его по количеству вхождений буквы 'a'

# def sort_lst_a(lststr: list) -> list:
#     '''
#     :param lststr: list of str
#     :return: list of str sorted by 'a'
#     '''
#     newdict = dict()
#     for el in lststr:  # класс сложности - O(N)
#         if 'a' in el:
#             cnt = el.count('a')
#             newdict[el] = cnt
#         else:
#             cnt == 0
#             newdict[el] = 0
#     lstkeys = sorted(newdict, key=newdict.get, reverse=True)  # класс сложности - O(N)
#     # изначально я сделал как ниже, но так сложнее
#     # newdictsort = dict(sorted(newdict.items(), key=lambda x: x[1], reverse=True))  # класс сложности - O(N)
#     # lstkeys = [key for key in newdictsort.keys()]  # класс сложности - O(N)
#     return lstkeys
#
#
# print("Дан список состоящий из слов. Отсортировать его по количеству вхождений буквы 'a'")
# print()
# lststr = list(map(str, input("Введите список, состоящий из слов, одной строкой, через пробел: ").split()))
# # alpha alnum swapcase join after capitalize sigma boy mother art available
# print(f'Отсортированный список по количеству вхождений "a" - {sort_lst_a(lststr)}')
# # max класс сложности - O(N) + O(N) = O(2N) = O(N)

# 12.   *Сгенерировать список всех простых чисел до  100 с помощью генератора.

# print("Сгенерировать список всех простых чисел до  100 с помощью генератора.")
# print()
# n = int(input("Введите n: "))

# # Первое решение - путем проверки всех элементов последовательности.
# lst_simp_num = [i for i in range(2, n) if (1<i<10 and i%2 !=0
#                                              and i%3 !=0 or i==2 or i==3) or (i % 2  != 0
#                                                                               and i % 3 != 0 and i % 5 != 0
#                                                                               and i % 7 != 0 and i % 10 != 0)]
# print(lst_simp_num)
# # max класс сложности - O(N)

# Второе решение с отсечением из последовательности составных чисел, нашел объяснение в инете
# Сходным принципом решалась задача из домашки на разборе
# def simp_num(n: int) -> list(int):
#     '''
#     :param n: any number
#     :return: list of numbers with simple numbers
#     '''
#     simpn = [True] * n
#     list_simpn = []
#     for i in range(2, n):   # класс сложности - O(N)
#         if simpn[i]:
#             list_simpn.append(i)
#             for x in range(i * i, n, i):    # класс сложности - O(N)
#                 simpn[x] = False
#     return list_simpn
# print(simp_num(n))
# # max класс сложности - O(N) * O(N) =O(N**2)
'''Этот алгоритм будет выполняться существенно быстрее при очень больших n, так как при проверке
чисел до 10 происходит отсеивание всех чисел до n полученных перемножением числа на число с шагом числа.'''

'''13.	 Напишите функцию которая принимает, неотрицательное целое число n
— столько элементов последовательности должна отобразить программа которая выводит часть последовательности
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно).
Функция ничего не возвращает, только выводит последовательность
Sample Input:
7
Sample Output:
1 2 2 3 3 3 4
Sample Input 2:
10
Sample Output 2:
1 2 2 3 3 3 4 4 4 4
'''

# def seqn(n: int) -> str:
#     '''
#     :param n: number int > 0
#     :return: sequence of numbers len = number
#     '''
#     seqn = ""
#     z = 3 + n // 3  # коррекция длины последовательности
#     for i in range(1, z):  # класс сложности - O(N)
#         seqn += str(i) * i
#     print(seqn[0:n])
#
#
# print('''Функция принимает неотрицательное целое число n
# — столько элементов последовательности должна отобразить программа''')
# print()
# n = int(input('Введите  неотрицательное целое число n: '))
# seqn(n)
# # max класс сложности - O(N)

