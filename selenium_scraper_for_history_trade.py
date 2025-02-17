from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time, os, re
import logging
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
import time

system_links = [ 'https://www.myfxbook.com/members/DIM_trade/belkaglazer-icmarkets/4382719', 'https://www.myfxbook.com/members/BigGlobalCapital/big-global-currency-fund-1/10662979', 'https://www.myfxbook.com/members/DizFix/bot2-581-neomod1/3270892', 'https://www.myfxbook.com/members/DizFix/bot3-978-neoagr/3564720', 'https://www.myfxbook.com/members/sixth_sense/breakthrough-strategy-icm/3631372', 'https://www.myfxbook.com/members/kazem3d/cent/3600868', 'https://www.myfxbook.com/members/CTrading80/ciarantrading/3516927', 'https://www.myfxbook.com/members/Hydra_MrRobot/copy-trade/3569855', 'https://www.myfxbook.com/members/ezrabarak/dar58197-41todam152/3334314', 'https://www.myfxbook.com/members/LongVision/darwin-tvs/3575530', 'https://www.myfxbook.com/members/johnmacknamara/day-night-trading/2605595', 'https://www.myfxbook.com/members/Salex_d/diamondfx-forex4you/3313183', 'https://www.myfxbook.com/members/Mkplr1/discretionary/3348474', 'https://www.myfxbook.com/members/pornsakc/doraemon-r1/3563183', 'https://www.myfxbook.com/members/Deepocketsystem/dps/3985973', 'https://www.myfxbook.com/members/HTServices/ea-ht-mix-prom5/6525998', 'https://www.myfxbook.com/members/HTServices/ea-ht-plus/6526060', 'https://www.myfxbook.com/members/eafiltergrid/eafg-190304/10188767', 'https://www.myfxbook.com/members/eladaforex/elada-fibo-64/3560952', 'https://www.myfxbook.com/members/TopRank/elite-forex-scalper/11102084', 'https://www.myfxbook.com/members/ayman30/equiti-fahad-live1/3531541', 'https://www.myfxbook.com/members/raaalphs/eurcad/2739006', 'https://www.myfxbook.com/members/Alcad83/fair-signal/5387387', 'https://www.myfxbook.com/members/Mkplr1/finch-11/3363612', 'https://www.myfxbook.com/members/Mkplr1/finch-241/3339087', 'https://www.myfxbook.com/members/klasterer/finch-live/3739895', 'https://www.myfxbook.com/members/vetallnemo/firmum-fiduciam-motus/1584377', 'https://www.myfxbook.com/members/orban8600/flex-ea-ribozymehalfgrid/6685775', 'https://www.myfxbook.com/members/alanproject/forex-cyborg-high-risk/7872037', 'https://www.myfxbook.com/members/forexdiamond/forex-diamond-real-money/3402799', 'https://www.myfxbook.com/members/SwapsRollovers/fp-markets-news-tradingrisk-events/11018593', 'https://www.myfxbook.com/members/sst_trader/fxcm-mara/8695681', 'https://www.myfxbook.com/members/ayman30/fxdd-ayman-live2/4757156', 'https://www.myfxbook.com/members/ayman30/fxdd-ayman-live3/4757016', 
'https://www.myfxbook.com/members/ayman30/fxdd-talal-live1/4758241', 'https://www.myfxbook.com/members/g0301837/g030-ig-wsevo2/2930253', 'https://www.myfxbook.com/members/akm1971/generic/1858058', 'https://www.myfxbook.com/members/GerFX/gerfx-momentum-capture-ea-selected/6430164', 'https://www.myfxbook.com/members/GerFX/gerfx-quantflow-scalper-nightwalker-ea/6430073', 'https://www.myfxbook.com/members/Ramss999/global-range/2551932', 'https://www.myfxbook.com/members/Meawbin_Project/gmi-silver-grid/3527233', 'https://www.myfxbook.com/members/grantlow/gmmav1/7967325', 'https://www.myfxbook.com/members/zv735/goldmind-cs-kzm/2259132', 'https://www.myfxbook.com/members/JoyJoy735/goldmind-super-b-eu/2536388', 'https://www.myfxbook.com/members/LeilaWilliams/greezly/9855219', 'https://www.myfxbook.com/members/Pijitr/halfgrid-cent/3599515', 'https://www.myfxbook.com/members/tradermc/ic-mam-eur/8943883', 'https://www.myfxbook.com/members/FERRARI2009/ic-markets/3534905', 'https://www.myfxbook.com/members/me156695/ic-markets-live/3299297', 
'https://www.myfxbook.com/members/arnoldTT/ic-mt5/3516149', 'https://www.myfxbook.com/members/tranle447/ic-aud/1191686', 'https://www.myfxbook.com/members/forexstore/incontrol/2624558', 'https://www.myfxbook.com/members/sofiansyah/insta-5235/7579555', 'https://www.myfxbook.com/members/FXTGFund/investing-geometry/4758171', 'https://www.myfxbook.com/members/Tannim/kazi-tanjedul-ershad/3477109', 'https://www.myfxbook.com/members/mt4easystemtrade/khs-3000-s20-titanfx-01/1914305', 'https://www.myfxbook.com/members/off_np/kongchang-noppadon/2218093', 'https://www.myfxbook.com/members/Kudou/kudou2/2631932', 'https://www.myfxbook.com/members/Leonetrading/leonetrading-strategy/11059247', 'https://www.myfxbook.com/members/LPiton/longterminvest/7949084', 'https://www.myfxbook.com/members/ota_0626_2019/ma3-sv01-108-8961/3394297', 'https://www.myfxbook.com/members/TradingIQ/marshcapitalmgmt/3968123', 'https://www.myfxbook.com/members/JakovM/martnmultym/2750132', 'https://www.myfxbook.com/members/mandysoy/masterbots-trezor-00/3524841', 'https://www.myfxbook.com/members/migoninvest/migon-invest/7458946', 'https://www.myfxbook.com/members/migueldelavega/migue/2712041', 'https://www.myfxbook.com/members/mtbennett/momentumbreakout/2329049', 'https://www.myfxbook.com/members/TeodorchikFest/moneymaker/2240613', 'https://www.myfxbook.com/members/sendbad/mt4-186719/3562679', 'https://www.myfxbook.com/members/bocs/mt5-5104737/3532117', 'https://www.myfxbook.com/members/bocs/mt5-5106645/3533990', 'https://www.myfxbook.com/members/bocs/mt5-5124964/3685050', 'https://www.myfxbook.com/members/NAGAN1/nagan-amarkets/6807575', 'https://www.myfxbook.com/members/Viacheslav1212/natali/10917804', 'https://www.myfxbook.com/members/s991432/nice-money/4380794', 'https://www.myfxbook.com/members/FCAcademyTS/nobelportolio-agressive/6521685', 'https://www.myfxbook.com/members/FCAcademyTS/nobelportolio-moderate/6521755', 'https://www.myfxbook.com/members/m1800/o6b--ic-marketsxx873/2139608', 'https://www.myfxbook.com/members/m1800/o6b--ic-marketsxx986/2633250', 'https://www.myfxbook.com/members/OnkelSeaborn/os-2022/9909957', 'https://www.myfxbook.com/members/hmacedo/pepper-manual-mt5-51013387/4399449', 'https://www.myfxbook.com/members/Pierstage_CM/portfolio-6/7573066', 'https://www.myfxbook.com/members/robotadvisor/portfolio-black-ra991p/10026710', 'https://www.myfxbook.com/members/rahulkghosh777/portfolio-oanda/2285764', 'https://www.myfxbook.com/members/pouis/pouis-main-account/974895', 'https://www.myfxbook.com/members/leapfx/power-growth-trader/10536828', 'https://www.myfxbook.com/members/mandysoy/pro-masterbots-trezor/3524846', 'https://www.myfxbook.com/members/kalvera/ps-magicc-aaa/3461259', 'https://www.myfxbook.com/members/PUNFUN2522/punfun-cent-martin/2717982', 'https://www.myfxbook.com/members/master_255/qm-type2/1876475', 'https://www.myfxbook.com/members/Ramabhakta/rama-gld-trump-100-50/3619824', 'https://www.myfxbook.com/members/katins/real1/10548183', 'https://www.myfxbook.com/members/zufarka/revenge/2263050', 'https://www.myfxbook.com/members/johnmacknamara/rfactor-eurcad-high-risk/2611161', 'https://www.myfxbook.com/members/BLZRobots/rf-hrtrump/3520572', 'https://www.myfxbook.com/members/investingpartner/safemove01/5237622', 'https://www.myfxbook.com/members/strueli/scalpers-icm-ecn/2194412', 'https://www.myfxbook.com/members/Pikasso/scr-euraud/3099604', 'https://www.myfxbook.com/members/forextraffic/sets-lem-1-2-from/9468346', 'https://www.myfxbook.com/members/pornsakc/sirinya/8689756', 'https://www.myfxbook.com/members/fxknot/sleepsheep/6891995', 'https://www.myfxbook.com/members/kris1002/sputnik2019/11155388', 'https://www.myfxbook.com/members/StarGoGo/stargogo/2517413', 'https://www.myfxbook.com/members/infoidea_uab/steve-audcad/10019413', 'https://www.myfxbook.com/members/suchl/su01/2413532', 'https://www.myfxbook.com/members/free20190720/systema/9414639', 'https://www.myfxbook.com/members/taichi20200218/taichi20200218/4706567', 'https://www.myfxbook.com/members/pornsakc/tanjiro/10146322', 'https://www.myfxbook.com/members/Cantax/tfl52-algo-trading/6180151', 'https://www.myfxbook.com/members/zcy789/top-bottom-ea/10069555', 'https://www.myfxbook.com/members/FCAcademyTS/trading-hero-5k/10330743', 'https://www.myfxbook.com/members/tradingsvietnam/tradings-capital/7232342', 'https://www.myfxbook.com/members/TravanCorpLLC/travancorpllcgmailcom/6253049', 'https://www.myfxbook.com/members/Upavla/trd-non-stop/4195609', 'https://www.myfxbook.com/members/aarontdang/tt1/4312047', 'https://www.myfxbook.com/members/MariSus/turbo200/7599553', 'https://www.myfxbook.com/members/rumax1704/ultra-30/3160717', 'https://www.myfxbook.com/members/raaalphs/usdjpy/2739016', 'https://www.myfxbook.com/members/sezer/vector-capital-mean-reversion/8894593', 'https://www.myfxbook.com/members/VBellon/v%C3%ADctorbell%C3%B3n/3248141', 'https://www.myfxbook.com/members/to_ining/wca/3576884', 'https://www.myfxbook.com/members/m131313/webmastermaksimru-alpari-etz/1658051', 'https://www.myfxbook.com/members/YUWENXIN/xinance-tw/8782015', 'https://www.myfxbook.com/members/zaniah/xtb-real/3221378', 'https://www.myfxbook.com/members/tvi86/%D0%BE%D1%82-%D1%84%D0%BE%D0%BD%D0%B0%D1%80%D1%8F-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D0%B5%D0%B9/1263615' ]
links_done = [
    'https://www.myfxbook.com/members/RiskOn/0288/9816086', 'https://www.myfxbook.com/members/eaknam/1930849/4449317', 'https://www.myfxbook.com/members/polacektrading/2000005143/10309391', 'https://www.myfxbook.com/members/Anarxist/2020-09-22/7196397','https://www.myfxbook.com/members/Scrittore/alpari-ecn/3538933',  'https://www.myfxbook.com/members/raaalphs/audcad/2739005', 'https://www.myfxbook.com/members/raaalphs/audusd/2738997', 'https://www.myfxbook.com/members/sawyer_h/ava-live/3349355', 'https://www.myfxbook.com/members/Jaumeso/axitrader/2735924', 'https://www.myfxbook.com/members/Pijitr/bbands-cent/3506529', 'https://www.myfxbook.com/members/majdan/become-more-2/7514512',
    'https://www.myfxbook.com/members/vshmonov/4-profit-fx321/3615560', 'https://www.myfxbook.com/members/Natawun/46013378/3335854', 'https://www.myfxbook.com/members/yunben/536371/2413233', 'https://www.myfxbook.com/members/coymahrens/930760/7638071', 'https://www.myfxbook.com/members/Ravengroup2/6ftr-06/3208652', 'https://www.myfxbook.com/members/tizianob/activetrades25-1/8565855', 'https://www.myfxbook.com/members/ahmedzubair/ahmed-zubair-dhaiban-aldhaif/3205751', 'https://www.myfxbook.com/members/akfx_ru/akfx-aggresive/2681353', 'https://www.myfxbook.com/members/albumariusiulian/albumariusiulian/3509808',
]
links_remaining = ['https://www.myfxbook.com/members/Michail91/alc-70519/3574281', 'https://www.myfxbook.com/members/FCAcademyTS/alpha-libertex/9230050',]
links_private = ['https://www.myfxbook.com/members/ProjectXFX/asterysc-hunter-1/2992420', 'https://www.myfxbook.com/members/pitufogranjero/axi/2322201',]
# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def initialize_driver():
    """Initialize WebDriver with options."""
    options = Options()
    # options.add_argument("--headless")  # Run in headless mode
    # options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    return webdriver.Chrome(options=options)

