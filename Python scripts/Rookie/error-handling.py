def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def catCounter():
    print('How many cats do u have?')
    cats=input()
    try:
        if int(cats) > 4:
            print('quite a lot of cats')
        else:
            print('not too many')
    except ValueError:
        print('Error: you didn\'t entered a valid value.')

catCounter()
