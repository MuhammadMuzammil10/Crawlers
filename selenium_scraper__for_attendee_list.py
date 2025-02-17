# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import TimeoutException
# import pandas as pd
# import time, os, re
# import logging


# def initialize_driver():
#     """Initialize WebDriver with options."""
#     options = Options()
#     # options.add_argument("--headless")  # Run in headless mode
#     # options.add_argument("--disable-gpu")
#     options.add_argument("--window-size=1920x1080")
#     return webdriver.Chrome(options=options)

# if __name__ == "__main__":
#     first_name = "Casey"
#     last_name = "Caronis"
#     email = "ccaronis@linklg.com"
    
#     driver = initialize_driver()


import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML file
with open('attendee_list.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

attendees = []

# Find all list items
for li in soup.find_all('li'):
    # Extract person's name
    name_tag = li.find('button', {'data-cvent-id': 'attendee-list-item-name'})
    name = name_tag.get_text(strip=True) if name_tag else 'N/A'
    
    # Extract company/job title info
    company_tag = li.find('div', {'data-cvent-id': 'attendee-list-item-company'})
    if company_tag:
        company_text = company_tag.get_text(strip=True).replace('&amp;', '&')
        # Split into job title and company
        if ',' in company_text:
            *job_title_parts, company = company_text.split(',')
            job_title = ','.join(job_title_parts).strip()  # Combine all parts before the last comma
            company = company.strip()
        else:
            job_title = company_text.strip()
            company = 'N/A'
    else:
        job_title = 'N/A'
        company = 'N/A'
    
    attendees.append({
        'Persons name': name,
        'Job title': job_title,
        'Company': company,
    })

# Create DataFrame and save to Excel
df = pd.DataFrame(attendees)
df.to_excel('attendees_list.xlsx', index=False)

print("Data successfully saved to attendees_list.xlsx")
