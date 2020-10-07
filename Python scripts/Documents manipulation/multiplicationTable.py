# multiplicationTable.py takes a number N from the command line
# and creates an N×N multiplication table in an Excel spreadsheet.

from openpyxl import Workbook
import sys

# take N number argument from command line.
if len(sys.argv) > 1:
    # Get number from command line.
    numN = int(sys.argv[1:][0])
else:
    print("Please, introduce a number as argument in command line")
wb = Workbook()
ws = wb.active
ws.title = "Multiplication table %s" % (numN)
mult = 0
# Create and loop through spreadsheet Object
# inserting NxN multiplication table
def evalNum(n, multiplier):
    if n == 1 and multiplier == 0:
        return ""
    elif multiplier:
        return n * multiplier
    else:
        return n


for i in range(1, numN + 2):
    for j in range(1, numN + 2):
        ws.cell(row=i, column=j, value=evalNum(j, mult))
    mult += 1
# save on output file
wb.save("multTable.xlsx")
print('Workbooks created and saved in local dir!')
