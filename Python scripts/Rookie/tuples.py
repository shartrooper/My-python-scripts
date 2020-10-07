#tuples are immutable like strings

eggs = ('hello', 42, 0.5)
eggs[0]
'hello'
eggs[1:3]
(42, 0.5)
print(len(eggs))

type(('hello',)) #class 'tuple'

type(('hello')) #class 'str'

#Converting Types with the list() and tuple() Functions

tuple(['cat', 'dog', 5]) #('cat', 'dog', 5)
list(('cat', 'dog', 5)) #['cat', 'dog', 5]
list('hello') #['h', 'e', 'l', 'l', 'o']
