#! python 3
#Evalue input password strenght

import re

# Evaluate input password
passwordRegex= re.compile(r'''(
^(?=.*[A-Z])   #Assert at least one uppercased character
(?=.*[!@#$&*]) #Assert at least one special character
(?=.*[0-9])    #Assert at least one number
(?=.*[a-z])    #Assert at least one lowercased character
\S{8,}$        #At least 8 characters
)''',re.VERBOSE)


while True:
    print('='*30)
    print('Introduce a password to evalue')
    print('='*30)
    password=input()
    if passwordRegex.search(password):
        print('This is fine!')
        break
    else:
        print('Not good enough.')

        
