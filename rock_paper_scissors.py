#rock, paper. scissors game with computer
import random

print('Welcome to this fun game! Good luck!')
ask_play = input('Do you want to play? ')

if ask_play.lower() != 'yes':
    quit()

ask_player = input('Do you think you have what it takes to win? Answer with yes, no, or maybe. ')

if ask_player == 'yes':
    print('You might just win!')
    print("Let's continue!")
if ask_player == 'no':
    print('Believe in yourself')
    print("Okay? let's continue!")
if ask_player == 'maybe':
    print('You will be fine...')
    print("There is no harm in trying, let's continue!")

player_win = 0
computer_win = 0

choices = ['rock', 'paper', 'scissors']

while True:
    player_input = input('Choose rock, paper, scissors, or q to quit: ').lower()
    if player_input == 'q':
        break
    if player_input not in choices:
        continue

    random_num = random.randint(0, 2)

    computer_input = choices[random_num]
    print('Computer picked', computer_input, '.')
    if player_input == 'rock' and computer_input == 'scissors':
        print('You win!')
        player_win += 1

    elif player_input == 'paper' and computer_input == 'rock':
        print('You win!')
        player_win += 1

    elif player_input == 'scissors' and computer_input == 'paper':
        print('You win!')
        player_win += 1

    else:
        print('You lost!')
        computer_win += 1

print('You won', player_win, 'times!')
print('Computer won', computer_win, 'times!')
print('Thanks for playing')



