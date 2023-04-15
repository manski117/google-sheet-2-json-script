# you may need to run this command in your local env: `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
from google.colab import auth
from googleapiclient.discovery import build
import json

# Authenticate with Google (popup should appear)
auth.authenticate_user()

# Set up access to the Sheets API
def get_sheet_data(spreadsheet_id, sheet_name):
    service = build('sheets', 'v4')

    # Get cell values (computed)
    result_vals = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=sheet_name,
        valueRenderOption='UNFORMATTED_VALUE'
    ).execute()
    values = result_vals.get('values', [])

    # Get formulas (if present)
    result_formulas = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=sheet_name,
        valueRenderOption='FORMULA'
    ).execute()
    formulas = result_formulas.get('values', [])

    return values, formulas

# Convert to structured dictionary with cell references
def to_cell_dict(values, formulas):
    data = {}
    for row_idx, (val_row, formula_row) in enumerate(zip(values, formulas), start=1):
        for col_idx, (val, formula) in enumerate(zip(val_row, formula_row), start=1):
            col_letter = chr(ord('A') + col_idx - 1)
            coord = f"{col_letter}{row_idx}"
            data[coord] = {
                "value": val,
                "formula": formula if isinstance(formula, str) and formula.startswith('=') else None
            }
    return data

# Paste your Sheet ID and Sheet Name here
SPREADSHEET_ID = '_'  # e.g., '1fVNh...yourID...AiM'
SHEET_NAME = 'Sheet1'  # e.g., 'Budget2025'

# Fetch and print data
values, formulas = get_sheet_data(SPREADSHEET_ID, SHEET_NAME)
sheet_data = to_cell_dict(values, formulas)

# Output result
print(json.dumps(sheet_data, indent=2))
