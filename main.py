from books import display_books, save_books, load_books

name = input("enter your name: ")

print("welcome,", name)

books = load_books()

display_books(books)

number_of_books = int(input("how many books do you want to add? "))

for i in range(number_of_books):
    book = input("enter the name of a book: ")
    books.append(book)

save_books(books)

display_books(books)
