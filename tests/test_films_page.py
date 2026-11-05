from playwright.sync_api import Page, expect 
from lib.database_connection import DatabaseConnection

def test_page_displays_all_films(page: Page):

    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")

    page.goto("http://localhost:5001/films")

    films = page.locator("li")

    expected_films = [
        'Avatar - 2009',
        'Avengers: Endgame - 2019',
        'Spider-Man: Brand New Day - 2026',
        'Avatar: The Way of Water - 2022',
        'Titanic - 1997'
    ]

    actual_films = films.all_inner_texts()

    assert actual_films == expected_films
