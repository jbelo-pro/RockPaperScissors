# Write your code here
import random


def check_winner(opts: list, user_opt: str, computer_opt):

    pos = opts.index(user_opt)
    new_list = None
    if pos == len(opts) - 1:
        new_list = opts[:pos]
    elif pos == 0:
        new_list = opts[1:]
    else:
        new_list = opts[pos + 1:]
        new_list.extend(opts[:pos])

    half = int(len(new_list)/2)
    user_defeated_by = new_list[:half]
    user_beating = new_list[half:]

    if computer_opt == user_opt:
        return 'draw'
    elif computer_opt in user_defeated_by:
        return 'computer'
    elif computer_opt in user_beating:
        return 'user'


user_name = input('Enter your name: ')
print('Hello, {}'.format(user_name))

score = 0

with open('rating.txt') as f:
    lines = f.readlines()
    for line in lines:
        if user_name in line:
            line = line.replace('\n', '')
            score = score + int(line.split()[1])
            break

options = input()
if options:
    options = options.split(',')
else:
    options = ['rock', 'paper', 'scissors']

print("Okay, let's start")

while True:

    user_sel = input()

    if user_sel == '!exit':
        print('Bye!')
        break
    elif user_sel == '!rating':
        print('Your rating: {}'.format(score))
    elif user_sel not in options:
        print('Invalid input')
    else:
        computer_sel = options[random.randint(0, len(options) - 1)]
        winner = check_winner(options, user_sel, computer_sel)

        if winner == 'user':
            print(
                'Well done. Computer chose {} and failed'.format(computer_sel))
            score += 100
        elif winner == 'computer':
            print('Sorry, but computer chose {}'.format(computer_sel))
        else:
            print('There is a draw {}'.format(computer_sel))
            score += 50
