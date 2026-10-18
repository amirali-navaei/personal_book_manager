import json
def display_books(books):
    print("your books are:")
    for book in books:
        print(book)
def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file)
def load_books():
    try:
        with open("books.json", "r") as file:
            books = json.load(file)
            return books

    except FileNotFoundError:
        return []
