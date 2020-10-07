##Project: mapIt.py with the webbrowser Module
"""
The webbrowser module’s open() function can launch a new browser to a specified URL.
"""
import webbrowser

webbrowser.open("https://inventwithpython.com/")

##Downloading Files from the Web with the requests Module
"""
The requests module doesn’t come with Python, so you’ll have to install it first. From the command line, run pip install --user requests.
"""

# Downloading a Web Page with the requests.get() Function
'''
The requests.get() function takes a string of a URL to download. By calling type() on requests.get()’s return value,
you can see that it returns a Response object, which contains the response that the web server gave for your request.
'''

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
<class 'requests.models.Response'>
res.status_code == requests.codes.ok
#True
len(res.text)
#178981
print(res.text[:250])# Displays only 250 characters
'''
The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare
This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Proje
'''

##Checking for Errors

res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Al\AppData\Local\Programs\Python\Python37\lib\site-packages\requests\models.py", line 940, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://inventwithpython.com/page_that_does_not_exist.html
'''
#The raise_for_status() method is a good way to ensure that a program halts if a bad download occurs.

res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
#There was a problem: 404 Client Error: Not Found for url: https://inventwithpython.com/page_that_does_not_exist.html

##Saving Downloaded Files to the Hard Drive

'''
First,open the file in write binary mode by passing the string 'wb' as the second argument to open().
Even if the page is in plaintext (such as the Romeo and Juliet text you downloaded earlier),
you need to write binary data instead of text data in order to maintain the Unicode encoding of the text.
'''

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    #The iter_content() method returns “chunks” of the content on each iteration through the loop.
    #Each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain.
    #One hundred thousand bytes is generally a good size, so pass 100000 as the argument to iter_content().
    playFile.write(chunk)
#100000
#78981
playFile.close()

## Parsing HTML with the bs4 Module

'''
Beautiful Soup is a module for extracting information from an HTML page (and is much better for this purpose than regular expressions).
run pip install --user beautifulsoup4 from the command line.
'''

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
type(exampleSoup)
<class 'bs4.BeautifulSoup'>
'''
The 'html.parser' parser used here comes with Python.
However, you can use the faster 'lxml' parser if you install the third-party lxml module.pip install --user lxml
'''

## Finding an Element with the select() Method

'''
Examples of CSS Selectors

Selector passed to the select() method
	

Will match . . .

soup.select('div')
	

All elements named <div>

soup.select('#author')
	

The element with an id attribute of author

soup.select('.notice')
	

All elements that use a CSS class attribute named notice

soup.select('div span')
	

All elements named <span> that are within an element named <div>

soup.select('div > span')
	

All elements named <span> that are directly within an element named <div>, with no other element in between

soup.select('input[name]')
	

All elements named <input> that have a name attribute with any value

soup.select('input[type="button"]')
	

All elements named <input> that have an attribute named type with value button
'''


'''
The select() method will return a list of Tag objects, which is how Beautiful Soup represents an HTML element.
The list will contain one Tag object for every match in the BeautifulSoup object’s HTML.
Tag values can be passed to the str() function to show the HTML tags they represent.
Tag values also have an attrs attribute that shows all the HTML attributes of the tag as a dictionary.
'''

#Using the example.html

import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
type(elems) # elems is a list of Tag objects.
<class 'list'>
len(elems)
type(elems[0])
<class 'bs4.element.Tag'>
str(elems[0]) # The Tag object as a string.
'<span id="author">Al Sweigart</span>'
elems[0].getText()
'Al Sweigart'
elems[0].attrs
{'id': 'author'}

pElems = exampleSoup.select('p')
#Using str() on pElems[0], pElems[1], and pElems[2] shows you each element as a string, and using getText() on each element shows you its text.
str(pElems[0])
'<p>Download my <strong>Python</strong> book from <a href="https://inventwithpython.com">my website</a>.</p>'
pElems[0].getText()
'Download my Python book from my website.'
str(pElems[1])
'<p class="slogan">Learn Python the easy way!</p>'
pElems[1].getText()
'Learn Python the easy way!'
str(pElems[2])
'<p>By <span id="author">Al Sweigart</span></p>'
pElems[2].getText()
'By Al Sweigart'

## Getting Data from an Element’s Attributes

soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
str(spanElem)
'<span id="author">Al Sweigart</span>'
spanElem.get('id')
'author'
spanElem.get('some_nonexistent_addr') == None
True
spanElem.attrs
{'id': 'author'}

