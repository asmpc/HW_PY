import sqlite3
from datetime import datetime, timedelta

# with sqlite3.connect('sqlite_db/library.db') as con:
#     cursor = con.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS books (
#                   id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   title TEXT,
#                   author TEXT,
#                   year INTEGER,
#                   status TEXT DEFAULT "available" CHECK("status" = "available" or "status" = "borrowed"))
#                ''')
#
# con.commit()

# cursor.execute('''CREATE TABLE IF NOT EXISTS readers (
#                   id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   name TEXT NOT NULL,
#                   age INTEGER)
#                ''')
#
# con.commit()

# cursor.execute('''CREATE TABLE IF NOT EXISTS borrowed_books (
#                   reader_id INTEGER,
#                   book_id INTEGER,
#                   borrow_date TEXT,
#                   FOREIGN KEY (reader_id) REFERENCES readers(id),
#                   FOREIGN KEY (book_id) REFERENCES books(id))
#                ''')
#
# con.commit()

# books_lst = [
#     ('Три товарища', 'Ремарк', 1936, 'available'),
#     ('На западном фронте без перемен', 'Ремарк', 1929, 'available'),
#     ('Возвращение', 'Ремарк', 1931, 'available'),
#     ('Старик и море', 'Хемингуэй', 1952, 'available'),
#     ('Прощай, оружие!', 'Хемингуэй', 1929, 'available'),
#     ('По ком звонит колокол', 'Хемингуэй', 1940, 'available'),
#     ('О дивный новый мир', 'Хаксли', 1932, 'available'),
#     ('1984', 'Оруэлл', 1949, 'available'),
#     ('Скотный двор', 'Оруэлл', 1945, 'available'),
#     ('451 градус по Фаренгейту', 'Брэдбери', 1953, 'available'),
#     ('Над пропастью во ржи', 'Сэлинджер', 1951, 'available'),
#     ('Улисс', 'Джойс', 1922, 'available'),
#     ('Великий Гэтсби', 'Фицджеральд', 1925, 'available'),
#     ('Грозовой перевал', 'Бронте', 1847, 'available'),
#     ('Гордость и предубеждение', 'Остин', 1813, 'available'),
#     ('Преступление и наказание', 'Достоевский', 1866, 'available'),
#     ('Идиот', 'Достоевский', 1869, 'available'),
#     ('Война и мир', 'Толстой', 1869, 'available'),
#     ('Анна Каренина', 'Толстой', 1877, 'available'),
#     ('Мастер и Маргарита', 'Булгаков', 1967, 'available'),
#     ('Сто лет одиночества', 'Маркес', 1967, 'available'),
#     ('Чума', 'Камю', 1947, 'available'),
#     ('Посторонний', 'Камю', 1942, 'available'),
#     ('Замок', 'Кафка', 1926, 'available'),
#     ('Процесс', 'Кафка', 1925, 'available'),
#     ('Доктор Фаустус', 'Манн', 1947, 'available'),
#     ('Моби Дик', 'Мелвилл', 1851, 'available'),
#     ('Дракула', 'Стокер', 1897, 'available'),
#     ('Фауст', 'Гёте', 1808, 'available'),
#     ('Имя розы', 'Эко', 1980, 'available')
# ]
#
# query = """
#     INSERT INTO books (title, author, year, status) VALUES (?, ?, ?, ?)"""
#
# cursor.executemany(query, books_lst)
#
# con.commit()

# books_lst = [
#     ('Мы', 'Замятин', 1924),
#     ('Заводной апельсин', 'Бёрджесс', 1962),
#     ('Облачный атлас', 'Митчелл', 2004),
#     ('Голодный дом', 'Митчелл', 2015),
#     ('Сон №9', 'Митчелл', 2001),
#     ('Финансист', 'Драйзер', 1912),
#     ('Титан', 'Драйзер', 1914),
#     ('Стоик', 'Драйзер', 1947),
#     ('Жизнь взаймы', 'Ремарк', 1959),
#     ('Черный обелиск', 'Ремарк', 1956),
#     ('И восходит солнце', 'Хемингуэй', 1926),
#     ('Острова в океане', 'Хемингуэй', 1970),
#     ('Сияние', 'Кинг', 1977),
#     ('Оно', 'Кинг', 1986),
#     ('Американская трагедия', 'Драйзер', 1925),
#     ('Тёмные аллеи', 'Бунин', 1943),
#     ('Братья Карамазовы', 'Достоевский', 1880),
#     ('Подросток', 'Достоевский', 1875),
#     ('Волшебная гора', 'Манн', 1924),
#     ('Триумфальная арка', 'Ремарк', 1945)
# ]
#
# query = """
#     INSERT INTO books (title, author, year) VALUES (?, ?, ?)"""
#
# cursor.executemany(query, books_lst)
#
# con.commit()

