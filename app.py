import random

user_score = 0
computer_score = 0
available_picks = ['rock', 'paper', 'scissors']

def print_win():
    print('You win!')

def print_lose():
    print('You lose.')

def print_result():
    print('You [ ' + str(user_score) + ' : ' + str(computer_score) +' ] Computer\n')

while True:
    user_pick = input('\nRock, paper or scissors? ')
    computer_pick = random.choice(available_picks)

    if user_pick not in available_picks:
        print('Pick again!')
        continue

    print('You picked: ' + user_pick)
    print('Computer picked: ' + computer_pick)

    if user_pick == computer_pick:
        print('It\'s a tie!')
        print_result()
    elif user_pick == available_picks[0]:
        if computer_pick == available_picks[2]:
            user_score += 1
            print_win()
            print_result()
        else:
            computer_score += 1
            print_lose()
            print_result()
    elif user_pick == available_picks[1]:
        if computer_pick == available_picks[0]:
            user_score += 1
            print_win()
            print_result()
        else:
            computer_score += 1
            print_lose()
            print_result()
    elif user_pick == available_picks[2]:
        if computer_pick == available_picks[1]:
            user_score += 1
            print_win()
            print_result()
        else:
            computer_score += 1
            print_lose()
            print_result()

    play_again = input('Play again? (y/n): ')

    if play_again.lower() != 'y':
        break
