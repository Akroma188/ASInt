
import bookDB
import book

class dbUI:

    def __init__(self):
        self.db = bookDB.bookDB()
        print('Welcome to te Book Database V1.0 \n')
        

    
    def insert_b(self):
        print('You chose to insert a new book! \n')
        author = input('Name of the author?')
        title = input('Title of the book?')
        pb_year = input('Publication year of the book?')
        ident = input('ID of the book?')
        new_book = book.Book(author, title, pb_year, ident)
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
        print('1 -> New Book | 2 -> Show book | 3 -> Show Authors | 4 -> Books from Author | 5 -> Books from Year | 0 -> Exit \n')

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