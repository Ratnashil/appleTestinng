from pages.home_page import HomePage
from pages.search_page import SearchPage


def test_recorded_flow(page):
    home_page = HomePage(page)
    search_page = SearchPage(page)

    # Step 1: Navigate to Google
    home_page.open_external_url("https://www.google.com/")

    # Step 2: Navigate to Apple
    home_page.open_external_url("https://www.apple.com/")

    # Step 3 & 4: Search for "apple 16" on apple.com and land on search results
    home_page.search_for_product_and_wait("apple 16")

    # Step 5: Click the first visible link containing 'specs' in the search results
    search_page.open_first_specs_result()
