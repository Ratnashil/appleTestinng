from pages.home_page import HomePage


def test_google_to_apple_tv_flow(page):
    home_page = HomePage(page)

    # Open Apple homepage (replaces explicit Google and Apple navigations)
    home_page.open_home_page()

    # Navigate to Apple TV section
    home_page.open_apple_tv_page()
