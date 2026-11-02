import sys
import os

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_get_books_returns_a_200():
    client = app.test_client()

    response = client.get('/books')

    assert response.status_code == 200

def test_get_books_returns_all_the_books():
    client = app.test_client()
    
    response = client.get('/simple-books')

    assert response.json == [

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

def test_get_authors_returns_status_code_200():
    client = app.test_client()

    response = client.get('/authors')

    assert response.status_code == 200

def test_get_authors_returns_all_the_authors():
    client = app.test_client()
    
    response = client.get('/authors')

    assert response.json == [
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

def test_get_all_quotes():

    client = app.test_client()

    response = client.get("/quotes")

    assert response.json == [
        {"quote": "You can never get a cup of tea large enough or a book long enough to suit me.", 
        "author": "C.S. Lewis"}, 
        {"quote": "Never trust anyone who has not brought a book with them.", 
        "author": "Lemony Snicket, Horseradish: Bitter Truths You Can't Avoid"},
        {"quote": "We read to know we're not alone.", 
        "author": "William Nicholson, Shadowlands: A Play"},
        {"quote": "Sometimes, you read a book and it fills you with this weird evangelical zeal, and you become convinced that the shattered world will never be put back together unless and until all living humans read the book.", 
        "author": "John Green, The Fault in Our Stars"},
        {"quote": "If one cannot enjoy reading a book over and over again, there is no use in reading it at all.", 
        "author": "Oscar Wilde"}
        ]

def test_get_all_quotes_returns_200():
    client = app.test_client()
    response = client.get("/quotes")
    assert response.status_code == 200

def test_get_films_returns_200():
    client = app.test_client()
    response = client.get('/films')
    assert response.status_code == 200