##ORGANIZING FILES

#The shutil Module

'''
The shutil (or shell utilities) module has functions to let you
copy, move, rename, and delete files in your Python programs.
'''

import shutil, os
from pathlib import Path
p = Path.home()
shutil.copy(p / 'spam.txt', p / 'some_folder')
'C:\\Users\\Al\\some_folder\\spam.txt'
shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')
#WindowsPath('C:/Users/Al/some_folder/eggs2.txt')


#shutil.copytree()
'''
will copy an entire folder and every folder and file contained in it.
Calling shutil.copytree(source, destination) will copy the folder at the
path source, along with all of its files and subfolders, to the folder at
the path destination. The source and destination parameters are both strings.
The function returns a string of the path of the copied folder.
'''

p = Path.home()
shutil.copytree(p / 'spam', p / 'spam_backup')
#WindowsPath('C:/Users/Al/spam_backup')
'''
creates a new folder named spam_backup with the same content
as the original spam folder
'''

## Moving and Renaming Files and Folders

'''
Calling shutil.move(source, destination) will move the file or folder
at the path source to the path destination and will return a string
of the absolute path of the new location.
'''

shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs\\bacon.txt'

# If there had been a bacon.txt file already in C:\eggs, it would have been overwritten.
#The destination path can also specify a filename. In the following example, the source file is moved and renamed.

shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
'C:\\eggs\\new_bacon.txt'
#Move C:\bacon.txt into the folder C:\eggs, also rename that bacon.txt file to new_bacon.txt.

#Both of the previous examples worked under the assumption that there was a folder eggs in the C:\ directory.
#But if there is no eggs folder, then move() will rename bacon.txt to a file named eggs.

shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs'  #move() can’t find a folder named eggs in the C:\ directory and so assumes that destination must be specifying a filename, not a folder.


## Permanently Deleting Files and Folders

'''
You can delete a single file or a single empty folder with functions in the os module, whereas to delete a folder and all of its contents, you use the shutil module.

    Calling os.unlink(path) will delete the file at path.
    Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
    Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

Be careful when using these functions in your programs! It’s often a good idea to first run your program with these calls commented out and with print() calls added to show the files that would be deleted.
'''

for filename in Path.home().glob('*.rxt'):
    os.unlink(filename)


## Safe Deletes with the send2trash Module

'''
A much better way to delete files and folders is with the third-party send2trash module.
You can install this module by running pip install --user send2trash from a Terminal window.
'''

import send2trash
baconFile = open('bacon.txt', 'a')   # creates the file
baconFile.write('Bacon is not a vegetable.')
25
baconFile.close()
send2trash.send2trash('bacon.txt')

## Walking a Directory Tree

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')

'''
The os.walk() function is passed a single string value: the path of a folder. You can use os.walk() in a for loop statement to walk a directory tree,
much like how you can use the range() function to walk over a range of numbers. Unlike range(), the os.walk() function will return three values on each iteration through the loop:

    A string of the current folder’s name
    A list of strings of the folders in the current folder
    A list of strings of the files in the current folder

'''

#When you run this program, it will output the following:
'''
The current folder is C:\delicious
SUBFOLDER OF C:\delicious: cats
SUBFOLDER OF C:\delicious: walnut
FILE INSIDE C:\delicious: spam.txt

The current folder is C:\delicious\cats
FILE INSIDE C:\delicious\cats: catnames.txt
FILE INSIDE C:\delicious\cats: zophie.jpg

The current folder is C:\delicious\walnut
SUBFOLDER OF C:\delicious\walnut: waffles

The current folder is C:\delicious\walnut\waffles
FILE INSIDE C:\delicious\walnut\waffles: butter.txt.
'''

## Compressing Files with the zipfile Module

'''
ZipFile objects are conceptually similar to the File objects you saw returned by the open() function in the previous chapter:
they are values through which the program interacts with the file. To create a ZipFile object, call the zipfile.ZipFile() function,
passing it a string of the .ZIP file’s filename. Note that zipfile is the name of the Python module, and ZipFile() is the name of the function.
'''

import zipfile

p = Path.home()
exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.namelist()
['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
13908
spamInfo.compress_size
3828
f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!'#fstring interpolation
'Compressed file is 3.63x smaller!'
exampleZip.close()

## Extracting from ZIP Files

p = Path.home()
exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.extractall()
exampleZip.close()

'''
After running this code, the contents of example.zip will be extracted to C:\.
Optionally, you can pass a folder name to extractall() to have it extract the files into a folder other than the current working directory.
If the folder passed to the extractall() method does not exist, it will be created.
'''


exampleZip.extract('spam.txt')
'C:\\spam.txt'
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
'C:\\some\\new\\folders\\spam.txt'
exampleZip.close()


'''
The string you pass to extract() must match one of the strings in the list returned by namelist().
Optionally, you can pass a second argument to extract() to extract the file into a folder other than the current working directory.
If this second argument is a folder that doesn’t yet exist, Python will create the folder. The value that extract() returns is
the absolute path to which the file was extracted.
'''

## Creating and Adding to ZIP Files

# This code will create a new ZIP file named new.zip that has the compressed contents of spam.txt.
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


