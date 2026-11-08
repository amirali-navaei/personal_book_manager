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
    book_name = input("Enter the name of a book: ")

    priority = input("Enter priority (low/medium/high): ").lower()

    while priority not in ["low", "medium", "high"]:
        print("Invalid priority. Please try again.")
        priority = input("Enter priority (low/medium/high): ").lower()

    book = {
        "name": book_name,
        "priority": priority
    }

    books.append(book)

save_books(books)

display_books(books)