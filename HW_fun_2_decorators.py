from functools import reduce

'''
1.	Написать декоратор log_result, который печатает результат выполнения функции.
Применить к функции возведения числа в квадрат.
'''

# # функция декоратор возводит в квадрат число, полученное в результате выполнения первоначальной функции
# # и выводит результат
# def log_result(fun: callable):
#     def inner(x: int):
#         '''
#         :param x: any number received from original function
#         :return: print number ** 2
#         '''
#         x = fun(x) ** 2
#         print(f'Применяем к функции возведение в квадрат и выводим результат - {x}')
#     return inner
#
# @log_result
# # функция выполняет сложения числа с самим собой
# def some_func(n: int) -> int:
#     '''
#     :param n: any integer number
#     :return: number + number
#     '''
#     return n + n
#
# # some_func = log_result(some_func)
# i = int(input("Введите любое число: "))
# some_func(i)

# 2.	Написать декоратор repeat(n), который повторяет вызов функции n раз и возвращает последний результат.

# def repeat(func: callable):
#     def inner_n(n: int):
#         if type(func(x))==int:
#             rez = 0
#         else:
#             rez = ""
#         while n>0:
#             i=func(x)
#             rez += i
#             n-= 1
#         print(f"Результат работы декоратора repeat(n) - {rez}")
#     return inner_n
#
# # @repeat
# # функция выполняет проверку полученного значения и если возможно переводит в int, иначе *str*
# def some_func(x) -> str or int:
#     if x.isdigit():
#         x = int(x)
#     else:
#         x = "*"+ x + "* "
#     return x
#
# some_func = repeat(some_func)
# x = input("Введите число или строку: ")
# some_func(int(input('Введите количество повторений функции - n: ')))

# 3.	Написать декоратор bench, который измеряет ошибки: если функция завершилась ошибкой, вывести её тип и сообщение.

# def bench(func: callable):
#     def inner(i):
#         try:
#             i = func(int(i))
#             print(f"Число умноженное на себя = {i}")
#             return i
#         except Exception as exc:
#             print("Error", type(exc))
#     return inner
#
# @bench
# def summ_i(i: int) -> int:
#     '''
#     :param i: any integer number
#     :return: number * number
#     '''
#     return i * i
#
# # summ_i = bench(summ_i)
# summ_i(input('Введите любое целое число: '))

# 4.	Дан список слов. Получить список их длин.

# print('Дан список слов. Получить список их длин.')
# lst_wrd = ['alpha', 'alnum', 'swapcase', 'join', 'after', 'capitalize', 'sigma', 'boy', 'mother', 'art', 'available']
# print(lst_wrd)
# print()
# lst_len_wrd = [len(el) for el in lst_wrd]  # класс сложности - O(N)
# print(f'Список длин слов: \n{lst_len_wrd}')
# # max класс сложности - O(N)

# 5.	Дан список: ['apple', 'Banana', 'cherry', 'DATE'].
# Получите новый список, оставив только слова в нижнем регистре.

# print('Дан список:')
# lst_wrd = ['apple', 'Banana', 'cherry', 'DATE']
# print(lst_wrd)
# print()
# lst_wrd_lwr = [el for el in lst_wrd if el == el.lower()]  # класс сложности - O(N)
# print(f'Новый список со словами в нижнем регистре: \n{lst_wrd_lwr}')
# # max класс сложности - O(N)

# 6.	Дан список кортежей (имя, возраст). Получите новый список, оставив кортеж в котором возраст > 18.

# print('Дан список кортежей (имя, возраст)')
# lst_tpna = [('Alice', 18), ('Bob', 19), ('Charlie', 20), ('John', 19), ('Kate', 17), ('Ann', 19), ('Mary', 18)]
# print(lst_tpna)
# lst_srt18 = [el for el in lst_tpna if el[1] > 18]   # класс сложности - O(N)
# print()
# print(f'Новый список с кортежами в котором возраст > 18 \n{lst_srt18}')
# # max класс сложности - O(N)

