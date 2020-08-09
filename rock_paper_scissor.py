import random
import sys
print('ROCK, PAPER, SCRISSORS')
wins = 0
losses = 0
ties = 0
while True:
    print('--- %s Wins, %s Losses, %s ties ---' % (wins, losses, ties))
    while True: #This While loop activates if a user doesn't type 'r', 'p', 's', or 'q'.
        print(
            "Enter a move: -|- rocks = r, paper = p, scissors = s -|- You can quit byy 'q'")
        userMove = input()
        if userMove == 'q':
            sys.exit()
        elif userMove == 'r' or userMove == 's' or userMove == 'p':
            break
    randomNumber = random.randint(1, 3)
    myMove = ''
    losing = 'You lost'
    winning = 'You won!!!'
    tie = 'It s a tie. I will beat you later!'
    if randomNumber == 1:
        myMove = 'rock'
    elif randomNumber == 2:
        myMove = 'paper'
    else:
        myMove = 'scissors'
    if (userMove == 'r' and myMove == 'paper' or userMove == 'p' and myMove == 'rock' or userMove == 's' and myMove == 'paper'):
        print(winning)
        wins = wins + 1
    elif (userMove == 'r' and myMove == 'rock' or userMove == 'p' and myMove == 'paper' or userMove == 's' and myMove == 'scissors'):
        print(tie)
        ties = ties + 1
    elif (userMove == 'r' and myMove == 'scissors' or userMove == 'p' and myMove == 'scissors' or userMove == 's' and myMove == 'rock'):
        print(losing)
        losses = losses + 1
        
