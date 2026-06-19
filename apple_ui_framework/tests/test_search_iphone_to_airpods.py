from pages.home_page import HomePage
from pages.iphone_page import IPhonePage
from pages.mac_page import MacPage
from pages.search_page import SearchPage
from pages.store_page import StorePage


def test_recorded_flow(page):
    home_page = HomePage(page)
    iphone_page = IPhonePage(page)
    mac_page = MacPage(page)
    search_page = SearchPage(page)
    store_page = StorePage(page)

    page.goto("https://www.google.com/", wait_until='domcontentloaded')
    page.goto("https://www.apple.com/", wait_until='domcontentloaded')
    page.bring_to_front()
    page.get_by_role("button", name="Close country or region selector", exact=True).or_(
        page.get_by_text("Close country or region selector", exact=False)
    ).or_(
        page.get_by_label("Close country or region selector", exact=True)
    ).or_(
        page.locator("#ac-ls-close")
    ).or_(
        page.locator("button#ac-ls-close")
    ).first.click(force=True)
    page.get_by_label("Search apple.com", exact=True).or_(
        page.get_by_placeholder("Search apple.com")
    ).or_(
        page.locator("div > div > form > div:nth-of-type(1) > input:nth-of-type(1)")
    ).first.fill("iphone 17")
    page.get_by_role("button", name="Submit search", exact=True).or_(
        page.get_by_text("Submit search", exact=False)
    ).or_(
        page.get_by_label("Submit search", exact=True)
    ).or_(
        page.locator("button[type=\"submit\"]")
    ).or_(
        page.locator("div > div > form > div:nth-of-type(1) > button:nth-of-type(2)")
    ).first.click(force=True)
    page.bring_to_front()
    page.get_by_text("iPhone 17 Pro", exact=False).or_(
        page.locator("a[href*=\"iphone-17\"]:visible").nth(1)
    ).or_(
        page.locator("a[href=\"https://www.apple.com/iphone-17-pro/\"]")
    ).or_(
        page.locator("div#exploreCurated > div:nth-of-type(1) > div:nth-of-type(2) > h2 > a")
    ).first.click(force=True)
    page.bring_to_front()
    page.evaluate('window.scrollTo(0, 33961)')
    page.get_by_text("AirPods", exact=False).or_(
        page.locator("a[href*=\"airpods\"]:visible").nth(5)
    ).or_(
        page.locator("a[href=\"/airpods/\"]")
    ).or_(
        page.locator("ul#footer-directory-column-section-products > li:nth-of-type(7) > a")
    ).first.click(force=True)
    page.locator("div#image-loop-container > div:nth-of-type(4) > button").click(force=True)