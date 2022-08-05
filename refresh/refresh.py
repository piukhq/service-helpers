import csv
import click
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By


@click.command()
@click.option("--filename", help="Specify the filename to run")
@click.option("--kind", default="csv", help="Should be one of tableau or csv")
def main(filename, kind):
    if kind == "csv":
        with open(filename, "r") as f:
            data = f.read()
    elif kind == "tableau":
        with open(filename, "r", encoding="utf-16") as f:
            data = f.read()
    else:
        print("Unknown type, please use one of csv or tableau")
        exit()

    csvdata = csv.reader(data.splitlines(), delimiter="\t")
    ids = []

    next(csvdata)  # Skip the first row of the CSV file.
    for row in csvdata:
        ids.append(row[0])

    # Configure Chrome to persist cookies otherwise Azure SSO blocks

    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=selenium")
    driver = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver", options=chrome_options)

    # Iterate over all scheme accounts, visit the filters page, refresh scheme account

    count = 0
    for scheme_account_id in ids:
        count = count + 1
        print(f'Processing ID {count} of {len(ids)}')
        url = f"https://api.gb.bink.com/admin/scheme/schemeaccount/?id={scheme_account_id}"
        driver.get(url)

        # Steps recorded in Selenium IDE
        driver.find_element(By.NAME, "_selected_action").click()
        driver.find_element(By.NAME, "action").click()
        dropdown = driver.find_element(By.NAME, "action")
        dropdown.find_element(By.XPATH, "//option[. = 'Refresh scheme account information']").click()
        driver.find_element(By.NAME, "index").click()

    driver.quit()


if __name__ == "__main__":
    main()
