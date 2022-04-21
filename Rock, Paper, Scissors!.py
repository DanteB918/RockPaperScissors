import random

ans = random.randint(1, 3)          #Picks a random interger, 1, 2 or 3, and assigns them to rock, paper and scissors.
if ans == 1:
    print('Rock!')
if ans == 2:
    print('Paper!')
if ans == 3:
    print('Scissors')
print('Welcome to Rock Paper Scissors!')

n = input('Which would you like to choose? \nRock, Paper or scissors?:')
if n == 'rock'.casefold():                      #Assigning responses to answers, if player chooses rock and the computer chooses paper, the player loses and vice versa.
    if ans == 1:
        print('Rock \nWe were tied!')
    if ans == 2:
        print('Paper \nyou were defeated!')
    if ans == 3:
        print('Scissors \nyou won!!')
if n == 'paper'.casefold():
    if ans == 1:
        print('Rock \nyou won!!')
    if ans == 2:
        print('Paper \nWe were tied!')
    if ans == 3:
        print('Scissors \nyou were defeated!')
if n == 'scissors'.casefold():
    if ans == 1:
        print('Rock \nyou were defeated!')
    if ans == 2:
        print('Paper \nyou won!!')
    if ans == 3:
        print('Scissors \nWe were tied!')
elif print('Thanks for playing!'):
    pass

else:
    quit()
