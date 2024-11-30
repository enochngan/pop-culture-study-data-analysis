import pandas as pd

# Load the Excel file
excel_file = "/Users/enochngan/Downloads/nora_roberts_linreg_copy/epigraphs_dedications.xlsx"

# Specify the sheets to save
sheets_to_save = ["Epigraphs"]

for sheet_name in sheets_to_save:
    # Read the specific sheet
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Save the sheet to a CSV file
    csv_file = f"{sheet_name}.csv"  # Name CSV file based on the sheet name
    df.to_csv(csv_file, index=False)

    print(f"Saved {sheet_name} as {csv_file}")