# readers_lst = [
#     ('Иванов', 25),
#     ('Петров', 32),
#     ('Сидоров', 41),
#     ('Смирнов', 19),
#     ('Кузнецов', 28),
#     ('Попов', 35),
#     ('Соколов', 22),
#     ('Лебедев', 45),
#     ('Новиков', 30),
#     ('Морозов', 27),
#     ('Волков', 38),
#     ('Соловьёв', 24),
#     ('Васильев', 50),
#     ('Зайцев', 29),
#     ('Павлов', 33),
#     ('Семёнов', 26),
#     ('Голубев', 21),
#     ('Виноградов', 42),
#     ('Богданов', 37),
#     ('Фёдоров', 31)
# ]
#
# query = """
#     INSERT INTO readers (name, age) VALUES (?, ?)"""
#
# cursor.executemany(query, readers_lst)
#
# con.commit()


from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: str
    genre: str

@dataclass
class Reader:
    id: int
    name: str
    age: int

class Library:

    FINE_DAY = 1

    def __init__(self, db_name='sqlite_db/library.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    """Создает таблицы в базе данных, если они еще не существуют"""

    def create_table(self, table_name, values: str):
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({values})'
        self.cursor.execute(query)
        self.conn.commit()

    """Выводит все книги библиотеки"""

    def get_books(self) -> list[Book]:
        query = f"SELECT * FROM books ORDER BY id"
        self.cursor.execute(query)
        books = self.cursor.fetchall()
        return [Book(*item) for item in books]

    """Поиск книг по id, году, названию или автору"""

    def search_books(self):
        book = input("Введите ID или Название книги, или Фамилию автора, или год(0....) для поиска: ")
        if book.isdigit():
            if book[0] == "0":
                book = book[1:]
                query = f"SELECT * FROM books WHERE year = {int(book)}"
                self.cursor.execute(query)
                data = self.cursor.fetchall()
                if data:
                    return [Book(*item) for item in data]
                else:
                    return f'По данному году: {book} ничего не найдено!'
            else:
                query = f"SELECT * FROM books WHERE id = {int(book)}"
                self.cursor.execute(query)
                data = self.cursor.fetchall()
                if data:
                    return [Book(*item) for item in data]
                else:
                    return f'По данному Id: {book} ничего не найдено!'
        else:
            query = f"SELECT * FROM books WHERE title = '{book}' or author = '{book}'"
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            if data:
                return [Book(*item) for item in data]
            else:
                return f'По запросу: {book} ни по названию книги, ни по автору, ничего не найдено!'

    """Добавляет новую книгу в библиотеку"""

    def add_book(self, title, author, year):
        query = f"INSERT INTO books (title, author, year) VALUES (?, ?, ?)"
        self.cursor.execute(query, (title, author, year))
        self.conn.commit()

    """Добавляет новые книги в библиотеку"""

    def add_books(self, books: list):
        query = f"INSERT INTO books (title, author, year) VALUES (?, ?, ?)"
        self.cursor.executemany(query, books)
        self.conn.commit()

    """Выводит всех читателей библиотеки"""

    def get_readers(self) -> list[Reader]:
        self.cursor.execute("SELECT * FROM readers ORDER BY id")
        data = self.cursor.fetchall()
        return [Reader(*item) for item in data]

    """Ищет читателя по фамилии или id в библиотекe"""

    def get_reader(self) -> list[Reader]:
        reader = input("Введите Фамилию или ID для поиска: ")
        if reader.isdigit():
            query = f"SELECT * FROM readers WHERE id = {int(reader)}"
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            if data:
                return [Reader(*item) for item in data]
            else:
                return f'Данные по Id: {reader} не найдены!'
        elif reader.isalpha():
            query = f"SELECT * FROM readers WHERE name = '{reader}'"
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            if data:
                return [Reader(*item) for item in data]
            else:
                return f'Данные по Фамилии: {reader} не найдены!'
        else:
            return f"Ошибка ввода! Попробуйте снова."

    """Добавляет нового читателя"""

    def add_reader(self, name, age):
        query = f"INSERT INTO readers (name, age) VALUES (?, ?)"
        self.cursor.execute(query, (name, age))
        self.conn.commit()

    """Выдает книгу читателю, если она доступна"""

    def borrow_book(self):
        book = input("Введите Название книги: ")
        query = f"SELECT id, status FROM books WHERE title = '{book}'"
        self.cursor.execute(query)
        data1 = self.cursor.fetchall()
        if data1:
            if data1[0][1] == 'available':
                book_id = data1[0][0]
                reader_id = int(input("Введите id читателя: "))
                query = f"SELECT id FROM readers WHERE id = {reader_id}"
                self.cursor.execute(query)
                data2 = self.cursor.fetchall()
                if data2:
                    date_out = datetime.now()
                    due_date = date_out + timedelta(days=30)
                    date_out_str = date_out.strftime("%Y-%m-%d")
                    due_date_str = due_date.strftime("%Y-%m-%d")
                    query_up = f"UPDATE books SET status = 'borrowed' WHERE id = {book_id}"
                    self.cursor.execute(query_up)
                    self.conn.commit()
                    query_ins = """
                             INSERT INTO borrowed_books (reader_id, book_id, borrow_date, return_date)
                              VALUES (?, ?, ?, ?)"""
                    self.cursor.execute(query_ins, (reader_id, book_id, date_out_str, due_date_str))
                    self.conn.commit()
                    print(f'Книга {book} успешно выдана!')
                else:
                    print(f"Читателя с таким Id: {reader_id} в нашей библиотеке нет!")
            else:
                print("Книга взята!")
        else:
            print("Нет такой книги в библиотеке!")

    """Возвращает книгу в библиотеку"""

    def return_book(self):
        book = input("Введите Название возвращаемой книги: ")
        query_status = f"SELECT id, status FROM books WHERE title = ?"
        self.cursor.execute(query_status, (book,))
        data1 = self.cursor.fetchall()
        if data1:
            if data1[0][1] == 'borrowed':
                book_id = data1[0][0]
                query_date = """
                             SELECT return_date 
                             FROM borrowed_books 
                             WHERE book_id = ? 
                               AND actual_return_date IS NULL"""
                self.cursor.execute(query_date, (book_id,))
                result = self.cursor.fetchone()
                if result:
                    due_date_str = result[0]
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                    today = datetime.now()
                    overdue_days = (today - due_date).days
                    if overdue_days > 0:
                        fine_amount = overdue_days * self.FINE_DAY
                        print(f"Книга просрочена на {overdue_days} дней.")
                        print(f"Штраф: {fine_amount}$.")
                    else:
                        print("Книга возвращена вовремя!")
                actual_return = today.strftime("%Y-%m-%d")
                update_query = """
                               UPDATE borrowed_books
                               SET actual_return_date = ?
                               WHERE book_id = ? 
                                 AND actual_return_date IS NULL"""
                self.cursor.execute(update_query, (actual_return, book_id))
                query_up_status = f"UPDATE books SET status = 'available' WHERE id = ?"
                self.cursor.execute(query_up_status , (book_id,))
                self.conn.commit()
                print(f'Книга {book} успешно возвращена!')
            else:
                print(f'Книга {book} уже была возвращена в библиотеку!')
        else:
            print(f'Книги с таким названием {book} не было в нашей библиотеке!')

    """Выводит список всех выданных книг"""

    def get_borrowed_books(self):
        query = f"SELECT * FROM books WHERE status = 'borrowed'"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        borrowed_books = []
        if data:
            for elem in data:
                borrowed_books.append(elem)
        else:
            print("Нет заимствованных книг!")
        print(borrowed_books)


    """Показывает количество доступных и занятых книг"""

    def get_statistics(self):
        query1 = f"SELECT count(status) FROM books WHERE status = 'borrowed'"
        self.cursor.execute(query1)
        data1 = self.cursor.fetchall()
        query2 = f"SELECT count(status) FROM books WHERE status = 'available'"
        self.cursor.execute(query2)
        data2 = self.cursor.fetchall()
        print(f"Заимствованных книг: {data1[0][0]}, Доступных книг: {data2[0][0]}")

    """Поиск по id или фамилии читателя списка книг и дату выдачи книг"""

    def get_lst_name_bb(self) -> list:
        reader = input("Введите Фамилию или ID для поиска: ")
        if reader.isdigit():
            query = (f"SELECT * FROM readers "
                     f"JOIN borrowed_books ON readers.id = borrowed_books.reader_id "
                     f"JOIN books ON borrowed_books.book_id = books.id "
                     f"WHERE readers.id = {int(reader)} AND borrowed_books.actual_return_date IS NULL")
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            if data:
                for elem in data:
                    print(f'Название книги: {elem[9]}, Автор: {elem[10]}, Дата выдачи: {elem[5]}, '
                          f'Дата для возврата: {elem[6]}')
            else:
                print(f'Данные по Id: {reader} не найдены!')
        elif reader.isalpha():
            query = (f"SELECT * FROM readers "
                     f"JOIN borrowed_books ON readers.id = borrowed_books.reader_id "
                     f"JOIN books ON borrowed_books.book_id = books.id "
                     f"WHERE readers.name = '{reader}'")
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            if data:
                for elem in data:
                    print(f'Название книги: {elem[7]}, Автор: {elem[8]}, Дата выдачи: {elem[5]}')
            else:
                print(f'Данные по Фамилии: {reader} не найдены!')
        else:
            print(f"Ошибка ввода! Попробуйте снова.")

    """Выводит все книги библиотеки с сортировкой на выбор"""

    def get_books_sort(self):
        sort = input("Укажите по какому параметру отсортировать: автор - 1, год - 2, статус - 3: ")
        if sort == '1':
            s = "author"
        elif sort == '2':
            s = "year"
        elif sort == '3':
            s = "status"
        else:
            s = 'id'
        query = f"SELECT * FROM books ORDER BY {s}"
        self.cursor.execute(query)
        books = self.cursor.fetchall()
        for elem in books:
            print(elem)

    """Создает в указанной таблице колонку с параметрами"""

    def _add_column(self, name_table:str, name_column:str):
        query = f"ALTER TABLE {name_table} ADD {name_column}"
        self.cursor.execute(query)
        self.conn.commit()

    """Продлевает книгу еще на 30 дней"""

    def extension_book(self):
        book = input("Введите Название продлеваемой книги: ")
        query_status = f"SELECT id, status FROM books WHERE title = ?"
        self.cursor.execute(query_status, (book,))
        data = self.cursor.fetchall()
        if data:
            if data[0][1] == 'borrowed':
                book_id = data[0][0]
                query_date = """
                             SELECT return_date 
                             FROM borrowed_books 
                             WHERE book_id = ? 
                               AND actual_return_date IS NULL"""
                self.cursor.execute(query_date, (book_id,))
                result = self.cursor.fetchone()
                due_date_str = result[0]
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                due_date = due_date + timedelta(days=30)
                due_date_str = due_date.strftime("%Y-%m-%d")
                query_update = f"UPDATE borrowed_books  SET return_date = ? WHERE book_id = ?"
                self.cursor.execute(query_update, (due_date_str, book_id))
                self.conn.commit()
                print(f"Книга успешно продлена, новая дата возврата: {due_date_str}")

    """Обновление жанров книг"""

    def _update_genres(self, genres):
        query_upgenre = "UPDATE books SET genre = ? WHERE title = ?"
        for title, genre in genres.items():
            self.cursor.execute(query_upgenre, (genre, title))
        self.conn.commit()
        print("Жанры успешно обновлены!")



my_library = Library()

# запрос списка всех читателей библиотеки
# list_readers = my_library.get_readers()
# print(list_readers)

# запрос читателя по фамилии или ID
# reader = my_library.get_reader()
# print(reader)

# запрос списка всех книг библиотеки
# list_books = my_library.get_books()
# print(list_books)
#
# for book in list_books:
#     print(book)

# запрос книги по id, Названию, Фамилии автора или году
# search_book = my_library.search_books()
# print(search_book)


# добавляем нового читателя
# my_library.add_reader(name="Федорова", age=22)

# добавляем новую книгу
# my_library.add_book('Театр', 'Моэм', 1937)

# добавляем несколько новых книг
# books = [
#     ('Повелитель мух', 'Голдинг', 1954),
#     ('Убить пересмешника', 'Ли', 1960),
#     ('Над кукушкиным гнездом', 'Кизи', 1962),
#     ('Алхимик', 'Коэльо', 1988)
# ]
# my_library.add_books(books)

# создание новой таблицы
# my_library.create_table(
#     table_name="librarians",
#     values="id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER")

# Поиск по id или фамилии читателя списка книг и дату выдачи книг
# my_library.get_lst_name_bb()

# запрос всех книг библиотеки с сортировкой на выбор
# my_library.get_books_sort()

# вставка новой колонки в таблицу
# my_library._add_column(name_table='borrowed_books', name_column='return_date TEXT')

#вставка новой колонки в таблицу
# my_library._add_column(name_table='borrowed_books', name_column='actual_return_date TEXT DEFAULT NULL')

# Поиск по id или фамилии читателя списка книг и дату выдачи книг
# my_library.get_lst_name_bb()

# запрос количества занятых и свободных книг
# my_library.get_statistics()

# запрос заимствованных книг
# my_library.get_borrowed_books()

# выдача книги читателю, книга выдается сроком на 30 дней
# my_library.borrow_book()

# возврат книги читателем, с проверкой просрочки и начислением штрафа, в случае просрочки
# my_library.return_book()

# продление книги ещё на 30 дней
# my_library.extension_book()

#вставка новой колонки в таблицу
# my_library._add_column(name_table='books', name_column='genre TEXT DEFAULT NULL')

# обновление жанров книг
genres = {
        "Три товарища": "war",
        "На западном фронте без перемен": "war",
        "Возвращение": "war",
        "Триумфальная арка": "war",
        "Прощай, оружие!": "war",
        "По ком звонит колокол": "war",
        "О дивный новый мир": "dystopia",
        "1984": "dystopia",
        "Скотный двор": "dystopia",
        "451 градус по Фаренгейту": "dystopia",
        "Мы": "dystopia",
        "Заводной апельсин": "dystopia",
        "Повелитель мух": "dystopia",
        "Чума": "philosophical",
        "Посторонний": "philosophical",
        "Замок": "philosophical",
        "Процесс": "philosophical",
        "Доктор Фаустус": "philosophical",
        "Волшебная гора": "philosophical",
        "Фауст": "philosophical",
        "Алхимик": "philosophical",
        "Преступление и наказание": "classic",
        "Идиот": "classic",
        "Братья Карамазовы": "classic",
        "Подросток": "classic",
        "Война и мир": "classic",
        "Анна Каренина": "classic",
        "Над пропастью во ржи": "classic",
        "Улисс": "classic",
        "Великий Гэтсби": "classic",
        "Грозовой перевал": "classic",
        "Гордость и предубеждение": "classic",
        "Моби Дик": "classic",
        "Дракула": "classic",
        "Мастер и Маргарита": "fiction",
        "Сто лет одиночества": "fiction",
        "Облачный атлас": "fiction",
        "Голодный дом": "fiction",
        "Сон №9": "fiction",
        "Финансист": "fiction",
        "Титан": "fiction",
        "Стоик": "fiction",
        "Американская трагедия": "fiction",
        "Сияние": "fiction",
        "Оно": "fiction",
        "Имя розы": "fiction",
        "Театр": "fiction",
        "Убить пересмешника": "fiction",
        "Над кукушкиным гнездом": "fiction",
        "Старик и море": "fiction",
        "И восходит солнце": "fiction",
        "Острова в океане": "fiction",
        "Жизнь взаймы": "fiction",
        "Черный обелиск": "fiction",
        "Тёмные аллеи": "fiction",
    }
# my_library._update_genres(genres)