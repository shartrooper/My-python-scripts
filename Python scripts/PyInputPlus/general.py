# PyInputPlus module
'''
If no errors appear when you import the module, it has been successfully installed.

PyInputPlus has several functions for different kinds of input:

inputStr() Is like the built-in input() function but has the general PyInputPlus features. You can also pass a custom validation function to it

inputNum() Ensures the user enters a number and returns an int or float, depending on if the number has a decimal point in it

inputChoice() Ensures the user enters one of the provided choices

inputMenu() Is similar to inputChoice(), but provides a menu with numbered or lettered options

inputDatetime() Ensures the user enters a date and time

inputYesNo() Ensures the user enters a “yes” or “no” response

inputBool() Is similar to inputYesNo(), but takes a “True” or “False” response and returns a Boolean value

inputEmail() Ensures the user enters a valid email address

inputFilepath() Ensures the user enters a valid file path and filename, and can optionally check that a file with that name exists

inputPassword() Is like the built-in input(), but displays * characters as the user types so that passwords, or other sensitive information, aren’t displayed on the screen

These functions will automatically reprompt the user for as long as they enter invalid input:
'''

import pyinputplus as pyip

response = pyip.inputNum('Enter a number: ')
# if input five
#'five' is not a number.
# if input 42
print(response)
#42

response = pyip.inputNum('Enter num: ', min=4)
response = pyip.inputNum('Enter num: ', greaterThan=4)
response = pyip.inputNum('>', min=4, lessThan=6)

##By default, blank input isn’t allowed unless the blank keyword argument is set to True

response = pyip.inputNum('Enter num: ')
#Enter num:(blank input entered here)
#Blank values are not allowed.

response = pyip.inputNum(blank=True)
#(blank input entered here)
print(response)

##The limit, timeout, and default Keyword Arguments

response = pyip.inputNum(limit=2)
'''blah
'blah' is not a number.
Enter num: number
'number' is not a number.
Traceback (most recent call last):
    --snip--
pyinputplus.RetryLimitException'''

response = pyip.inputNum(timeout=10)
'''42 (entered after 10 seconds of waiting)
Traceback (most recent call last):
    --snip--
pyinputplus.TimeoutException'''

##When you use these keyword arguments and also pass a default keyword argument, the function returns the default value instead of raising an exception.

response = pyip.inputNum(limit=2, default='N/A')
'''
hello
'hello' is not a number.
world
'world' is not a number.
>>> response
'N/A'
'''




# The allowRegexes and blockRegexes Keyword Arguments

response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
'''XLII
>>> response
'XLII'
'''
response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
'''xlii
>>> response
'xlii'
'''

response = pyip.inputNum(blockRegexes=[r'[02468]$'])
'''42
This response is invalid.
44
This response is invalid.
43
>>> response
43
'''

response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'],
blockRegexes=[r'cat'])
#If you specify both an allowRegexes and blockRegexes argument, the allow list overrides the block list.
'''cat
This response is invalid.
catastrophe
This response is invalid.
category
>>> response
'category'
'''


##Passing a Custom Validation Function to inputCustom()
'''
For example, we can create our own addsUpToTen() function, and then pass it to inputCustom().
Note that the function call looks like inputCustom(addsUpToTen) and
not inputCustom(addsUpToTen()) because we are passing the addsUpToTen() function itself to inputCustom(),
not calling addsUpToTen() and passing its return value.
'''

def addsUpToTen(numbers):
   numbersList = list(numbers)
   for i, digit in enumerate(numbersList):
     numbersList[i] = int(digit)
   if sum(numbersList) != 10:
     raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
   return int(numbers) # Return an int form of numbers.


response = pyip.inputCustom(addsUpToTen) # No parentheses after addsUpToTen here.
'''
123
The digits must add up to 10, not 6.
1235
The digits must add up to 10, not 11.
1234
>>> response # inputStr() returned an int, not a string.
1234
>>> response = pyip.inputCustom(addsUpToTen)
hello
invalid literal for int() with base 10: 'h'
55
>>> response
'''




