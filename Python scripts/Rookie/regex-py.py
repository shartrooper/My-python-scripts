import re

##re.compile() returns a Regex pattern object

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')

##Writing mo.group() inside our print() function
##call displays the whole match, 415-555-4242.

print('Phone number found: ' + mo.group())


## Grouping with parenthesis

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
'415'
mo.group(2)
'555-4242'
mo.group(0)
'415-555-4242'
mo.group()
'415-555-4242'

##If you would like to retrieve all the groups at once,
##use the groups() method—note the plural form for the name.

mo.groups()
('415', '555-4242')
areaCode, mainNumber = mo.groups()
print(areaCode)
#415
print(mainNumber)
#555-4242

# Matching multiple groups with the pipe

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()
'Batman'

mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()
'Tina Fey'

#pipe character and grouping parentheses
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
'Batmobile'
mo.group(1)
'mobile'


#Greedy and Lazy

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()
'HaHaHaHaHa'

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()
'HaHaHa'

#findall() method will return a list of strings of every match in the searched string.

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']

#If there are groups in the regular expression, then findall() will return a list of tuples.
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]


# DotALL to match anything including newline

noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
"Serve the public trust."

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.\nProtect the innocent.\nUphold the law.'

#Case insensitive matching

robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
'RoboCop'

robocop.search('ROBOCOP protects the innocent.').group()
'ROBOCOP'

robocop.search('Al, why does your programming book talk about robocop so much?').group()
'robocop'

# sub() method for substitution!

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
"A**** told C**** that E**** knew B**** was a double agent."

#Managing complex regexes


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

'''Note how the previous example uses the triple-quote syntax to create a multiline
string so that you can spread the regular expression definition over many lines, making it much more legible.'''

# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)