def login_to_myfxbook(driver, username, password):
    """Login to Myfxbook."""
    driver.get("https://www.myfxbook.com/login")
    time.sleep(5)
    # Perform login
    driver.find_element(By.ID, "loginEmail").send_keys(username)
    driver.find_element(By.ID, "loginPassword").send_keys(password)
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(5)
    logging.info("Logged into Myfxbook.")
    time.sleep(5)

def handle_popup(driver):
    """Handle any popup modals."""
    try:
        modal = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "popupAdModal"))
        )
        modal.find_element(By.XPATH, '//button[@data-dismiss="modal"]').click()
        logging.info("Popup handled.")
    except Exception:
        logging.info("No popup appeared.")

def scrape_watched_links(driver):
    """Scrape links from the Watched list."""
    # Click the "Watched" toggle to make the list visible
    try:
        watched_tab = WebDriverWait(driver, 20).until(
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
        watched_table = WebDriverWait(driver, 20).until(
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
    return system_links

def scrape_section_data(driver, section_id):
    print("Scrape Section data runs")
    """Scrape data from a specific section by its ID."""
    data = {}
    if section_id == 'infoGeneral':
        try:
            # Locate and click the tab, ensuring it's clickable
            watched_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "infoGeneralTab"))
            )
            # Scroll the element into view to avoid interception
            driver.execute_script("arguments[0].scrollIntoView(true);", watched_tab)
            # Use JavaScript to click if direct click fails
            driver.execute_script("arguments[0].click();", watched_tab)
            print("Clicked on the 'infoGeneralTab' tab successfully.")
            time.sleep(3)  # Allow time for the table to load
        except Exception as e:
            print(f"Error clicking on 'infoGeneralTab' tab: {e}")
            # Optional: Save a screenshot for debugging
            # driver.save_screenshot("infoGeneralTab_click_error.png")
            return {}
        section_container = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "system-info-section"))
        )
        # Locate and click the tab, ensuring it's clickable
        tables = section_container.find_elements(By.CSS_SELECTOR, "table")
        for table in tables:
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) == 2:
                    key = cells[0].text.strip()
                    value = cells[1].text.strip()
                    print("KEY: ", key, "Value: ", value)
                    data[key] = value
                    if key == 'Started:':
                        started_date = value
                        print("Started key is: ", value)
                        # try:
                        started_datetime = datetime.strptime(started_date, "%b %d, %Y")
                        cutoff_datetime = datetime(2019, 12, 31)
                        if started_datetime > cutoff_datetime:
                            print(f"'Started' date {started_date} is later than December 2019. Skipping link.")
                            return None,None
                        else:
                            history_data = scrape_last_history_trade_data(driver)
                        # except ValueError:
                        #     print(f"Invalid date format for 'Started': {started_date}. Skipping link.")
                        #     return None

    return data, history_data  # Return both general data and history data

 
