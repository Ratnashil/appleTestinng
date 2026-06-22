from pages.home_page import HomePage


def test_recorded_flow(page):
    home_page = HomePage(page)
    home_page.open_external_page("https://www.google.com/")
    home_page.open_external_page("https://www.apple.com/")
    home_page.dismiss_continue_modal()
