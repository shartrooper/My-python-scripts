# blankRowInserter.py takes two integers and a filename string as command line arguments.
# N is starting row. M is the num of blank spaces to insert.
# example blankRowInserter.py 3 2 multTable.xlsx
from openpyxl import load_workbook
import sys

# take N number argument from command line.
if len(sys.argv) > 3:
    # Get arguments from command line.
    n, m, filename = sys.argv[1:]
else:
    print("Please, introduce number N, M and input filename in command line")
    sys.exit(1)
# Load wordBook filename
try:
    wb = load_workbook(filename)
    ws = wb.active
except Exception as err:
    print('An exception happened : \n'+str(err))
    sys.exit(1)

# Insert blank row cells in file WorkBook
ws.insert_rows(int(n),amount=int(m))

# Save changes
wb.save(filename)
print('Workbooks updated!')
