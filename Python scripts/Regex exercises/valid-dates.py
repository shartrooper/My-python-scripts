#! python3
# valid-dates.py - Finds valid dates on the clipboard.

import pyperclip, re


#Create date regex
dateRegex= re.compile(r'''(
    ([0-3]?[1-9])\/         #day
    ([0-1]?[1-9])\/         #month
    ([1-2][0-9]{3})        #year
    )''',re.VERBOSE)


#find matches in clipboard text and validate.
text=str(pyperclip.paste())

def detectSingleDigit (str):
    if len(str) < 2:
        return '0'+ str
    else:
        return str

matches=[]
for date,day,month,year in dateRegex.findall(text):
    #Validate dates
    if int(day) == 31 and (int(month) != 2 or int(month) != 4 or int(month) != 6 or int(month) != 9 or int(month) != 11)  and int(month)<= 12:
        day= detectSingleDigit(day)
        month= detectSingleDigit(month)
    elif int(day) == 29 and int(month) == 2 and (int(year)%4 == 0 and (int(year)%100 != 0) or (int(year)%100 ==0 and int(year)%400 == 0)):
        day= detectSingleDigit(day)
        month= detectSingleDigit(month)
    elif int(day) <= 28 and int(month) == 2:
        day= detectSingleDigit(day)
        month= detectSingleDigit(month)
    elif int(day)<= 30 and int(month) != 2 and int(month)<= 12:
        day= detectSingleDigit(day)
        month= detectSingleDigit(month)
    else:
        continue
    # append valid matches
    matches.append(day+'/'+month+'/'+year)


# Print valid results on List.
print(matches)
