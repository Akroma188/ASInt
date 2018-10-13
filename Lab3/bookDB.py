import pickle
import os

class bookDB:

    def __init__(self):
        self.database = []
        self.filename = 'backup.pkl'
        if os.path.isfile(self.filename) is True:
            self.file = open(self.filename, 'rb')
            self.database = pickle.load(self.file)
            self.file.close()
            print('Files were backed up. \n')
        else:
            self.database = []
            print('there was no backup file \n')
            
        
        

    def insert_book(self, book):
        self.database.append(book)
        self.file = open(self.filename, 'wb')
        pickle.dump(self.database, self.file)
        self.file.close()
        print('book in database success')

    def show_book(self, identifier):
        print(type(self.database))
        print(self.database)
        found = False
        for book in self.database:
            if book.identifier == identifier:
                print('Selected Book: \n' + 'Title: ' + book.title + '\n' +
                      'Author: ' + book.author + '\n'+  'Publication Year: ' + book.pb_year + '\n' + 'Identifier: ' + book.identifier + '\n')
                found = True
        if not found:
            print('\n There is no book with that ID.')

    def list_all_authors(self):
        authors = []
        found=False
        if len(self.database) != 0:
            for book in self.database:
                authors.append(book.author)
                for author in authors[:-1]:
                    if book.author == author:
                        found = True
                if found == True:
                    authors.pop()
                    found = False
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