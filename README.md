# Service Helpers

Scripts to help Service Team with various functions

## Script 1: chromedriver

Install or update the install of chromedriver on this Mac. This matches the version of chromedriver to the major version of Chrome you have installed.

## Script 2: Compare

This script compares all CSV files in the data directory and will print the IDs of all scheme accounts that are present across all files.

Run this script by running `helper compare` with the CSV files inside a directory called `data` at the same location.

Expected CSV format (header row is ignored):

|Scheme account id|Extra gubbins|More gubbins|
|---|---|---|
|12345|ABC123|XYZ999|

Only the first column is read. Only CSV files will be checked.

Example output:

```
{'321594', '305106', '295978', '294927', '296305', '301249'}
```

## Script 3: Login

Use this to login to Django Admin, exits if it detects the Django Admin Index page.

## Script 4: Refresh

This script runs Selenium to automate the balance refresh process. Django has an option to trigger a balance refresh for selected account. Currently, ops take a list of IDs, manually visit a filtered page with just that ID and run the refresh. I recorded this process using Selenium IDE and then built a function to import the IDs of the scheme accounts. This simply loads in those IDs, generates URLs and does the same balance process that is otherwise being performed manually.

Run this script by passing in a CSV file with the list of scheme account IDs:
`helper refresh --filename example_file.csv --kind csv`

Expected CSV format (header row is ignored):

|Scheme account id|Extra gubbins|More gubbins|
|---|---|---|
|12345|ABC123|XYZ999|

Only the first column is read. Only CSV files will be checked.

The first time you run this you will need to authenticate through Azure SSO. Session persistence is setup so your local instance won't need to perform this step every time.
