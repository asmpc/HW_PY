import os
import json

# print(os.getcwd())
os.chdir('D:/PY/files')
# print(os.getcwd())

# 1. Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.

# file_path = "text_file.txt"
# if os.path.exists(file_path):
#     print(f"Файл {file_path} существует")
# else:
#     print(f"Файл {file_path} не найден")
#
# print(os.listdir())

# texts = ""
# while True:
#     text = input("Введите строку (для завершения нажмите Enter): ")
#     if text == "":
#         break
#     texts += text + "\n"
#
# with open (
#     file="text_file.txt",
#     mode="w",
#     encoding="Utf-8"
# ) as f:
#     f.write(texts)

# 2. В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.

# texts = ""
# while True:
#     text = input("Введите строку (для завершения нажмите Enter): ")
#     if text == "":
#         break
#     texts += text + "\n"
#
# with open (
#     file="text_file.txt",
#     mode="a",
#     encoding="Utf-8"
# ) as f:
#     f.write(texts)

# 3. Дан текстовый файл. Подсчитать количество символов в нем. Без \n

# with open (
#     file="text_file.txt",
#     mode="r",
#     encoding="Utf-8"
# ) as f:
#     data = f.read()
#
# count = 0
# for line in data:
#     if line != "\n":
#         count += 1
# print(count)

# 4. Имеется текстовый файл, содержащий 5 строк. Переписать каждую из его строк в список в том же порядке.

# with open (
#     file="text_file.txt",
#     mode="r",
#     encoding="Utf-8"
# ) as f:
#     data = f.read()
#     data = list(map(str, data.split("\n")))
#     print(data)


# 5. Имеется текстовый файл. Получить текст, в котором в конце каждой строки из
# заданного файла добавлен восклицательный знак.
# Fas dsad asd
# Asda das dsad!
# Dasd dsad das
# Dasda asd asd das!

# with open (
#     file="text_file.txt",
#     mode="r",
#     encoding="Utf-8"
# ) as f:
#     data = f.read()
#     data = list(map(str, data.split("\n")))
#     new_data = ""
#     for item in data:
#         if "!" in item:
#             new_data += item + "\n"
#     print(new_data)

# 6. В справочной аэропорта хранится расписание вылета самолетов
# на следующие сутки. Для каждого рейса указаны номер рейса, пункт назначения,
# время вылета. Вывести все номера рейсов и время вылета самолета для
# заданного пункта назначения. Пример файла flights.json

# path = "flights.json"
# mode = "r"
# with open(file=path,mode=mode,encoding='Utf-8') as file:
#     data = json.load(file)
#     destination = str(input("Введите пункт назначения: "))
#     for item in data:
#         for value in item.values():
#             if destination in value:
#                 newdata = list(item.values())
#                 newdata.remove(destination)
#                 print(newdata)

# 7.	Ведомость студентов, сдававших сессию, содержит ФИО и оценки по четырем предметам.
# Вывести список студентов, сдавших сессию со средним баллом больше 7.
# Пример файла student_grades.json

# path = "student_grades.json"
# mode = "r"
# with open(file=path,mode=mode,encoding='Utf-8') as file:
#     data = json.load(file)
#     dct_n = {}
#     for student in data:
#         for item in student.values():
#             if type(item) != list:
#                 keys = item
#             else:
#                 values = item
#                 avg = sum(values) / len(values)
#         # проверка условия, что средний бал больше 7
#         if avg > 7:
#             dct_n[keys] = avg
#
#     print(dct_n)

# 8. Вашей задачей будет восстановление исходной строки обратно.
# Напишите программу, которая считывает из файла строку,
# соответствующую тексту, сжатому с помощью кодирования повторов,
# и производит обратную операцию, получая исходный текст.
# Для решения вам необходимо открыть файл для чтения 8.txt

# path = "8.txt"
# mode = "r"
# with open(
#         file=path,
#         mode=mode,
#         encoding="Utf-8"
# ) as f:
#     strd = f.read()
#     strd = strd.strip()
#     strdn = ""
#     cnt = ''
#
#     for i in reversed(range(len(strd))):  # класс сложности - O(N)
#         if strd[i].isdigit():
#             cnt += str(strd[i])
#         else:
#             cnt = cnt[::-1]
#             strdn += strd[i] * int(cnt)
#             cnt = ''
#     print(f'Преобразуется в - {strdn[::-1]}')


# 9. Имеется текстовый файл 9.txt. Найдите самое часто встречаемое слово в этом файле.
# В ответе выведете само слово и сколько оно раз встретилось. Если слов более одного.
# Выведите все слова, и сколько раз они встречались

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
# path = "9.txt"
# mode = "r"
# with open(
#         file=path,
#         mode=mode,
#         encoding="Utf-8"
# ) as f:
#     strd = f.read()
#     strd = strd.replace("\n", " ")
#     lst = strd.split(" ")
#
# fl = LogReader(lst)
# dct = {}
# cnt = 1
# for i in fl:
#     if i:
#         dct[i] = cnt
#         cnt += 1
#
# max_value = 0
# max_key = []
# for k, v in dct.items():
#     if v > max_value:
#         max_value = v
#         max_key = k
#     elif max_value == v:
#         max_key.append(k)
#
# print(f"Самое встречаемое слово (или слова) : {max_key}, количество: {max_value}")