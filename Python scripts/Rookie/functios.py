#import random call random and has to type in it before their methods(random.rand) 
from random import * #call all random function and doesn't have to type random
import sys # method exit forces a closing
import pyperclip # pyperclip.copy() and pyperclip.paste() copy and paste to the clipboard
rand= randint(1,10)
print(rand)
pyperclip.copy(rand)
pyperclip.paste()# paste rand number string
sys.exit()
print('Not reached')
