from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

def test_list_of_all_books(page: Page):

    # 1. Reset the database:
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")

    # 2. Open the books webpage:

    page.goto('http://127.0.0.1:5001/books')

    # 3. Find all the books displayed

    books = page.locator("li")
    actual_books = books.all_inner_texts()

    #  4. Define the expected books

    expected_books = [
        'The Gruffalo by Julia Donaldson',
        'Ada Twist, Scientist by Andrea Beaty',
        'The Girl Who Drank the Moon by Kelly Barnhill',
        'Dragons in a Bag by Zetta Elliott'
    ]


    # 5. Compare the results

    assert actual_books == expected_books

# def test_user_can_create_a_new_book(page: Page):
#         connection = DatabaseConnection()
#         connection.connect()
#         connection.seed("./seeds/books.sql")
        
#         page.goto("http://localhost:5001/books")
#         page.get_by_placeholder("Title").fill("Charlie and the Chocolate Factory")
#         page.get_by_placeholder("Author").fill("Roald Dahl")
#         page.get_by_role("button", name="Submit").click()
#         books = page.locator('li')
#         new_book = books.all_inner_texts()[-1]
#         assert new_book == "Charlie and the Chocolate Factory by Roald Dahl"

# This test is for a logged in user - testing when we added the decorator stuff if that works.

def test_create_new_book(page: Page):

    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_placeholder("Email").fill("test@test.com")
    page.get_by_placeholder("Username").fill("test")
    page.get_by_placeholder("Password").fill("1234")
    page.get_by_role("button").click()

    page.goto("http://localhost:5001/books")
    page.get_by_placeholder("Title").fill("The Chroicles of Geronimo (the cat)")
    page.get_by_placeholder("Author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The Chroicles of Geronimo (the cat) by Geronimo"