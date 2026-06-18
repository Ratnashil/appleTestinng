from pages.home_page import HomePage
from pages.iphone_page import IPhonePage
from pages.mac_page import MacPage
from pages.search_page import SearchPage
from pages.store_page import StorePage


def test_recorded_flow(page):
    # The original script opens Google first, then Apple, and brings the page to front after each navigation.
    # In pytest-playwright, the 'page' fixture provides the Page instance; we replicate the same sequence.
    page.goto("https://www.google.com/", wait_until="domcontentloaded")
    page.bring_to_front()
    page.goto("https://www.apple.com/", wait_until="domcontentloaded")
    page.bring_to_front()