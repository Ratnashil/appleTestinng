from pages.home_page import HomePage
from pages.iphone_page import IPhonePage
from pages.mac_page import MacPage
from pages.search_page import SearchPage
from pages.store_page import StorePage


def test_recorded_flow(page):
    home_page = HomePage(page)

    # Navigate to Google
    home_page.open_url("https://www.google.com/", wait_until="domcontentloaded")
    page.bring_to_front()

    # Navigate to Apple
    home_page.open_url("https://www.apple.com/", wait_until="domcontentloaded")
    page.bring_to_front()

    # Click the "Continue" button using the same chained locators
    page.get_by_role("button", name="Continue", exact=True).or_(
        page.get_by_text("Continue", exact=False)
    ).or_(
        page.locator("#ac-ls-continue")
    ).or_(
        page.locator("a[role=\"button\"]")
    ).or_(
        page.locator("a[href=\"https://www.apple.com/in/\"]")
    ).or_(
        page.locator("a#ac-ls-continue")
    ).first.click(force=True)