# def scrape_history_trade_data(driver):
#     data = {}
#     print("Scrape History Trade data runs")
#     date_format = "%m.%d.%Y %H:%M"  # Expected date format in the table
#     start_date = datetime.strptime("12.01.2019 00:00", date_format)
#     end_date = datetime.strptime("04.30.2020 23:59", date_format)
#     try:
#         # Wait for the History tab to become clickable
#         history_tab = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.ID, "tabHistory"))
#         )
        
#         # Scroll the element into view to avoid interception
#         driver.execute_script("arguments[0].scrollIntoView(true);", history_tab)
        
#         # Click the <a> tag inside the <li> with ID 'tabHistory'
#         history_link = history_tab.find_element(By.TAG_NAME, "a")
#         driver.execute_script("arguments[0].click();", history_link)
        
#         print("Clicked on the 'tabHistory' tab successfully.")
#         time.sleep(3)  # Allow time for the table to load
#     except Exception as e:
#         print(f"Error clicking on 'tabHistory' tab: {e}")
#         return {}
    
#     # Function to parse date strings into datetime objects
#     def parse_date(date_string):
#         try:
#             return datetime.strptime(date_string, date_format)
#         except ValueError:
#             print(f"Invalid date format: {date_string}")
#             return None  # Handle empty or invalid date fields
        
