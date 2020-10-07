#! python3
# Mad-libs.py reads madlib.txt file and lets the user add their own text anywhere
# the words ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.!

from pathlib import Path
import re, random, pyinputplus as pyip

#Load and read text file. (get string)
madLibFile= open(Path.cwd()/'madlib.txt')
madLibContent= madLibFile.read()

#Split the whole string into a list of sentences.
if len(madLibContent):
    sentencesList=madLibContent.split('\n')
#Verify valid sentence, then choose a random  string and display to user.
    picked=random.randint(0,len(sentencesList)-1)
    sentence=sentencesList[picked]
    while not sentencesList[picked]:
        picked=random.randint(0,len(sentencesList)-1)
        sentence=sentencesList[picked]
    print('*'*60+'MAD LIBS!'+'*'*60)
    print(sentence)
    print('*'*60+'MAD LIBS!'+'*'*60)
#Loop the sentence and Prompt the user to introduce words for ADJECTIVE, NOUN, ADVERB or VERB respectively.
    madLibsRegex=re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
    while madLibsRegex.search(sentence):
        found=madLibsRegex.search(sentence).group()
        response = pyip.inputStr('Enter the following word type : '+found.lower()+'\n',blockRegexes=[r'[0-9]+'])
        sentence=madLibsRegex.sub(response,sentence,count=1)
#TODO: Display modified string.
    print('New Text:')
    print(sentence)
