import random
ans = random.randint(1, 3)
if ans == 1:
    print('Rock!')
if ans == 2:
    print('Paper!')
if ans == 3:
    print('Scissors')
print('Welcome to Rock Paper Scissors!')
input('Which would you like to choose? \nRock, Paper or scissors?:')
if input() == 'rock':
    if ans == 1:
        print('Rock \nWe were tied!')
    if ans == 2:
        print('Paper \nyou were defeated!')
    if ans == 3:
        print('Scissors \nyou won!!')
if input() == 'paper':
    if ans == 1:
        print('Rock \nyou won!!')
    if ans == 2:
        print('Paper \nWe were tied!')
    if ans == 3:
        print('Scissors \nyou were defeated!')
if input() == 'scissors':
    if ans == 1:
        print('Rock \nyou were defeated!')
    if ans == 2:
        print('Paper \nyou won!!')
    if ans == 3:
        print('Scissors \nWe were tied!')
else:
    print('Thats not an option..')
    quit()
    