#     # try:
#     while True:
#         # Locate the table in the History section
#         history_table = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "table#tradingHistoryTable"))
#         )

#         # Extract headers from the table
#         headers = [
#             header.text.strip()
#             for header in history_table.find_elements(By.CSS_SELECTOR, "thead tr th")
#         ]
#         print(f"Extracted headers: {headers}")

#         # Extract rows from the table
#         rows = history_table.find_elements(By.CSS_SELECTOR, "tbody tr")
#         for index, row in enumerate(rows, start=1):
#             cells = row.find_elements(By.TAG_NAME, "td")
#             row_data = [cell.text.strip() for cell in cells]
#             # Extract Open Date and filter by range
#             open_date = parse_date(row_data[1])  # Assuming 'Open Date' is the first column
#             print("Open Date: ", open_date)
#             if open_date and start_date <= open_date <= end_date:
#                 data[f"Row_{len(data) + 1}"] = dict(zip(headers, row_data))
#             elif open_date and open_date > end_date:
#                 # If the Open Date is beyond the desired range, stop processing further
#                 print("Open Date is beyond the desired range. Stopping pagination.")
#                 try:
#                     pagination = driver.find_element(By.CSS_SELECTOR, "#historyCont .pagination")
#                     # Locate the "Next" button
#                     next_button = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.CSS_SELECTOR, "#historyCont .pagination li.next a"))
#                     )
#                     if "disabled" in next_button.get_attribute("class"):
#                         print("No more pages available.")
#                         break  # Stop if the next button is disabled

