from actions import *


class Book:
    def __init__(self, id, title, author, year, status):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __repr__(self):
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {self.status}"


class Library:
    def __init__(self, books):
        self.books = books

    def run(self):
        while True:
            print("Библиотека книг. Выберите действие:")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Поиск книг")
            print("4. Отобразить все книги")
            print("5. Изменить статус книги")
            print("6. Выход")

            choice = input()
            match choice:
                case "1":
                    title = input("Введите название книги: ")
                    author = input("Введите автора книги: ")
                    year = int(input("Введите год издания: "))
                    add_book(self.books, title, author, year)
                case "2":
                    id = int(input("Введите ID книги для удаления: "))
                    remove_book(self.books, id)
                case "3":
                    query = input("Введите запрос для поиска: ")
                    search_books(self.books, query)
                case "4":
                    display_all_books(self.books)
                case "5":
                    id = int(input("Введите ID книги для изменения статуса: "))
                    new_status = input("Введите новый статус (в наличии/выдана): ")
                    change_book_status(self.books, id, new_status)
                case "6":
                    return
                case _:
                    print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    library = Library(books)
    library.run()
