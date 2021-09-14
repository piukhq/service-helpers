import sys
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


DJANGO_BASE_URL = "https://api.dev.gb.bink.com/admin/"


# Start by getting a list of all IDs from the selected file

file_name = sys.argv[1]

with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    scheme_account_ids = []

    next(csv_reader)  # Skip the first row of the CSV file.
    for row in csv_reader:
        scheme_account_ids.append(row[0])


# Configure Chrome to persist cookies otherwise Azure SSO blocks

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)


# Iterate over all scheme accounts, visit the filters page, refresh scheme account

for scheme_account_id in scheme_account_ids:
    url = f"{DJANGO_BASE_URL}scheme/schemeaccount/?id={scheme_account_id}"
    driver.get(url)

    # Steps recorded in Selenium IDE
    driver.find_element(By.NAME, "_selected_action").click()
    driver.find_element(By.NAME, "action").click()
    dropdown = driver.find_element(By.NAME, "action")
    dropdown.find_element(By.XPATH, "//option[. = 'Refresh scheme account information']").click()
    driver.find_element(By.NAME, "index").click()

driver.quit()
