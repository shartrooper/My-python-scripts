import random

guess = ""
flip = {1:"heads",0:"tails"}
while guess not in ("heads", "tails"):
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if flip[toss] == guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    guess = input()
    toss = random.randint(0, 1)
    if flip[toss] == guess:
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")
