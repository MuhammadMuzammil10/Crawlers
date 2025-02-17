from playwright.sync_api import sync_playwright
import time

url = "https://www.gumtree.com.au/s-search.html"
tab_selector = "a.tab-link"
content_selector = ".content"

with sync_playwright() as p:
    try:
        # Launch the browser
        browser = p.chromium.launch(
            headless=False)
        # browser = p.chromium.launch(
        #     headless=False,
        #     proxy={
        #     "server": "http://195.35.9.31:443",  # Replace with your proxy
        #     "username": "openvpn",  # If authentication is required
        #     "password": "Hostinger321@+"
        # },    )
        page = browser.new_page()
        # Set user-agent and headers
        # page.set_extra_http_headers({
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        # })
        # Navigate to the website
        page.goto(url)
        print("Page loaded:", page.title())
        time.sleep(10)
        
        # Click on the tab
        # page.click(tab_selector)
        # print("Clicked on the tab.")

        # # Wait for the content to load
        # page.wait_for_selector(content_selector, timeout=10000)  # 10-second timeout
        # print("Content loaded.")

        # Scrape data
        data = page.inner_text(content_selector)
        print("Scraped Data:", data)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the browser
        browser.close()