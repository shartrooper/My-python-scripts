##Dictionary basics. Similar to objects in data structure

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

def birthdayInfo (birthdays):
   while True:
       print('Enter a name: (blank to quit)')
       name = input()
       if name == '':
           break

       if name in birthdays:
          print(birthdays[name] + ' is the birthday of ' + name)
       else:
           print('I do not have birthday information for ' + name)
           print('What is their birthday?')
           bday = input()
           birthdays[name] = bday
           print('Birthday database updated.')

#birthdayInfo(birthdays)

spam = {'color': 'red', 'age': 42}

##values()

def useValuesMethod(spam):

    for v in spam.values():
        print(v)
#red
#42

#useValuesMethod(spam)


##keys()

def useKeysMethod(spam):
 for k in spam.keys():
     print(k)

#color
#age

#useKeysMethod(spam)

##items() are tuples of keys and value

def useItemsMethod(spam):
 for k in spam.items():
     print(k)

#('color', 'red')
#('age', 42)

#useItemsMethod(spam)

## Multiple Assignment Trick

def multAssing(spam):
    spam = {'color': 'red', 'age': 42}
    for k, v in spam.items():
        print('Key: ' + k + ' Value: ' + str(v))

#Key: age Value: 42
#Key: color Value: red

#multAssign(spam)

## Checking Whether a Key or Value Exists in a Dictionary

def checkExistence (arr={'name': 'Zophie', 'age': 7}):
    print('name' in arr.keys())
    True
    print('Zophie' in arr.values())
    True
    print('color' in arr.keys())
    False
    print('color' not in arr.keys())
    True
    print('color' in arr)
    False

#checkExistence()

##  The get() Method
## takes two arguments:
## -the key of the value to retrieve
## -a fallback value to return if that key does not exist.
    
def tryGetMethod (picnicItems = {'apples': 5, 'cups': 2}):
    print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
    #'I am bringing 2 cups.'
    print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
    #'I am bringing 0 eggs.'

#tryGetMethod()

#The setdefault() Method. Allows to set a default value for keys without it.

def setDefaultOnDiccionary (items={'name': 'Pooka', 'age': 5}):
    items.setdefault('color', 'black')
    #'black'
    print(items)
    #{'color': 'black', 'age': 5, 'name': 'Pooka'}
    items.setdefault('color', 'white')
    # he value for that key is not changed to 'white',
    #because items already has a key named 'color'.
    print(items)
    #{'color': 'black', 'age': 5, 'name': 'Pooka'}

setDefaultOnDiccionary()











