import pytest

from pages.home_page import HomePage


@pytest.mark.allure_label("journey")
def test_recorded_flow(page, create_allure_artifact_dirs):
    home_page = HomePage(page)

    # Step 1: Open Google (external site) as in the recorded flow
    home_page.open_external_site("https://www.google.com/")

    # Step 2: Navigate to Apple.com and bring page to front
    home_page.open_external_site("https://www.apple.com/")

    # Step 3: Dismiss the regional/cookie modal via the Continue button
    home_page.dismiss_region_modal()

    # Step 4: Scroll down the home page
    home_page.scroll_by(4432)

    # Step 5: Open the Mac page via the main content link
    home_page.open_mac_from_main_content()

    # Step 6: Scroll further down the Mac page
    home_page.scroll_by(8507)
