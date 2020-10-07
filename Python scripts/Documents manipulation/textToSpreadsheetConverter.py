# textToSpreadsheetConverter.py insert texts content into spreadsheet
# one line of text per row, each column per text file
import sys, logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s -  %(levelname)s -  %(message)s"
)
# Get key filename from command line.

if len(sys.argv) > 1 and open(f"{sys.argv[1:][0]}.txt", "r"):
    # Get arguments from command line.
    filename = sys.argv[1:][0]
else:
    print("Please, introduce existing filename in command lines")
    sys.exit(1)
# While loop for loading every text f'{filename}{index}.txt'
txtDict = {}
idx = 0
while True:
    try:
        if not idx:
            textFile = open(f"{filename}.txt", "r")
        else:
            textFile = open(f"{filename}{idx}.txt", "r")
        # Create list of string lines from text and save on text dictionary.
        txtDict[f"{filename}{idx}"] = textFile.readlines()
        logging.debug("loaded file: " + filename + str(idx))
        logging.debug(txtDict[f"{filename}{idx}"])
        textFile.close()
        idx += 1
    except:
        print("No more files found")
        break
# Create workbook and sheet.
from openpyxl import Workbook
from openpyxl.styles import Font

wb = Workbook()
ws = wb.active
ws.title = filename
# Loop through dictionary and insert file's texts on workbook.
for i, file in enumerate(txtDict, start=1):
    for j, string in enumerate(txtDict[file], start=1):
        currentRow = ws.cell(row=j, column=i, value=string)
        if j == 1:
            fontObj = Font(name="Arial", size=12, bold=True)
            currentRow.font = fontObj
# Save workbook.
wb.save(filename + ".xlsx")
print("Workbook created and saved in local dir!")
