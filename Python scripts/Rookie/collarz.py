def collatz(num):
    if num % 2 == 0:
        print(str(num)+'// 2')
        return num/2
    else:
        odds=3*num+1
        print(str(odds))
        return odds

def typeNumAndRunCollarz():
    print('Input your number')
    val=input()
    try:
        if int(val) >= 0:
            val=int(val)
            while val != 1:
                val=collatz(val)
            print(str(val))
    except ValueError:
        print('Error: you didn\'t entered a valid value.''Error:')

typeNumAndRunCollarz()

