import pickle


class Book:

    def __init__(self, author, title, pb_year, identifier):
        self.author = author
        self.title = title
        self.pb_year = pb_year
        self.identifier = identifier


class bookDB:

    def __init__(self):
        self.database = []
        filename = 'backup.p'
        self.file = open(filename, 'wb')

    def insert_book(self, book):
        self.database.append(book)
        pickle.dump(book, self.file)
        print('book in database success')

    def show_book(self, identifier):
        for book in self.database:
            if book.identifier == identifier:
                print('Selected Book: \n' + 'Title: ' + book.title + '\n' +
                      'Author: ' + book.author + '\n'+  'Publication Year: ' + book.pb_year + '\n' + 'Identifier: ' + book.identifier + '\n')
                found = True
        if not found:
            print('\n There is no book with that ID.')

    def list_all_authors(self):
        authors = []
        if len(self.database) != 0:
            for book in self.database:
                authors.append(book.author)
                for author in authors[:-1]:
                    if book.author == author:
                        found = True
                if found == True:
                    authors.pop()
            print('Authors Found: \n')
            for person in authors:
                print(person + '\n')
        else:
            print('There are no books in the Database \n')       

    def list_by_author(self, author):
        if len(self.database) != 0:
            print('Books From: ' + author + '\n')
            for book in self.database:
                if book.author == author:
                    print(book.title)
                    found = True
            if not found:
                print('\n There is no book by that author.')
        else:
            print('There are no books in the Database \n')


    def list_by_year(self, year):
        if len(self.database) != 0:
            print('Books From Year: ' + year + '\n')
            for book in self.database:
                if book.year == year:
                    print(book.title)
                    found = True
            if not found:
                print('\n There is no book from that year.')
        else:
            print('There are no books in the Database \n')

class dbUI:

    def __init__(self):
        self.db = bookDB()
        print('Welcome to te Book Database V1.0 \n')
        

    
    def insert_b(self):
        print('You chose to insert a new book! \n')
        author = input('Name of the author?')
        title = input('Title of the book?')
        pb_year = input('Publication year of the book?')
        id = input('ID of the book?')
        new_book = Book(author, title, pb_year, id)
        self.db.insert_book(new_book)
        print('Book added to the database sucessfully!')

    def show(self):
        identifier = input('Enter the ID of the book you want to see: \n')
        self.db.show_book(identifier)

    def list_all_A(self):
        self.db.list_all_authors()

    def list_by_A(self):
        author = input('Which author do you wish to see the books from? \n')
        self.db.list_by_author(author)

    def list_by_Y(self):
        year = input('From what year do you wish to see the books from? \n')
        self.db.list_by_year(year)

    def user_input(self):
        print('\n This Interface Works by pressing the number keys from 1 to 5 and following text \n')
        print('1 -> New Book | 2 -> Show book | 3 -> Show Authors | 4 -> Books from Author | 5 -> Books from Year \n')

        pressed_key = input('\n What do you want to do? \n')
        
        while pressed_key != '1' and pressed_key != '2' and pressed_key != '3' and pressed_key != '4' and pressed_key != '5' and pressed_key != '0':
            pressed_key = input('Not Valid! What do you want to do?')

        if pressed_key == '1':
            self.insert_b()
        if pressed_key == '2':
            self.show()
        if pressed_key == '3':
            self.list_all_A()
        if pressed_key == '4':
            self.list_by_A()
        if pressed_key == '5':
            self.list_by_Y()
        if pressed_key == '0':
            return True
        return False

def main():
    interface = dbUI()

    while not interface.user_input() :
        pass

if __name__ == "__main__":
    main()