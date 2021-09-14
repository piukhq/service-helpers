# ops-balance-helpers

Scripts to help Ops with the current account balance refresh process.

## Script 1: Compare

This script compares all CSV files in the data directory and will print the IDs of all scheme accounts that are present across all files.

Run this script by running `compare.py` with the CSV files inside a directory called `data` at the same location.

Expected CSV format (header row is ignored):

|Scheme account id|Extra gubbins|More gubbins|
|---|---|---|
|12345|ABC123|XYZ999|

Only the first column is read. Only CSV files will be checked.

Example output:

```
{'321594', '305106', '295978', '294927', '296305', '301249'}
```


## Script 2: Refresh

This script runs Selenium to automate the balance refresh process. Django has an option to trigger a balance refresh for selected account. Currently, ops take a list of IDs, manually visit a filtered page with just that ID and run the refresh. I recorded this process using Selenium IDE and then built a function to import the IDs of the scheme accounts. This simply loads in those IDs, generates URLs and does the same balance process that is otherwise being performed manually.

Requries Selenium to be setup and the `chromedriver` to be included in the same directory as `refresh.py`. This can be downloaded [here](https://sites.google.com/chromium.org/driver/).

Run this script by passing in a CSV file with the list of scheme account IDs: `refresh accounts.csv`

Expected CSV format (header row is ignored):

|Scheme account id|Extra gubbins|More gubbins|
|---|---|---|
|12345|ABC123|XYZ999|

Only the first column is read. Only CSV files will be checked.

The first time you run this you will need to authenticate through Azure SSO. Session persistence is setup so your local instance won't need to perform this step every time.