#                     driver.execute_script("arguments[0].click();", next_button)
#                     print("Navigated to the next page.")
#                     time.sleep(2)

#                 except Exception as pagination_error:
#                     print(f"No further pages available or error in pagination: {pagination_error}")
#                     break
#                 # return data
#             print(f"Row {index}: {row_data}")

#                 # Map row data to corresponding headers
#                 # data[f"Row_{index}"] = dict(zip(headers, row_data))
#             # Navigate to the next page if available
#             # try:
#             #     pagination = driver.find_element(By.CSS_SELECTOR, "#historyCont .pagination")
#             #     next_button = pagination.find_element(By.CSS_SELECTOR, "li.next")

#             #     if "disabled" in next_button.get_attribute("class"):
#             #         print("No more pages available.")
#             #         break  # Stop if the next button is disabled

#             #     driver.execute_script("arguments[0].click();", next_button)
#             #     print("Navigated to the next page.")
#             #     time.sleep(2)

#             # except Exception as pagination_error:
#             #     print(f"No further pages available or error in pagination: {pagination_error}")
#             #     break

#             # print("History trade data successfully scraped.")
#     # except Exception as e:
#     #     print(f"Error extracting data from the History table: {e}")
#     #     return {}

#     return data
  
# def scrape_history_trade_data(driver):
#     data = {}
#     print("Scrape History Trade data runs")
#     date_format = "%m.%d.%Y %H:%M"  # Expected date format in the table
#     start_date = datetime.strptime("12.01.2019 00:00", date_format)
#     end_date = datetime.strptime("04.30.2020 23:59", date_format)

#     try:
#         # Wait for the History tab to become clickable
#         history_tab = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.ID, "tabHistory"))
#         )
#         driver.execute_script("arguments[0].scrollIntoView(true);", history_tab)
#         driver.execute_script("arguments[0].click();", history_tab.find_element(By.TAG_NAME, "a"))
#         print("Clicked on the 'tabHistory' tab successfully.")
#         time.sleep(3)  # Allow time for the table to load
#     except Exception as e:
#         print(f"Error clicking on 'tabHistory' tab: {e}")
#         return {}

#     def parse_date(date_string):
#         try:
#             return datetime.strptime(date_string, date_format)
#         except ValueError:
#             print(f"Invalid date format: {date_string}")
#             return None

#     while True:
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
#             break

#     return data

