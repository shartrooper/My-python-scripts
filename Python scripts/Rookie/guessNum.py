#this is a quest the number game,between 1 to 10
import random,sys,time


def guessNum(num,rand):
    if num < rand:
        print('Try again with a higher number')
        return None
    elif num > rand:
        print ('Try again with a lower number')
        return None
    else:
        print ('Congratulations, you guessed the number!, It\'s '+ str(rand))
        return rand

def promptUserGuessNumber():
    rand=int(random.randrange(0,10))
    evalguess= 0
    wordForSentence= 'an'
    while evalguess!= rand:
        print('Introduce '+wordForSentence+' integer number between 0 to 10')
        guess=input()
        try:
            if int(guess)<=10 and int(guess)>=0:
                evalguess= guessNum(int(guess),rand)
                wordForSentence='another'
            else:
                print('Input a number between 0 and 10!')
        except ValueError:
            print('Invalid value')
            wordForSentence='another'
    time.sleep(2)
    sys.exit()
            
promptUserGuessNumber()
