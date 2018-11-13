from flask import Flask
from flask import render_template
from flask import request
import bookDB

app = Flask(__name__)
db = bookDB.bookDB("mylib")
#addBook(self, author, title, year)


@app.route('/')
def hello_world():
    count = len(db.listAllBooks())
    return render_template("mainPage.html", count_books=count)


# ! ADD BOOK
@app.route('/addBooksForm')
def add_Book_Form():
    return render_template("addBookTemplate.html")

@app.route('/addBook', methods=['POST', 'GET'])
def add_Book():
    if request.method == "GET":
        db.addBook(request.args['Author'], request.args['Title'], int(request.args['Year']))
        return str('Added to the database using GET')
    else:
        db.addBook(request.form['Author'], request.form['Title'], int(request.form['Year']))
        return str('Added to the database using POST')
    return render_template("addBookTemplate.html")


# ! SHOW BOOK
@app.route('/showBookForm')
def show_Book_Form():
    return render_template("showBook.html")

@app.route('/showBook', methods=['POST', 'GET'])
def show_Book():
    if request.method == 'GET':
        book = db.showBook(int(request.args['id']))
        return str(book.author)
    return render_template("showBook.html")



# ! LIST ALL BOOKS
@app.route('/listAllBooksForm')
def list_AllBooks_Form():
    return render_template("listAllBooksForm.html")

@app.route('/listAllBooks')
def listAllBooksForm():
    info = []
    book_list = db.listAllBooks()
    for n_book in book_list:
        aux = [str(n_book.author), str(n_book.title), str(n_book.year), str(n_book.id)]
        info.append(aux)
    return render_template("listAllBooksForm.html", info=info)



# ! LIST BOOKS BY YEAR
@app.route('/listBooksYear')
def list_BooksYear_Form():
    return render_template("listBooksYear.html")

@app.route('/listBooksYear_new', methods=['GET'])
def list_BooksYear():
    if request.method == 'GET':
        book_list=db.listBooksYear(int(request.args['year']))
    return render_template("listBooksYear.html", book_list=book_list)

    
if __name__ == '__main__':
    app.run()
