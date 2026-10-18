name = input("enter your name: ")
print("welcome,", name)
number_of_books = int(input("how many books do you want to add? "))
books = []
for i in range(number_of_books):
    book = input("enter the name of a book: ")
    books.append(book)

print("your books are:")

for book in books:
    print(book)