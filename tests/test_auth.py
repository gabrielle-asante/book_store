from app import app
from lib.database_connection import DatabaseConnection

from playwright.sync_api import Page, expect

def test_auth_integration():
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users")
    connection.execute("INSERT INTO users(email, username, password) VALUES('testing@example.com', 'testauth', 'testauth1234');")

    response = client.post("/sessions", data={
        "email": "testing@example.com",
        "username":"testauth",
        "password": "testauth1234"
    } )

    assert response.status_code == 302

    assert response.headers['Location'].endswith('/books')

# Playwright test for logging in:

# Acting like a user 
# A user needs to first put their email, username and password and becausdr this needs 
# needs to be a user that exists we need to insert this user to the databasde and truncate.
# And then after the user logs in they should be redirected back to the /books page 

def test_user_can_login(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE table users")
    connection.execute("INSERT INTO users (email, username, password) VALUES('test_user_can_login@example.com', 'testusercanlogin', 'testuserlogin123')")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_placeholder("Email").fill('test_user_can_login@example.com')
    page.get_by_placeholder("Username").fill('testusercanlogin')
    page.get_by_placeholder("Password").fill('testuserlogin123')
    page.get_by_role("button").click()

    assert page.url== 'http://localhost:5001/books'

    
    

