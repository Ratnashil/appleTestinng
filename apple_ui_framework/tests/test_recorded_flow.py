from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.search_page import SearchPage


def test_recorded_flow(page):
    base_page = BasePage(page)
    home_page = HomePage(page)
    search_page = SearchPage(page)

    # Step 1: Navigate to Google homepage
    base_page.open_url("https://www.google.com/")
    base_page.bring_to_front()

    # Step 2: Navigate to Apple homepage
    home_page.open_home_page()
    base_page.bring_to_front()

    # Step 3: Click the 'Continue' button on the Apple website
    home_page.handle_continue_button()

    # Step 4: Fill the 'Search apple.com' field with 'iphone 17'
    home_page.search_for_product_without_submit("iphone 17")
    )
    base_page.bring_to_front()
