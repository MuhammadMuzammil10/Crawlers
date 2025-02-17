from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time

def scrape_history_trade_data(driver):
    data = {}
    print("Scrape History Trade data runs")
    date_format = "%m.%d.%Y %H:%M"
    start_date = datetime.strptime("12.01.2019 00:00", date_format)
    end_date = datetime.strptime("04.30.2020 23:59", date_format)

    try:
        # Navigate to the History tab
        history_tab = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "tabHistory"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", history_tab)
        driver.execute_script("arguments[0].click();", history_tab.find_element(By.TAG_NAME, "a"))
        print("Clicked on the 'tabHistory' tab successfully.")
        time.sleep(5)
    except Exception as e:
        print(f"Error clicking on 'tabHistory' tab: {e}")
        return {}

    def parse_date(date_string):
        try:
            return datetime.strptime(date_string, date_format)
        except ValueError:
            print(f"Invalid date format: {date_string}")
            return None

    def navigate_to_page(page_number):
        """Navigate to the specified page using the visible pagination."""
        max_retries = 3
        for _ in range(max_retries):
            try:
                print(f"Navigating to page {page_number}...")
                # Target the VISIBLE pagination (not the hidden one)
                pagination = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "ul.pagination:not(.mobile-paging)"))
                )
                # Find the page button
                page_button = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, f"ul.pagination:not(.mobile-paging) li a[page='{page_number}']"))
                )
                # Scroll into view and click using JavaScript
                driver.execute_script("arguments[0].scrollIntoView(true);", page_button)
                driver.execute_script("arguments[0].click();", page_button)
                # Wait for the table to reload
                WebDriverWait(driver, 30).until(
                    EC.staleness_of(pagination)  # Wait until the old pagination is gone
                )
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "table#tradingHistoryTable"))
                )
                time.sleep(3)
                return True
            except (TimeoutException, StaleElementReferenceException) as e:
                print(f"Retrying navigation to page {page_number}... Error: {e}")
                continue
        print(f"Failed to navigate to page {page_number} after {max_retries} attempts.")
        return False

    def get_page_date_range(page_number):
        """Get the first and last dates on the page."""
        if not navigate_to_page(page_number):
            return None, None
        try:
            history_table = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table#tradingHistoryTable"))
            )
            rows = history_table.find_elements(By.CSS_SELECTOR, "tbody tr")
            if not rows:
                return None, None
            first_row_date = parse_date(rows[0].find_elements(By.TAG_NAME, "td")[1].text.strip())
            last_row_date = parse_date(rows[-1].find_elements(By.TAG_NAME, "td")[1].text.strip())
            return first_row_date, last_row_date
        except Exception as e:
            print(f"Error getting dates for page {page_number}: {e}")
            return None, None

    def binary_search_pagination(start_page, end_page):
        """Binary search to find the starting page."""
        while start_page <= end_page:
            mid_page = (start_page + end_page) // 2
            print(f"Checking page {mid_page}...")
            first_date, last_date = get_page_date_range(mid_page)
            if not first_date or not last_date:
                break
            if last_date < start_date:
                start_page = mid_page + 1
            elif first_date > end_date:
                end_page = mid_page - 1
            else:
                return mid_page
        return start_page

    def scrape_page(page_number):
        """Scrape data from a single page."""
        if not navigate_to_page(page_number):
            return False
        try:
            history_table = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table#tradingHistoryTable"))
            )
            headers = [header.text.strip() for header in history_table.find_elements(By.CSS_SELECTOR, "thead tr th")]
            rows = history_table.find_elements(By.CSS_SELECTOR, "tbody tr")
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                row_data = [cell.text.strip() for cell in cells]
                open_date = parse_date(row_data[1])
                if open_date and start_date <= open_date <= end_date:
                    data[f"Row_{len(data) + 1}"] = dict(zip(headers, row_data))
                elif open_date and open_date > end_date:
                    print("Stopping pagination: Open date exceeds range.")
                    return False
            return True
        except Exception as e:
            print(f"Error scraping page {page_number}: {e}")
            return False

    # Get total pages from the VISIBLE pagination
    try:
        pagination = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul.pagination:not(.mobile-paging)"))
        )
        last_page = int(pagination.find_element(By.CSS_SELECTOR, "li a[lastpage='true']").get_attribute("page"))
        print(f"Total pages: {last_page}")
    except Exception as e:
        print(f"Error getting total pages: {e}")
        return {}

    # Binary search to find the starting page
    start_page = binary_search_pagination(1, last_page)
    if not start_page:
        print("No pages found within the date range.")
        return {}

    # Scrape pages sequentially from the starting page
    current_page = start_page
    while current_page <= last_page:
        if not scrape_page(current_page):
            break
        current_page += 1

    return data

while True:
#         try:
#             # Locate the table on the current page
#             history_table = WebDriverWait(driver, 20).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "table#tradingHistoryTable"))
#             )

#             # Extract headers
#             headers = [
#                 header.text.strip()
#                 for header in history_table.find_elements(By.CSS_SELECTOR, "thead tr th")
#             ]
#             print(f"Extracted headers: {headers}")

#             # Extract rows
#             rows = history_table.find_elements(By.CSS_SELECTOR, "tbody tr")
#             for index, row in enumerate(rows, start=1):
#                 cells = row.find_elements(By.TAG_NAME, "td")
#                 row_data = [cell.text.strip() for cell in cells]

#                 open_date = parse_date(row_data[1])  # Assuming 'Open Date' is the second column
#                 print("Open Date: ", open_date)

#                 if open_date and start_date <= open_date <= end_date:
#                     data[f"Row_{len(data) + 1}"] = dict(zip(headers, row_data))
#                 elif open_date and open_date > end_date:
#                     print("Open Date is beyond the desired range. Stopping pagination.")
#                     break

#                 print(f"Row {index}: {row_data}")

#             # Navigate to the next page
#             try:
#                 next_button = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, "#historyCont .pagination li.next a"))
#                 )
#                 if "disabled" in next_button.get_attribute("class"):
#                     print("No more pages available.")
#                     break
#                 driver.execute_script("arguments[0].click();", next_button)
#                 print("Navigated to the next page.")
#                 time.sleep(3)
#             except Exception as pagination_error:
#                 print(f"No further pages available or error in pagination: {pagination_error}")
#                 break

#         except Exception as e:
#             print(f"Error while processing the History table: {e}")
            break