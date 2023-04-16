# Script for converting google sheets to json format
I wrote this because I needed some way to download google sheet data with formulas in-tact in a JSON format so that google sheet and excel formulas can be fed to an LLM with full context preserved.

## Setup:
1. Make sure you have a valid google account with a google sheet you want to extract data from, and a google project running in google cloud.

### Setup google cloud credentials
1. In the left nav: APIs & Services → Credentials
1. Click “Create Credentials” → choose OAuth client ID
1. Choose Desktop app or Web App depending on use case
1. Download the .json file — this contains your client ID and secret ID. (save these!)


### Running the script
1. Remember to run `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
1. Make sure your cell range is properly defined in `range_notation` on line 15. For instance, if the actual cells you want to convert to JSON are only A1 through O26, then you should explicitly define that as `range_notation = f"{sheet_name}!A1:O26"` or else you may get an error. (**I highly recommend narrowly defining this** or else you may get a thousand blank cells in your JSON that you don't need)
1. Make sure that `SPREADSHEET_ID` contains the link to your actual spreadsheet ID. This is the long string of characters and numbers in the link to your google sheets between the `spreadsheets/d/` and the `/edit?` sections.
1. Make sure that your value for `SHEET_NAME` matches the name of your sheet's name *exactly*. If you don't know what this is, this is the name of the actual tab at the bottom of the screen (google sheets and excel files can have multiple sheets in one file. Even if you only have one sheet, this script won't know to pick that single sheet by default, so make sure the name is an exact match. For best results, consider naming your sheet to something without spaces or strange special characters).


