from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_scraper_for_history_trade import initialize_driver
import time
from selenium_stealth import stealth
import undetected_chromedriver as uc

# Configure proxy
proxy_ip = "195.35.9.31"  # Replace with your proxy IP
proxy_port = "443"

def check_website_with_selenium(url):
    try:
        options = Options()
        options.add_argument("start-maximized")

        # Chrome is controlled by automated test software
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        s = Service('C:\\WebDrivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=s, options=options)

        # Selenium Stealth settings
        stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win64",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
        # Open the website
        driver.get(url)

        # Wait for the page to load (adjust the sleep time as needed)
        time.sleep(10)

        # Check if the page title is accessible (basic check)
        page_title = driver.title
        print(f"Website loaded successfully. Page Title: {page_title}")

        # Optionally, check for specific elements on the page
        try:
            driver.find_element(By.TAG_NAME, 'body')  # Check if the body tag exists
            print("The website content is accessible.")
        except Exception as e:
            print("The website content is not accessible.")

        # Close the browser
        driver.quit()
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False


# Input website URL
website_url = input("Enter the website URL to check: ")

# Check if the website can be accessed with Selenium
if check_website_with_selenium(website_url):
    print("Selenium can interact with this website.")
else:
    print("Selenium cannot interact with this website.")
    
    
link = "https://www.gumtree.com.au/s-search.html"