def scrape_history_trade_data(driver):
    print("Scrape History Trade data runs")
    data = {}
    date_format = "%m.%d.%Y %H:%M"
    start_date = datetime.strptime("12.01.2019 00:00", date_format)
    end_date = datetime.strptime("04.30.2020 23:59", date_format)
    # start_date = datetime.strptime("02.27.2022 00:00", date_format)
    # end_date = datetime.strptime("10.8.2021 23:59", date_format)

    # Navigate to History tab
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
    # **🔹 Pause for Manual Click on 'Open Date' Header**
    input("🔹 Click manually on the 'Open Date' header in the browser, then press ENTER here to continue...")
    def parse_date(date_string):
        try:
            return datetime.strptime(date_string, date_format)
        except ValueError:
            print(f"Invalid date format: {date_string}")
            return None
    
    while True:
        try:
            # Locate the table on the current page
            history_table = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table#tradingHistoryTable"))
            )
            # Extract headers
            headers = [
                header.text.strip()
                for header in history_table.find_elements(By.CSS_SELECTOR, "thead tr th")
            ]
            print(f"Extracted headers: {headers}")

            filtered_headers = [h for h in headers if h]  # Remove empty headers
            print(f"Filtered Headers: {filtered_headers}")

            # Extract rows
            rows = history_table.find_elements(By.CSS_SELECTOR, "tbody tr")
            if not rows:
                print("No rows found in the table.")
                break

            # Get the first and last row's Open Date
            first_row = rows[0]
            last_row = rows[-1]

            first_cells = first_row.find_elements(By.TAG_NAME, "td")
            first_row_data = [cell.text.strip() for cell in first_cells]
            filtered_first_row_data = [first_row_data[i] for i in range(len(headers)) if headers[i]]
            first_row_dict = dict(zip(filtered_headers, filtered_first_row_data))
            first_date = parse_date(first_row_dict.get("Open Date"))

            last_cells = last_row.find_elements(By.TAG_NAME, "td")
            last_row_data = [cell.text.strip() for cell in last_cells]
            filtered_last_row_data = [last_row_data[i] for i in range(len(headers)) if headers[i]]
            last_row_dict = dict(zip(filtered_headers, filtered_last_row_data))
            last_date = parse_date(last_row_dict.get("Open Date"))

            # Check if the entire page can be skipped
            if first_date and last_date:
                if first_date < start_date and last_date < start_date:
                    print(f"🚀 Skipping page (all rows are older than start date: {start_date})")
                    # Navigate to the next page
                    try:
                        next_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "#historyCont .pagination li.next a"))
                        )
                        if "disabled" in next_button.get_attribute("class"):
                            print("No more pages available.")
                            break
                        driver.execute_script("arguments[0].click();", next_button)
                        print("Navigated to the next page.")
                        time.sleep(3)
                        continue  # Skip processing this page
                    except Exception as pagination_error:
                        print(f"No further pages available or error in pagination: {pagination_error}")
                        break

                if first_date > end_date:
                    print(f"🔴 First row date {first_date} is beyond the desired range. Stopping pagination.")
                    print("📌 Data collected so far:", data)
                    return data  # Stop execution
                
            for index, row in enumerate(rows, start=1):
                cells = row.find_elements(By.TAG_NAME, "td")
                row_data = [cell.text.strip() for cell in cells]

                # Remove empty values in the row corresponding to removed headers
                filtered_row_data = [r for r in row_data if r]

                # Map filtered headers to filtered row data
                row_dict = dict(zip(filtered_headers, filtered_row_data))

                open_date = parse_date(row_dict.get("Open Date"))  # Fetch Open Date safely
                print("Open Date: ", open_date)

                if open_date:
                    if open_date < start_date:
                        print(f"🚀 Skipping old date: {open_date}")
                        continue
                    elif open_date > end_date:
                        print(f"🔴 Open Date {open_date} is beyond the desired range. Stopping pagination.")
                        print("📌 Data collected so far:", data)
                        return data  # Stop execution

                    data[f"Row_{len(data) + 1}"] = row_dict
                print(f"✅ Row {index}: {row_data}")

            # Navigate to the next page
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#historyCont .pagination li.next a"))
                )
                if "disabled" in next_button.get_attribute("class"):
                    print("No more pages available.")
                    break
                driver.execute_script("arguments[0].click();", next_button)
                print("Navigated to the next page.")
                time.sleep(3)
            except Exception as pagination_error:
                print(f"No further pages available or error in pagination: {pagination_error}")
                break

        except Exception as e:
            print(f"Error while processing the History table: {e}")
            break

    return data

