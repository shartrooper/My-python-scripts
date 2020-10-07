# Take a list value as an argument and returns a string with all the items
# separated by a comma and a space, with "and" inserted before the last item.

def makeStringFromList(list):
    stringBuild=''
    
    for i in range(len(list)):
        if i != 0 and i < len(list)-1:
            stringBuild+=','+list[i]
            continue
        elif i == len(list)-1:
            stringBuild+=' and '+list[i]+'.'
            continue
        stringBuild+=list[i]
    return print(stringBuild)

makeStringFromList(['apples', 'bananas', 'tofu', 'cats'])
