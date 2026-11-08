import json
def display_books(books):
    print("\n===== Your Book List =====")

    for book in books:
        if isinstance(book, dict):
            print(f"Book Name: {book['name']}")
            print(f"Priority Level: {book['priority']}")
            print("--------------------")
        else:
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
