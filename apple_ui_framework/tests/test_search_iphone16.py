from pages.home_page import HomePage
from pages.search_page import SearchPage


def test_search_iphone_16_opens_expected_result(page):
    # Note: the original script navigated via Google first; here we go directly to Apple using the HomePage object.
    home_page = HomePage(page)
    home_page.open_home_page()
    home_page.verify_home_page_loaded()

    # Use the HomePage search to look for "iphone 16"
    home_page.search_for_product("iphone 16")

    # On the Search results page, open the first result that matches the expected link text
    search_page = SearchPage(page)
    search_page.verify_search_url()
    search_page.verify_results_are_displayed()
    search_page.open_first_result_matching("iPhone 16 Case with MagSafe")