def scrape_last_history_trade_data(driver):
    print("Scrape History Trade data runs")
    data = {}
    date_format = "%m.%d.%Y %H:%M"
    start_date = datetime.strptime("12.01.2019 00:00", date_format)
    end_date = datetime.strptime("04.30.2020 23:59", date_format)

    # Navigate to History tab
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

    # Manual intervention for sorting
    input("🔹 Click manually on the 'Close Date' header in the browser, then press ENTER here to continue...")

    def parse_date(date_string):
        if not date_string:  # Handle empty/NONE dates
            return None
        try:
            return datetime.strptime(date_string, date_format)
        except ValueError:
            print(f"Invalid date format: {date_string}")
            return None

    while True:
        try:
            # Locate the table on the current page
            history_table = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table#tradingHistoryTable"))
            )

            # Extract headers
            headers = [
                header.text.strip()
                for header in history_table.find_elements(By.CSS_SELECTOR, "thead tr th")
            ]
            print(f"Extracted headers: {headers}")

            filtered_headers = [h for h in headers if h]  # Remove empty headers
            print(f"Filtered Headers: {filtered_headers}")

            # Extract rows
            rows = history_table.find_elements(By.CSS_SELECTOR, "tbody tr")
            if not rows:
                print("No rows found in the table.")
                break

            # Get the first and last row's Close Date
            first_row = rows[0]
            last_row = rows[-1]

            # Helper function to extract row data
            def get_row_data(row):
                cells = row.find_elements(By.TAG_NAME, "td")
                row_data = [cell.text.strip() for cell in cells]
                filtered_data = [r for r in row_data if r]
                return dict(zip(filtered_headers, filtered_data))

            first_row_dict = get_row_data(first_row)
            last_row_dict = get_row_data(last_row)

            first_date = parse_date(first_row_dict.get("Close date"))
            last_date = parse_date(last_row_dict.get("Close date"))

            print(f"First Close Date: {first_date}, Last Close Date: {last_date}")  # Debugging

            # Check if the entire page can be skipped
            if last_date is not None:
                if last_date < start_date:
                    print(f"🚀 Skipping page (last row date {last_date} < start date {start_date})")
                    # Navigate to the next page
                    try:
                        next_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "#historyCont .pagination li.next a"))
                        )
                        if "disabled" in next_button.get_attribute("class"):
                            print("No more pages available.")
                            break
                        driver.execute_script("arguments[0].click();", next_button)
                        print("Navigated to the next page.")
                        time.sleep(3)
                        continue  # Skip processing rows for this page
                    except Exception as pagination_error:
                        print(f"No further pages available or error in pagination: {pagination_error}")
                        break

                if first_date is not None and first_date > end_date:
                    print(f"🔴 First row date {first_date} > end date {end_date}. Stopping pagination.")
                    print("📌 Data collected so far:", data)
                    return data  # Stop execution
            else:
                print("⚠️ Last Close Date is missing; processing page manually.")

            # Process rows on the current page
            for index, row in enumerate(rows, start=1):
                row_dict = get_row_data(row)
                close_date = parse_date(row_dict.get("Close date"))

                if not close_date:
                    print("⚠️ Skipping row with missing Close Date")
                    continue

                if close_date < start_date:
                    print(f"🚀 Skipping old date: {close_date}")
                    continue
                elif close_date > end_date:
                    print(f"🔴 Close Date {close_date} is beyond the desired range. Stopping pagination.")
                    print("📌 Data collected so far:", data)
                    return data  # Stop execution

                data[f"Row_{len(data) + 1}"] = row_dict
                print(f"✅ Row {index}: {row_dict}")

            # Navigate to the next page
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#historyCont .pagination li.next a"))
                )
                if "disabled" in next_button.get_attribute("class"):
                    print("No more pages available.")
                    break
                driver.execute_script("arguments[0].click();", next_button)
                print("Navigated to the next page.")
                time.sleep(3)
            except Exception as pagination_error:
                print(f"No further pages available or error in pagination: {pagination_error}")
                break

        except Exception as e:
            print(f"Error while processing the History table: {e}")
            break

    return data
# def scrape_system_data(driver, link):
#     """Scrape data from a specific system link."""
#     logging.info(f"Current link: {link}")
#     try:
#         # Navigate to the link
#         driver.get(link)
#         time.sleep(2)  # Optional: Adjust based on page load speed

#         # Scrape data from both sections
#         # Wait for the system name to load (example element)
#         system_name = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.TAG_NAME, "h1"))  # Replace with actual selector
#         ).text.strip()
#         logging.info(f"System name: {system_name}")
#         # stats_data = scrape_section_data(driver, "infoStats")
#         general_data = scrape_section_data(driver, "infoGeneral")
#         # advance_trade_data = scrape_advance_section_data(driver, 'trades')
#         # advance_risk_data = scrape_advance_section_data(driver, 'riskDataTab')

#         # Combine both sections' data
#         return {
#             "system": {'system': system_name},
#             # "infoStats": stats_data,
#             "infoGeneral": general_data,
#             # "advanceTrade": advance_trade_data,
#             # "advanceRisk": advance_risk_data
#         }
#     except TimeoutException as e:
#         logging.error(f"Timeout while accessing link: {link}. Skipping this link.")
#         return None  # Skip this link and return None
#     except Exception as e:
#         logging.error(f"Unexpected error while processing link: {link}. Error: {e}")
#         return None  # Skip this link and return None

