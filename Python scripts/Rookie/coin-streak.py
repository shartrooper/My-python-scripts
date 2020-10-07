import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    coinFlipsList=[]
    streak=0
    flip=0
    # Code that creates a list of 100 'heads' or 'tails' values.
    for randNum in range(100):
        flip=random.randint(0,1)
        if flip == 0:
            coinFlipsList.append("H")
        elif flip == 1:
            coinFlipsList.append("T")
    # Code that checks if there is a streak of 6 heads or tails in a row.
        flip=coinFlipsList[0]
    for i in range(1,len(coinFlipsList)):
        if(flip == coinFlipsList[i]):
            streak+=1
        else:
            flip=coinFlipsList[i]
            streak=0
        if(streak >= 6):
            numberOfStreaks+=1
            streak = 0
        
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
