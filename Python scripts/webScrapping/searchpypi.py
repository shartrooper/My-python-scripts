#! python 3
""" searchpypi.py  - Opens several search results.
    Gets search keywords from the command line arguments
    Retrieves the search results page
    Opens a browser tab for each result
"""
import requests, sys, webbrowser, bs4

print("Searching...")  # display text while downloading the search result page
res = requests.get(
    "https://google.com/search?q="
    "https://pypi.org/search/?q=" + " ".join(sys.argv[1:])
)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")
# Open a browser tab for each result.
linkElems = soup.select(".package-snippet")
# E.G. <a class="package-snippet" href="HYPERLINK "view-source:https://pypi.org/project/xml-parser/"/project/xml-parser/">.
numOpen = min(5, len(linkElems)) #The built-in Python function min() returns the smallest of the integer or float arguments it is passed.
for i in range(numOpen):
    urlToOpen = "https://pypi.org" + linkElems[i].get("href")
    print("Opening", urlToOpen)
    webbrowser.open(urlToOpen)

# beatiful soup other features https://www.crummy.com/software/BeautifulSoup/bs4/doc/.