# 7.	Дан список списков: [[1,2],[3,4],[5,6]].
# С помощью reduce объединить в один список: [1,2,3,4,5,6].

# print('Дан список списков: [[1,2],[3,4],[5,6]], \nc помощью reduce объединили в один список:')
# lst_lst = [[1,2],[3,4],[5,6]]
# lst_jn = reduce(lambda x, y: x+y, lst_lst)
# print(lst_jn)

# 8.	Дан список ['cat','car','mouse','dog','snake','cow'].
# Получить словарь: {начальная буква: [слова...]}.

# print('Дан список:')
# lst_animals = ['cat','car','mouse','dog','snake','cow']
# print(lst_animals)
# print()
# dct_animals = {el[0] : [i for i in lst_animals if el[0] in i[0]] for el in lst_animals}
# print(f'Получили словарь: \n{dct_animals}')
# # max класс сложности - O(N)

# 9.	Дан список кортежей (товар, цена, количество).
# Получить список сумм: цена * количество.

# print('Дан список кортежей (товар, цена, количество).')
# lst_cost = [('book', 3, 11), ('textbook', 0.5, 20), ('pen', 1, 3), ('pencil', 0.2, 5), ('notebook', 1.5, 2)]
# print(lst_cost)
# print()
# list_sum = [el[1]*el[2] for el in lst_cost]
# print(f'Cписок сумм: цена * количество \n{list_sum}')

# 10.	Написать декоратор cache, который кеширует результаты функции,
# чтобы повторные вызовы с теми же аргументами не вычислялись.

# # функция декоратор, возвращает inner
# def cache():
#     dict_cache = {}
#     def inner(func):
#         def check_func(arg):
#             '''
#             функция проверяет наличие arg в словаре dict_cache, если его нет,
#             добавляет его в качестве ключа, запускает выполнение основной функции,
#             результат выполнения функции добавляет в качестве значения к ключу,
#             если arg есть - возвращает значение из словаря
#             '''
#             if arg not in dict_cache:
#                 new_value = func(arg)
#                 dict_cache[arg] = new_value
#             else:
#                 print("Возвращаем из cache")
#             return dict_cache[arg]
#         return check_func
#     return inner
#
# @cache()
# # функция возводит число в квадрат
# def add(a):
#     print("calculating sqt arg")
#     arg = a **2
#     return arg
#
# print(add(3))
# print(add(5))
# print(add(6))
# print(add(3))
# print(add(5))
# print(add(7))

'''
11.	Дана коллекция: items = [("A", 10), ("B", 20), ("A", 5), ("B", 7), ("C", 3)]
С помощью функции reduce получите: { "A": {"count": 2, "sum": 15, "avg": 7.5}, 
"B": {"count": 2, "sum": 27, "avg": 13.5}, "C": {"count": 1, "sum": 3, "avg": 3}}
'''

# print('Дана коллекция:')
# items = [("A", 10), ("B", 20), ("A", 5), ("B", 7), ("C", 3)]
# print(items)
#
# dict_items_sum = {k: reduce(lambda q, w: q + w, [x[1] for x in items if x[0] == k]) for k in [x[0] for x in items]}
# dict_items_count = {k: reduce(lambda q, w: q + w, [x[0] for x in items if x[0] == k]) for k in [x[0] for x in items]}
#
# dict_items = {}
# for k, v in dict_items_count.items():    # класс сложности - O(N)
#     for q, w in dict_items_sum.items():     # класс сложности - O(N)
#         if k == q:
#             dict_items[k] = {"count":v.count(v[0]), "sum": w, 'avg': w/v.count(v[0])}
# print("Словарь от items:")
# print(dict_items)
# # max класс сложности - O(N^2) + O(N^2) + O(N^2) = O(3N^2) = O(N^2)
