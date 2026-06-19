from pages.home_page import HomePage


def test_recorded_flow(page):
    home_page = HomePage(page)

    # Open Apple homepage (BASE_URL is handled by framework/Playwright config)
    home_page.open_home_page()
    home_page.verify_home_page_loaded()

    # Use the search input and fill it with "iphone1" (no submit/enter to match script)
    home_page.open_search()
    search_input = home_page.search_input()
    search_input.fill("iphone1")
