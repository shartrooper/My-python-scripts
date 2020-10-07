## Raising Exceptions

raise Exception('This is the error message.')
'''
  File "<pyshell#191>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.
'''

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
       raise Exception('Symbol must be a single character string.')
    if width <= 2:
       raise Exception('Width must be greater than 2.')
    if height <= 2:
       raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

    for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
        try:
            boxPrint(sym, w, h)
        except Exception as err:
            print('An exception happened: ' + str(err))

## Getting the Traceback as a String

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

spam()

'''
Traceback (most recent call last):
  File "errorExample.py", line 7, in <module>
    spam()
  File "errorExample.py", line 2, in spam
    bacon()
  File "errorExample.py", line 5, in bacon
    raise Exception('This is the error message.')
Exception: This is the error message.
'''


import traceback
try:
...          raise Exception('This is the error message.')
except:
...          errorFile = open('errorInfo.txt', 'w')
...          errorFile.write(traceback.format_exc())
...          errorFile.close()
...          print('The traceback info was written to errorInfo.txt.')


#111
#The traceback info was written to errorInfo.txt.

'''
The 111 is the return value from the write() method,
since 111 characters were written to the file.
The traceback text was written to errorInfo.txt.
'''

## Assertions

'''
 An assert statement consists of the following:

    The assert keyword
    A condition (that is, an expression that evaluates to True or False)
    A comma
    A string to display when the condition is False
'''

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
ages
#[73, 47, 80, 17, 15, 22, 54, 92, 57, 26]
assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
'''
#Unlike exceptions, your code should not handle assert statements with try and except;
#if an assert fails, your program should crash.

'''
Assertions are for programmer errors, not user errors.
Assertions should only fail while the program is under development; a user should never see an assertion error in a finished program.
'''

## LOGGING

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
'''
When Python logs an event, it creates a LogRecord object that holds information about that event.
The logging module’s basicConfig() function lets you specify what details about the LogRecord object
you want to see and how you want those details displayed.
'''


## Logging Levels

'''
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Level
	

Logging function
	

Description
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

DEBUG
	

logging.debug()
	

The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.

INFO
	

logging.info()
	

Used to record information on general events in your program or confirm that things are working at their point in the program.

WARNING
	

logging.warning()
	

Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.

ERROR
	

logging.error()
	

Used to record an error that caused the program to fail to do something.

CRITICAL
	

logging.critical()
	

The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.
'''


## Disabling Logging

logging.basicConfig(level=logging.INFO, format=' %(asctime)s -%(levelname)s -  %(message)s')
logging.critical('Critical error! Critical error!')
#2019-05-22 11:10:48,054 - CRITICAL - Critical error! Critical error!
logging.disable(logging.CRITICAL)
#logging.disable() will disable all messages after it
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')

## Logging to a File
#Instead of displaying the log messages to the screen, you can write them to a text file. 
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')



