from playwright.sync_api import sync_playwright, expect
# from test_script_helpers import (
#     _run_genai_validation,
# )

def test_recorded_flow():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.google.com/", wait_until='domcontentloaded')
        page.goto("https://www.google.com/?zx=1779254262883", wait_until='domcontentloaded')
        page.goto("https://www.apple.com/in/", wait_until='domcontentloaded')
        page.bring_to_front()
        # page.get_by_role('button', name='United States').click()
        # page.get_by_role('button', name='Close country or region selector').click()
        page.locator('a[aria-label="Store"]').click()
        page.locator("a[href*='buy-mac']:visible").filter(has_text="Mac").first.click()
        with page.expect_popup() as page1_info:
            page.locator("a[href*='retail']:visible").first.click()
        page1 = page1_info.value
        page.bring_to_front()
        page.locator("a[href*='list']:visible").filter(has_text="Order Status").first.click()
        page.bring_to_front()
        page.locator('a[aria-label="Store"]').click()
        page.evaluate('window.scrollTo(0, 4080)')
        with page.expect_popup() as page2_info:
            page.get_by_role('link', name='Shopping Help (opens in new window)', exact=False).click()
        page2 = page2_info.value
        # _run_genai_validation(page2, 'validate here and wow on screen')

        context.close()
        browser.close()


if __name__ == '__main__':
    test_recorded_flow()