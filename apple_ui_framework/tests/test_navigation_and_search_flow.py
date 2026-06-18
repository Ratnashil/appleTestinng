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

    # 1. Navigate to Google homepage
    page.goto("https://www.google.com/", wait_until="domcontentloaded")
    page.bring_to_front()

    # 2. Navigate to Apple homepage
    page.goto("https://www.apple.com/", wait_until="domcontentloaded")
    page.bring_to_front()

    # 3. Close the Apple country or region selector dialog
    page.get_by_role("button", name="Close country or region selector", exact=True).or_(
        page.get_by_text("Close country or region selector", exact=False)
    ).or_(
        page.get_by_label("Close country or region selector", exact=True)
    ).or_(
        page.locator("#ac-ls-close")
    ).or_(
        page.locator("button#ac-ls-close")
    ).first.click(force=True)

    # 4. Click the AirPods link from the Apple global navigation
    page.get_by_text("AirPods", exact=False).or_(
        page.locator("a[aria-label=\"AirPods\"]").nth(1)
    ).or_(
        page.get_by_label("AirPods", exact=True)
    ).or_(
        page.locator("a[href=\"/airpods/\"]")
    ).or_(
        page.locator("div > div:nth-of-type(7) > ul > li:nth-of-type(1) > a")
    ).first.click(force=True)

    # 5. Select the fourth item in the AirPods image loop
    page.locator("div#image-loop-container > div:nth-of-type(4) > button").click(force=True)

    # 6. Click the AirPods product link leading to the AirPods 4 page
    page.get_by_text("AirPods", exact=False).or_(
        page.locator("a[href*=\"airpods-4\"]:visible").nth(5)
    ).or_(
        page.locator("a[href=\"/airpods-4/\"]")
    ).or_(
        page.locator("nav#chapternav > div > ul > li:nth-of-type(1) > a")
    ).first.click(force=True)

    page.bring_to_front()

    # 7. Click the iPhone link from the Apple navigation
    page.get_by_text("iPhone", exact=False).or_(
        page.locator("a[aria-label=\"iPhone\"]").nth(1)
    ).or_(
        page.get_by_label("iPhone", exact=True)
    ).or_(
        page.locator("a[href=\"/iphone/\"]")
    ).or_(
        page.locator("div > div:nth-of-type(4) > ul > li:nth-of-type(1) > a")
    ).first.click(force=True)

    # 8. Open the 'Search apple.com' search UI on the iPhone page
    page.get_by_role("button", name="Search apple.com", exact=True).or_(
        page.get_by_text("Search apple.com", exact=False)
    ).or_(
        page.get_by_label("Search apple.com", exact=True)
    ).or_(
        page.locator("#globalnav-menubutton-link-search")
    ).or_(
        page.locator("a[role=\"button\"]")
    ).or_(
        page.locator("a[href=\"/us/search\"]")
    ).or_(
        page.locator("a#globalnav-menubutton-link-search")
    ).first.click(force=True)

    # 9. Enter 'apple' into the Apple site search field
    page.get_by_label("Search apple.com", exact=True).or_(
        page.get_by_placeholder("Search apple.com")
    ).or_(
        page.locator("div > div > form > div:nth-of-type(1) > input:nth-of-type(1)")
    ).first.fill("apple")

    # 10. Click the 'Submit search' button to run the Apple site search
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

    # 11. Click the 'Apple TV - Apple' search result link
    page.get_by_role("link", name="Apple TV - Apple", exact=True).or_(
        page.get_by_text("Apple TV - Apple", exact=False)
    ).or_(
        page.locator("a[href=\"https://www.apple.com/apple-tv/\"]")
    ).or_(
        page.locator("div#exploreOrganic > div:nth-of-type(1) > div:nth-of-type(1) > h2 > a")
    ).first.click(force=True)

    page.bring_to_front()