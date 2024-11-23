import json


def add_book(books, title, author, year):
    """
    Добавляет новую книгу в библиотеку.
    :param books: Список книг
    :param title: Название книги
    :param author: Автор книги
    :param year: Год издания
    """

    new_id = len(books) + 1 if not books else max(book['id'] for book in books) + 1
    new_book = {'id': new_id, 'title': title, 'author': author, 'year': year, 'status': 'в наличии'}
    books.append(new_book)
    save_books_to_json(books)


def remove_book(books, id):
    """
    Удаляет книгу из библиотеки по ID.
    :param books: Список книг
    :param id: ID книги для удаления
    """

    for book in books:
        if book['id'] == id:
            books.remove(book)
            save_books_to_json(books)
            return
    print("Книга с таким ID не найдена.")


def search_books(books, query):
    """
    Ищет книги по названию, автору или году.
    :param books: Список книг
    :param query: Запрос для поиска
    """

    results = [book for book in books if
               query.lower() in book['title'].lower() or query.lower() in book['author'].lower() or str(
                   book['year']) == query]
    for book in results:
        print(book)


def display_all_books(books):
    """
    Отображает все книги в библиотеке.
    :param books: Список книг
    """

    for book in books:
        print(book)


def change_book_status(books, id, new_status):
    """
    Изменяет статус книги по ID.
    :param books: Список книг
    :param id: ID книги для изменения статуса
    :param new_status: Новый статус книги
    """

    for book in books:
        if book['id'] == id:
            book['status'] = new_status
            save_books_to_json(books)
            return
    print("Книга с таким ID не найдена.")


def save_books_to_json(books):
    """
    Сохраняет книгу в JSON
    """

    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)


def load_books_from_json():
    """
    Загружает книгу в JSON
    """

    try:
        with open('books.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


books = load_books_from_json()
