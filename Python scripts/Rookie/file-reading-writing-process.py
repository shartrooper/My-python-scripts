#The File Reading/Writing Process
'''
The pathlib module’s read_text() method returns a string of the full contents of a text file.
Its write_text() method creates a new text file (or overwrites an existing one) with the string
passed to it. Enter the following into the interactive shell:
'''

from pathlib import Path
p = Path('spam.txt')
p.write_text('Hello, world!')
13  #The 13 that write_text() returns indicates that 13 characters were written to the file
p.read_text()

'Hello, world!'

'''
There are three steps to reading or writing files in Python:

Call the open() function to return a File object.
Call the read() or write() method on the File object.
Close the file by calling the close() method on the File object.

'''

helloFile = open(Path.home() / 'hello.txt')

helloFile = open('C:\\Users\\your_home_folder\\hello.txt') # The open() function can also accept strings


##Reading the Contents of Files

helloContent = helloFile.read()
helloContent
'Hello, world!'

#If you think of the contents of a file as a single large string value,
#the read() method returns the string that is stored in the file.

#Alternatively, you can use the readlines() method to get a list of string values from the file, one string for each line of text.
'''
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
'''

sonnetFile = open(Path.home() / 'sonnet29.txt')
sonnetFile.readlines()
'''
[When, in disgrace with fortune and men's eyes,\n', ' I all alone beweep my
outcast state,\n', And trouble deaf heaven with my bootless cries,\n', And
look upon myself and curse my fate,']
'''

## Writing to Files


baconFile = open('bacon.txt', 'w')  # Write mode. Since there isn’t a bacon.txt yet, Python creates one.
baconFile.write('Hello, world!\n') #  writes the string to the file and returns the number of characters written
#13
baconFile.close()
baconFile = open('bacon.txt', 'a') # To add text to the existing contents of the file instead of replacing the string we just wrote, we open the file in append mode.
baconFile.write('Bacon is not a vegetable.')
#25
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
'''
Hello, world!
Bacon is not a vegetable.
'''

##Saving Variables with the shelve Module

'''
You can save variables in your Python programs to binary shelf files using the shelve module.
For example, if you ran a program and entered some configuration settings, you could save those
settings to a shelf file and then have the program load them the next time it is run.
'''


import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

#Shelf values don’t have to be opened in read or write mode—they can do both once opened.
#Enter the following into the interactive shell:

shelfFile = shelve.open('mydata')
type(shelfFile)
<class 'shelve.DbfilenameShelf'>
shelfFile['cats']
#['Zophie', 'Pooka', 'Simon']
shelfFile.close()


'''
Just like dictionaries, shelf values have keys() and values() methods that will return list-like values of the keys and values in the shelf.
Since these methods return list-like values instead of true lists, you should pass them to the list() function to get them in list form.
'''

shelfFile = shelve.open('mydata')
list(shelfFile.keys())
['cats']
list(shelfFile.values())
[['Zophie', 'Pooka', 'Simon']]
shelfFile.close()


## Saving Variables with the pprint.pformat() Function
#Not only is this string formatted to be easy to read, but it is also syntactically correct Python code.

import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
#83
fileObj.close()

# Since Python scripts are themselves just text files with the .py file extension, your Python programs can even generate other Python programs. You can then import these files into scripts.


import myCats
myCats.cats
[{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
myCats.cats[0]
{'name': 'Zophie', 'desc': 'chubby'}
myCats.cats[0]['name']
'Zophie'





