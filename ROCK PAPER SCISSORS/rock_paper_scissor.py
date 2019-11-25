# coding=utf-8
# this is a game of rock, paper, scissor

import random

# taking inputs from the user

while True:
    ans = 0
    while ans > 3 or ans < 1:
        try:
            print('Enter your choice:')
            print('\t1. Rock\n\t2. Paper\n\t3. Scissor')
            ans = int(input('>>> '))
        except ValueError:
            print('Enter valid input.')

    # assigning values to the inputs from the user

    user_choice = None
    if ans == 1:
        user_choice = 'rock'
    elif ans == 2:
        user_choice = 'paper'
    elif ans == 3:
        user_choice = 'scissor'

    # taking inputs from the computer

    comp_ans = random.randint(1, 3)
    while comp_ans == ans:
        comp_ans = random.randint(1, 3)

    # assigning values to inputs from computer

    comp_choice = None
    if comp_ans == 1:
        comp_choice = 'rock'
    elif comp_ans == 2:
        comp_choice = 'paper'
    elif comp_ans == 3:
        comp_choice = 'scissor'

    # displaying the hand each user and the computer has dealt

    print(f'{user_choice.title()} vs. {comp_choice.title()}')

    result = str()
    if ans == 1 and comp_ans == 2 or ans == 2 and comp_ans == 1:
        result = 'paper'
    elif ans == 1 and comp_ans == 3 or ans == 3 and comp_ans == 1:
        result = 'rock'
    elif ans == 3 and comp_ans == 2 or ans == 2 and comp_ans == 3:
        result = 'scissor'

    if result == user_choice:
        print('You Win !')
    elif result == comp_choice:
        print('You lose !')

    # asking whether user want to play more
    print('Do you want to play again ? [Yes/no]: ')
    ans = input().lower()
    if ans == 'no'or ans == 'n':
        break
