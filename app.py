from flask import Flask, render_template, request, redirect, session
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book

from lib.film_repository import FilmRepository

from lib.user_repository import UserRepository
from lib.user import User

from login_required import login_required

# instantiate a Flask app object
app = Flask(__name__)

app.secret_key = "some_really_secret_key"


# NEW PART START

# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"


@app.route('/simple-books', methods=['GET']) 
def get_books():
    return [
    {
    "title": "The Gruffalo",
    "author": "Julia Donaldson"
    },
    {
    "title": "Ada Twist, Scientist",
    "author": "Andrea Beaty"
    },
    {
    "title": "The Girl Who Drank the Moon",
    "author": "Kelly Barnhill"
    },
    {
    "title": "Dragons in a Bag",
    "author": "Zetta Elliott"
    }
    ]

# NEW PART END
@app.route('/authors', methods= ['GET'])
def get_authors():
    return [
        {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
    },
    {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
    },
    {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
    },
    {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
    }
]

@app.route('/quotes', methods=['GET'])
def get_quotes():
    quotes = [
    {"quote": "You can never get a cup of tea large enough or a book long enough to suit me.", "author": "C.S. Lewis"},
    {"quote": "Never trust anyone who has not brought a book with them.", "author": "Lemony Snicket, Horseradish: Bitter Truths You Can't Avoid"},
    {"quote": "We read to know we're not alone.", "author": "William Nicholson, Shadowlands: A Play"},
    {"quote": "Sometimes, you read a book and it fills you with this weird evangelical zeal, and you become convinced that the shattered world will never be put back together unless and until all living humans read the book.", "author": "John Green, The Fault in Our Stars"},
    {"quote": "If one cannot enjoy reading a book over and over again, there is no use in reading it at all.", "author": "Oscar Wilde"}
    ]
    return quotes

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")



@app.route('/books', methods=['GET'])
def books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    print(books)
    return render_template("books.html", books= books)



@app.route('/books', methods=['POST'])
@login_required
def create_new_book():
    
    connection = DatabaseConnection()
    connection.connect()

    book_repository = BookRepository(connection)
    
    book_details = request.form
    
    book= Book(title = book_details['title'], author = book_details['author'])

    book_repository.create(book)
    
    return redirect("/books")

@app.route('/films', methods=['GET'])
def get_all_films():
    connection = DatabaseConnection()
    connection.connect()

    film_repository = FilmRepository(connection)
    films = film_repository.all()

    return render_template("films.html", films= films)

@app.route("/users/new", methods=['GET'])
def get_sign_up_page():
    return render_template("signup_form.html")


@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    user = User(email= user_details["email"], username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect("/books")


@app.route('/sessions/new', methods=['GET'])
def get_login_page():
    return render_template("login_form.html")


@app.route('/sessions', methods=['POST'])
def create_session():
    connection = DatabaseConnection()
    connection.connect()

    user_repository = UserRepository(connection)

    username = request.form['username']
    password = request.form['password']

    user = user_repository.find_by_username(username) 

    if user and user.password == password:
        session['user_id'] = user.id 
        session["username"] = user.username
        return redirect("/books")
    else:
        return redirect("/sessions/new")


# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=5001, debug=True)


