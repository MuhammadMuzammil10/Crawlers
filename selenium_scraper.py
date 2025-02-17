from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Or use Firefox, Edge, etc.

# Open Myfxbook login page
driver.get("https://www.myfxbook.com/login")
time.sleep(2)

# Login credentials (replace with your own)
username = "evan.mlburgess@gmail.com"
password = "Qwertyuiop1!"

# Perform login
driver.find_element(By.ID, "loginEmail").send_keys(username)
driver.find_element(By.ID, "loginPassword").send_keys(password)
driver.find_element(By.ID, "login-btn").click()
time.sleep(5)

# Navigate to the main page
driver.get("https://www.myfxbook.com/")
time.sleep(5)

# Click the "Watched" toggle to make the list visible
try:
    watched_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "watchedTab"))
    )
    watched_tab.click()
    print("Clicked on the 'Watched' tab.")
    time.sleep(3)  # Allow time for the table to load
except Exception as e:
    print(f"Error clicking on 'Watched' tab: {e}")
    driver.quit()
    exit()

# Wait for the watched table to load
try:
    watched_table = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "watchedTable"))
    )
    print("Watched table loaded.")
except Exception as e:
    print("Error loading watched table:", e)
    driver.quit()
    exit()

# Locate the "watchedTable" and extract system links
rows = watched_table.find_elements(By.XPATH, '//tr[contains(@class, "watchedAccountRow")]')

system_links = []
for row in rows:
    try:
        link_element = row.find_element(By.TAG_NAME, "a")
        system_links.append(link_element.get_attribute("href"))
    except Exception as e:
        print(f"Error extracting link from row: {e}")

if system_links:
    print(f"Found {len(system_links)} system links.")
else:
    print("No system links found.")
    driver.quit()
    exit()

# Function to scrape data from a system page
def scrape_system_data(url):
    driver.get(url)
    time.sleep(3)

    data = {}

    # Extract "Stats" table
    try:
        stats_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#infoStats table"))
        )
        stats_rows = stats_table.find_elements(By.TAG_NAME, "tr")
        for row in stats_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 2:
                key = cells[0].text.strip().replace(":", "")
                value = cells[1].text.strip()
                data[key] = value
    except Exception as e:
        print(f"Error extracting Stats table: {e}")

    # Extract "General" table
    try:
        general_table = driver.find_element(By.CSS_SELECTOR, "#infoGeneral table")
        general_rows = general_table.find_elements(By.TAG_NAME, "tr")
        for row in general_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 2:
                key = cells[0].text.strip().replace(":", "")
                value = cells[1].text.strip()
                data[key] = value
    except Exception as e:
        print(f"Error extracting General table: {e}")

    return data

# Scrape only the first system link for now
first_system_link = system_links[0]
print(f"Scraping data from: {first_system_link}")
system_data = scrape_system_data(first_system_link)

# Save the scraped data to an Excel file
if system_data:
    df = pd.DataFrame([system_data])
    df.to_excel("system_data.xlsx", index=False)
    print("Data saved to 'system_data.xlsx'.")
else:
    print("No data scraped.")

# Close the browser
driver.quit()
