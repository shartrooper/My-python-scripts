
#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
# Example py mapit.py 870 Valencia St, San Francisco, CA 94110
import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
# TODO: Get address from clipboard.
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
