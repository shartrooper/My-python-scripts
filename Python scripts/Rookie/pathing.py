from pathlib import Path
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\Al', filename))
    
#C:\Users\Al\accounts.txt
#C:\Users\Al\details.csv
#C:\Users\Al\invite.docx

Path('spam', 'bacon', 'eggs')

#WindowsPath('spam/bacon/eggs')

str(Path('spam', 'bacon', 'eggs'))
'spam\\bacon\\eggs'


Path('spam') / 'bacon' / 'eggs'
#WindowsPath('spam/bacon/eggs')
Path('spam') / Path('bacon/eggs')
#WindowsPath('spam/bacon/eggs')
Path('spam') / Path('bacon', 'eggs')
#WindowsPath('spam/bacon/eggs')

homeFolder = Path('C:/Users/Al')
subFolder = Path('spam')
homeFolder / subFolder
WindowsPath('C:/Users/Al/spam')
str(homeFolder / subFolder)
'C:\\Users\\Al\\spam'

#The Current Working Directory

import os
Path.cwd()
#WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')'
os.chdir('C:\\Windows\\System32')
Path.cwd()
#WindowsPath('C:/Windows/System32')

#The Home Directory

Path.home()
#WindowsPath('C:/Users/Al')

#Creating New Folders Using the os.makedirs() Function

import os
os.makedirs('C:\\delicious\\walnut\\waffles')

Path(r'C:\Users\Al\spam').mkdir()


# Handling Absolute and Relative Paths

Path.cwd()
WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')
Path.cwd().is_absolute()
True
Path('spam/bacon/eggs').is_absolute()
False


os.path.abspath('.')
'C:\\Users\\Al\\AppData\\Local\\Programs\\Python\\Python37'
os.path.abspath('.\\Scripts')
'C:\\Users\\Al\\AppData\\Local\\Programs\\Python\\Python37\\Scripts'
os.path.isabs('.')
False
os.path.isabs(os.path.abspath('.'))
True


os.path.relpath('C:\\Windows', 'C:\\')
'Windows'
os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
'..\\..\\Windows'


#Getting the Parts of a File Path

p = Path('C:/Users/Al/spam.txt')
p.anchor
'C:\\'
p.parent # This is a Path object, not a string.
WindowsPath('C:/Users/Al')
p.name
'spam.txt'
p.stem
'spam'
p.suffix
'.txt'
p.drive
'C:'

##The parents attribute (which is different from the parent attribute) evaluates to the ancestor folders of a Path object with an integer index:

Path.cwd()
#WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')
Path.cwd().parents[0]
#WindowsPath('C:/Users/Al/AppData/Local/Programs/Python')
Path.cwd().parents[1]
#WindowsPath('C:/Users/Al/AppData/Local/Programs')
Path.cwd().parents[2]
#WindowsPath('C:/Users/Al/AppData/Local')
Path.cwd().parents[3]
#WindowsPath('C:/Users/Al/AppData')
Path.cwd().parents[4]
#WindowsPath('C:/Users/Al')
Path.cwd().parents[5]
#WindowsPath('C:/Users')
Path.cwd().parents[6]
#WindowsPath('C:/')


#The older os.path module also has similar functions for getting the different parts of a path written in a string value.


calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(calcFilePath)
#'calc.exe'
os.path.dirname(calcFilePath)
#'C:\\Windows\\System32'

#If you need a path’s dir name and base name together, you can just call os.path.split() to get a tuple

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.split(calcFilePath)
#('C:\\Windows\\System32', 'calc.exe')

'''
Also, note that os.path.split() does not take a file path and return a list of strings of each folder.
For that, use the split() string method and split on the string in os.sep. (Note that sep is in os, not os.path.)
The os.sep variable is set to the correct folder-separating slash for the computer running the program, '\\' on Windows
and '/' on macOS and Linux, and splitting on it will return a list of the individual folders.
'''

calcFilePath.split(os.sep)
#['C:', 'Windows', 'System32', 'calc.exe']

##Finding File Sizes and Folder Contents

'''
The os.path module provides functions for finding the size of a file in bytes and the files and folders inside a given folder:


    Calling os.path.getsize(path) will return the size in bytes of the file in the path argument.
    Calling os.listdir(path) will return a list of filename strings for each file in the path argument. (Note that this function is in the os module, not os.path.)

'''


os.path.getsize('C:\\Windows\\System32\\calc.exe')
#27648
os.listdir('C:\\Windows\\System32')
#['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
#--snip--
#'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)


##Modifying a List of Files Using Glob Patterns


p = Path('C:/Users/Al/Desktop')
p.glob('*')
#<generator object Path.glob at 0x000002A6E389DED0>
#The asterisk (*) stands for “multiple of any characters,”
#so p.glob('*') returns a generator of all files in the path stored in p.
'''
list(p.glob('*')) # Make a list from the generator.
[WindowsPath('C:/Users/Al/Desktop/1.png'), WindowsPath('C:/Users/Al/
Desktop/22-ap.pdf'), WindowsPath('C:/Users/Al/Desktop/cat.jpg'),
  --snip--
WindowsPath('C:/Users/Al/Desktop/zzz.txt')]
'''

list(p.glob('*.txt') # Lists all text files.
'''
[WindowsPath('C:/Users/Al/Desktop/foo.txt'),
  --snip--
WindowsPath('C:/Users/Al/Desktop/zzz.txt')]
'''

#In contrast with the asterisk, the question mark (?) stands for any single character:
list(p.glob('project?.docx')
'''
[WindowsPath('C:/Users/Al/Desktop/project1.docx'), WindowsPath('C:/Users/Al/
Desktop/project2.docx'),
  --snip--
WindowsPath('C:/Users/Al/Desktop/project9.docx')]
'''

list(p.glob('*.?x?') #will return files with any name and any three-character extension where the middle character is an 'x'.
'''
[WindowsPath('C:/Users/Al/Desktop/calc.exe'), WindowsPath('C:/Users/Al/
Desktop/foo.txt'),
  --snip--
WindowsPath('C:/Users/Al/Desktop/zzz.txt')]
'''

p = Path('C:/Users/Al/Desktop')
for textFilePathObj in p.glob('*.txt'):
    print(textFilePathObj) # Prints the Path object as a string.
    # Do something with the text file.
    # .....
'''
C:\Users\Al\Desktop\foo.txt
C:\Users\Al\Desktop\spam.txt
C:\Users\Al\Desktop\zzz.txt
'''


##Checking Path Validity
'''
Many Python functions will crash with an error if you supply them with a path that does not exist.
Luckily, Path objects have methods to check whether a given path exists and whether it is a file or folder.
Assuming that a variable p holds a Path object, you could expect the following:

    Calling p.exists() returns True if the path exists or returns False if it doesn’t exist.
    Calling p.is_file() returns True if the path exists and is a file, or returns False otherwise.
    Calling p.is_dir() returns True if the path exists and is a directory, or returns False otherwise.
    
'''

#You can determine whether there is a DVD or flash drive currently attached to the computer by checking for it with the exists() method.

winDir.exists()
#True
winDir.is_dir()
#True
notExistsDir.exists()
#False
calcFile.is_file()
#True
calcFile.is_dir()
#False


winDir = Path('C:/Windows')
notExistsDir = Path('C:/This/Folder/Does/Not/Exist')
calcFile = Path('C:/Windows/System32/calc.exe')

