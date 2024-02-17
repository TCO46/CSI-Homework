class Book:
    def inseft_book(self):
        self.ID = int(input('Enter book ID: '))
        self.name = input('Enter book name: ')
        self.publisher = input('Enter book publisher: ')
        self.price = int(input('Enter book price: '))

    def book_info(self):
        return {
            'ID': self.ID,
            'name': self.name,
            'publisher': self.publisher,
            'price': self.price
        }


amount_of_books = int(input('Enter amount of books: '))
books = []

for i in range(amount_of_books):
    book = Book()
    print(f"----------Book {i + 1}----------")
    book.inseft_book()
    books.append(book.book_info())

print(books)
