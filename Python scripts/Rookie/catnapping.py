##Multiline Strings with Triple Quotes

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

#Another way to write comments
"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""

spam = 'Hello, world!'
print(spam[0:5])
'Hello'
print(spam[:5])
'Hello'
print(spam[7:])
'world!'

#String interpolation

name = 'Al'
age = 4000
print('My name is %s. I am %s years old.' % (name, age))

#Python 3.6+ f-string
print(f'My name is {name}. Next year I will be {age + 1}.')


print(spam.upper())
'HELLO, WORLD!'
print(spam.lower())
'hello, world!'

print(spam.islower())
#False
print(spam.isupper())
#False
print('HELLO'.isupper())
#True
print('abc12345'.islower())
#True
print('12345'.islower())
#False
print('12345'.isupper())
#False

#isalpha() Returns True if the string consists only of letters and isn’t blank.

#isalnum() Returns True if the string consists only of letters and numbers and is not blank.

#isdecimal() Returns True if the string consists only of numeric characters and is not blank.

#isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank.

#istitle() Returns True if the string consists only of words that begin with an uppercase letter
#followed by only lowercase letters.

'''The startswith() and endswith() methods return True if the string value they are called on begins
or ends (respectively) with the string passed to the method; otherwise, they return False.'''

print('Hello, world!'.startswith('Hello'))
#True
print('Hello, world!'.endswith('world!'))
#True
print('abc123'.startswith('abcdef'))
#False
print('abc123'.endswith('12'))
#False

#The join() and split() Methods

print(', '.join(['cats', 'rats', 'bats']))
#'cats, rats, bats'

print('My name is Simon'.split())
#['My', 'name', 'is', 'Simon']


mail = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''
print(mail.split('\n'))

#Splitting Strings with the partition() Method
#Returns a tuple of three substrings for the “before,” “separator,” and “after” substrings. 

print('Hello, world!'.partition('o'))
#('Hell', 'o', ', world!')


#Justifying Text with the rjust(), ljust(), and center() Methods
print('Hello'.rjust(10))
#'     Hello'
print('Hello'.rjust(20))
#'              Hello'
print('Hello, World'.rjust(20))
#'         Hello, World'
print('Hello'.ljust(10))
#'Hello     '

print('Hello'.rjust(20, '*'))
#'***************Hello'

# The center() string method works like ljust() and rjust() but centers the text rather than justifying it to the left or right.

print('Hello'.center(20))
#'       Hello        '
print('Hello'.center(20, '='))
#'=======Hello========'

#Removing Whitespace with the strip(), rstrip(), and lstrip() Methods

spaced = '    Hello, World    '
print(spaced.strip())
#'Hello, World'
print(spaced.lstrip())
#'Hello, World    '
print(spam.rstrip())
#'    Hello, World'
spammed = 'SpamSpamBaconSpamEggsSpamSpam'
print(spammed.strip('ampS'))
#'BaconSpamEggs'


#Numeric Values of Characters with the ord() and chr() Functions

print(ord('A'))
#65
print(ord('4'))
#52
print(ord('!'))
#33
print(chr(65))
#'A'

print(ord('B'))
#66
print(ord('A') < ord('B'))
#True
print(chr(ord('A')))
#'A'
print(chr(ord('A') + 1))
#'B'


'''If you’d like to know more, I recommend watching Ned Batchelder’s 2012 PyCon talk,
“Pragmatic Unicode, or, How Do I Stop the Pain?” at https://youtu.be/sgHbC6udIqc.'''


