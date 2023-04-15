# Script for converting google sheets to json format
I wrote this because I needed some way to download google sheet data with formulas in-tact in a JSON format so that google sheet and excel formulas can be fed to an LLM with full context preserved.

## Setup:
1. Make sure you have a valid google account with a google sheet you want to extract data from, and a google project running in google cloud.

### Setup google cloud credentials
1. In the left nav: APIs & Services → Credentials
1. Click “Create Credentials” → choose OAuth client ID
1. Choose Desktop app or Web App depending on use case
1. Download the .json file — this contains your client ID and secret ID. (save these!)