# Modified scrape_system_data to integrate saving
def scrape_system_data(driver, link):
    """Scrape data from a specific system link and save to Excel"""
    system_data = {
        "system": {},
        "infoGeneral": {},
        "history": {}  # This will be populated by scrape_history_trade_data
    }
    
    try:
        driver.get(link)
        time.sleep(2)

        # Get system name
        system_name = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        ).text.strip()
        system_data["system"]["system"] = system_name

        # Get general info and history data from scrape_section_data
        general_data, history_data = scrape_section_data(driver, "infoGeneral")

        if general_data is None:
            print("Skipping system due to invalid start date.")
            return None

        system_data["infoGeneral"] = general_data
        system_data["history"] = history_data  # This now contains the history data

        # Save to Excel
        save_to_excel(system_data)
        return system_data

    except Exception as e:
        print(f"Error in processing system: {e}")
        return None

PREDEFINED_HEADERS = [
    'method', 'trading', 'system', 'Open Date', 'Close date', 'Symbol',
    'Action', 'Open Price', 'Close Price', 'Profit (USD)', 'Duration', 'Gain']

def save_to_excel(data, filename="trading_data.xlsx"):
    """Save scraped data to Excel with predefined structure"""

    # Load existing data if file exists, otherwise create an empty DataFrame
    if os.path.exists(filename):
        df = pd.read_excel(filename)
    else:
        df = pd.DataFrame(columns=PREDEFINED_HEADERS)

    # Extract general info
    method = data.get('infoGeneral', {}).get('System', '')
    trading = data.get('infoGeneral', {}).get('Trading', '')
    system = data.get('system', {}).get('system', '')

    # Extract history data (Iterate over multiple rows)
    history_data = data.get('history', {})
    new_rows = []
    
    for row_key, row in history_data.items():
        # Prepare row data
        row_data = {
            'method': method,
            'trading': trading,
            'system': system,
            'Open Date': row.get('Open Date', ''),
            'Close date': row.get('Close date', ''),
            'Symbol': row.get('Symbol', ''),
            'Action': row.get('Action', ''),
            'Open Price': row.get('Open Price', ''),
            'Close Price': row.get('Close Price', ''),
            'Profit (USD)': row.get('Profit\n(USD)', ''),  # Fixing key mismatch
            'Duration': row.get('Duration', ''),
            'Gain': row.get('Gain', '')
        }

        # Convert date strings to datetime objects
        date_columns = ['Open Date', 'Close date']
        for col in date_columns:
            if row_data[col]:
                try:
                    row_data[col] = datetime.strptime(row_data[col], "%m.%d.%Y %H:%M")
                except ValueError:
                    row_data[col] = None  # Invalid date format handling

        new_rows.append(row_data)

    # Create DataFrame for new rows
    new_df = pd.DataFrame(new_rows)

    # Append to existing data
    df = pd.concat([df, new_df], ignore_index=True)

    # Save to Excel
    try:
        df.to_excel(filename, index=False)
        print(f"Data successfully saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving to Excel: {e}")
        return False
    
if __name__ == "__main__":
    username = "evan.mlburgess@gmail.com"
    password = "Qwertyuiop1!"
    
    driver = initialize_driver()
    try:
        # login_to_myfxbook(driver, username, password)
        # handle_popup(driver)
        # system_links = scrape_watched_links(driver)
        
        # print("System links: ",system_links)
        
        # Get the list of already-scraped system names
        # existing_system_names = get_existing_system_names()

        if system_links:
            start_index = 10  # Starting index for slicing
            end_index = 672    # Ending index for slicing
            for link in system_links:
                # print(f"Processing link {i}: {link}")
                print("Current link: ", link)
                
                # Navigate to the link to get the system name first
                driver.get(link)
                time.sleep(2)  # Adjust based on page load speed

                try:
                    # Retrieve the system name
                    system_name = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.TAG_NAME, "h1"))  # Replace with actual selector
                    ).text.strip()
                    
                    # if system_name in existing_system_names:
                    #     print(f"System '{system_name}' already exists. Skipping...")
                    #     continue  # Skip this link if the system name is already in the file
                    
                    # If not already processed, scrape the system data
                    data = scrape_system_data(driver, link)
                    # if data:
                    #     save_to_excel_single(data)  # Save the scraped data immediately
                        # Add the system name to the set to avoid reprocessing in the same run
                        # existing_system_names.add(system_name)
                except TimeoutException:
                    logging.error(f"Timeout while accessing link: {link}. Skipping this link.")
                except Exception as e:
                    logging.error(f"Unexpected error while processing link: {link}. Error: {e}")
        else:
            logging.info("No system links to scrape.")
    finally:
        driver.quit()
        logging.info("Browser closed.")

 