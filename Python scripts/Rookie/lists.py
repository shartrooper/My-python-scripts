#MOST OF THEM ALSO CAN BE APPLIED TO STRINGS

#Slicing list in order to create a new list

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])#['cat', 'bat', 'rat', 'elephant']
print(spam[1:3])#['bat', 'rat']
print(spam[0:-1])#['cat', 'bat', 'rat']


# List Concatenation and List Replication

print([1, 2, 3] + ['A', 'B', 'C']) #[1, 2, 3, 'A', 'B', 'C']
print(['X', 'Y', 'Z'] * 3) #['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam) #[1, 2, 3, 'A', 'B', 'C']

# Removing Values from Lists with del Statements

spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam) #['cat', 'bat', 'elephant']
del spam[2]
print(spam) #['cat', 'bat'] 

# The in and not in Operators

'howdy' in ['hello', 'hi', 'howdy', 'heyas'] #True
spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam #False
'howdy' not in spam #False
'cat' not in spam #True

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

#The Multiple Assignment Trick(detructuring assingment)

cat = ['fat', 'gray', 'loud']
size, color, disposition = cat

print(size+' '+color+' '+disposition)

#Using the enumerate() Function with Lists
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

#Using the random.choice() and random.shuffle() functions with Lists

import random
pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))

people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)

#index() Method

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello') #0

# Adding Values to Lists with the append() and insert() Methods

spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam) #['cat', 'dog', 'bat', 'moose']

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam) #['cat', 'chicken', 'dog', 'bat']

# Removing Values from Lists with the remove() Method

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam) #['cat', 'rat', 'elephant']


#Sorting the Values in a List with the sort() Method

spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam) #[-7, 1, 2, 3.14, 5]
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam) #['ants', 'badgers', 'cats', 'dogs', 'elephants'


#Reverse sorting (unable to sort lists with mixed values like strings and numbers)

spam.sort(reverse=True)
print(spam) #['elephants', 'dogs', 'cats', 'badgers', 'ants']

#quickie reverse

spam = ['cat', 'dog', 'moose']
spam.reverse()
print(spam) #['moose', 'dog', 'cat']

#Strings are immutable, only way to make a new string is with a copy

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName) #'Zophie the cat'

#  Actually modify the original list in eggs

eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs) #[4, 5, 6]

# function parameters are a reference copy. Passing a list to a function
# argument will still be mutable and modify the actual value

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam) #[1, 2, 3, 'Hello']

#To actually copy a list. Use copy module.

import copy

spam = ['A', 'B', 'C', 'D']
id(spam) #44684232
cheese = copy.copy(spam)
id(cheese) # cheese is a different list with different identity.
#44685832
cheese[1] = 42
print(spam) #['A', 'B', 'C', 'D']
print(cheese) #['A', 42, 'C', 'D']

#copy.deepcopy() allows to copy list with inner lists

