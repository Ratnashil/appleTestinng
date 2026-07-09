from pages.home_page import HomePage
from pages.store_page import StorePage


def test_recorded_flow(page, create_allure_artifact_dirs):
    home_page = HomePage(page)
    store_page = StorePage(page)

    # Navigate to Google as in the original script
    home_page.open_google_homepage()

    # Navigate directly to Apple homepage
    home_page.open_home_page()

    # The following bring_to_front calls are omitted because the single-page
    # pytest-playwright fixture already focuses the active page.

    # Click on Shopping Bag button using the same locator and force option
    home_page.open_shopping_bag()

    # Click on "Your Saves" link using the same locator and force option
    home_page.open_your_saves()
