
class Library:
    
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        if title in self.books:
            print("Book already exists")
        else:
            self.books.append({'title': title, 'author': author, 'available': True})

    def borrow_book(self, title):
        for book in self.books:
            if book['title'] == title:
                book['available'] = False
                print(f"You borrowed: {title}. ")
                return
        print("Book not found")

    def return_book(self, title):
        for book in self.books:
            if book['title'] == title:
                book['available'] = True
                print(f'Book returned: {title}')
                return
        print('Book not found. ')
   


    def get_catalog(self):
        for book in self.books:
            print(f"{book['title']} | {book['author']} | 'available' {book['available']}")
            print("--------------------------------------------------------------")
    
l1 = Library('City Library')
l1.add_book("1984","Orwell")
l1.add_book("Dune", "Hebert")
l1.get_catalog()
l1.borrow_book("1984")
l1.get_catalog()
l1.return_book("1984")
l1.get_catalog()