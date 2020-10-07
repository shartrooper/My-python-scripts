import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

def getAnswerArray(answerNumber):
    responseArray=['It is certain','It is decidedly so',
                   'Yes','Reply hazy try again','Ask again later',
                   'Concentrate and ask again','My reply is no', 'Outlook not so good','Very doubtful']
    for i in range(9):
        if answerNumber == i:
            print(responseArray[i])
            break
    return None  # Behind the scenes, Python adds return None to the end of any function definition with no return statement.
                 #This is similar to how a while or for loop implicitly ends with a continue statement. Also, if you use a return
                 #statement without a value (that is, just the return keyword by itself), then None is returned.
getAnswerArray(r)
