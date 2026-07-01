from pages.home_page import HomePage


def test_recorded_flow(page):
    home_page = HomePage(page)

    # Navigate to Google first (as in the recorded script)
    home_page.open_url("https://www.google.com/")

    # Then navigate to Apple homepage
    home_page.open_url("https://www.apple.com/")
    home_page.bring_page_to_front()

    # Handle Google/consent interstitial if present
    home_page.handle_google_continue_interstitial()

    # Open OS previews page
    home_page.open_os_previews_page()

    # Navigate through iPadOS preview
    home_page.open_ipados_preview()

    # Scroll to match recorded flow behaviour
    home_page.scroll_to_y_position(2040)

    # Finally open macOS preview
    home_page.open_macos_preview()
    home_page.bring_page_to_front()
