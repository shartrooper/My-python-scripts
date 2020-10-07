##Selenium Implementation. src=https://selenium-python.readthedocs.org/.
#to import selenium, you need to run from selenium import webdriver. pip install --user selenium
from selenium import webdriver
browser = webdriver.Firefox() # Firefox web browser starts up.
type(browser)
<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
browser.get('https://inventwithpython.com')

#Finding Elements on the Page
'''
Method name
	

WebElement object/list returned

browser.find_element_by_class_name(name)

browser.find_elements_by_class_name(name)
	

Elements that use the CSS
class name

browser.find_element_by_css_selector(selector)
browser.find_elements_by_css_selector(selector)
	

Elements that match the CSS
selector

browser.find_element_by_id(id)

browser.find_elements_by_id(id)
	

Elements with a matching id
attribute value

browser.find_element_by_link_text(text)

browser.find_elements_by_link_text(text)
	

<a> elements that completely
match the text provided

browser.find_element_by_partial_link_text(text)

browser.find_elements_by_partial_link_text(text)
	

<a> elements that contain the
text provided

browser.find_element_by_name(name)

browser.find_elements_by_name(name)
	

Elements with a matching name
attribute value

browser.find_element_by_tag_name(name)
browser.find_elements_by_tag_name(name)
	

Elements with a matching tag name
(case-insensitive; an <a> element is
matched by 'a' and 'A')
'''

#If no elements exist on the page that match what the method is looking for, the selenium module raises a NoSuchElement exception.
#If you do not want this exception to crash your program, add try and except statements to your code.

try:
    elem = browser.find_element_by_class_name(' cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

'''
Attribute or method
	

Description

tag_name
	

The tag name, such as 'a' for an <a> element

get_attribute(name)
	

The value for the element’s name attribute

text
	

The text within the element, such as 'hello' in <span>hello </span>

clear()
	

For text field or text area elements, clears the text typed into it

is_displayed()
	

Returns True if the element is visible; otherwise returns False

is_enabled()
	

For input elements, returns True if the element is enabled; otherwise returns False

is_selected()
	

For checkbox or radio button elements, returns True if the element is selected; otherwise returns False

location
	

A dictionary with keys 'x' and 'y' for the position of the element in the page
'''

linkElem = browser.find_element_by_link_text('Read Online for Free')
type(linkElem)
<class 'selenium.webdriver.remote.webelement.FirefoxWebElement'>
linkElem.click() # follows the "Read Online for Free" link

import pyinputplus

browser.get('https://login.metafilter.com')
userElem = browser.find_element_by_id('user_name')
userElem.send_keys('your_real_username_here')
passwordElem = browser.find_element_by_id('user_pass')
your_real_password_here=pyinputplus.inputPassword()
passwordElem.send_keys(your_real_password_here)
passwordElem.submit()

'''
As long as login page for MetaFilter hasn’t changed the id of the Username and Password text fields since this book was published,
the previous code will fill in those text fields with the provided text.
'''



## Sending Special keys

'''
Attributes
	

Meanings

Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT
	

The keyboard arrow keys

Keys.ENTER, Keys.RETURN
	

The ENTER and RETURN keys

Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP
	

The HOME, END, PAGEDOWN, and PAGEUP keys

Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE
	

The ESC, BACKSPACE, and DELETE keys

Keys.F1, Keys.F2, . . . , Keys.F12
	

The F1 to F12 keys at the top of the keyboard

Keys.TAB
	

The TAB key
'''

from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)     # scrolls to bottom
htmlElem.send_keys(Keys.HOME)    # scrolls to top
# Calling browser.find_element_by_tag_name('html') is a good place to send keys to the general web page


#Clicking Browser Buttons

'''
The selenium module can simulate clicks on various browser buttons as well through the following methods:

browser.back() Clicks the Back button.

browser.forward() Clicks the Forward button.

browser.refresh() Clicks the Refresh/Reload button.

browser.quit() Clicks the Close Window button.
'''

