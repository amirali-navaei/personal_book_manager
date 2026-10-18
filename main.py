import os
from dotenv import load_dotenv
from books import display_books, save_books, load_books

load_dotenv()

admin_password = os.getenv("BOOK_MANAGER_ADMIN_PASSWORD")

name = input("Enter your name: ")

print("Welcome,", name)

admin_choice = input("Do you want to enter Admin Mode? (yes/no): ")

if admin_choice.lower() == "yes":
    password = input("Enter Admin Password: ")

    if admin_password is None:
        print("Admin password is not configured.")
    elif password == admin_password:
        print("aadmin Mode activated successfully.")
    else:
        print("Incorrect Admin Password.")

books = load_books()

display_books(books)

number_of_books = int(input("how many books do you want to add? "))

for i in range(number_of_books):
    book = input("enter the name of a book: ")
    books.append(book)

save_books(books)

display_books(books)