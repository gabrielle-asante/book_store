from playwright.sync_api import Page, expect 

def test_page_displays_all_films(page: Page):
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
