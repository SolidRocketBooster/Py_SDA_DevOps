import random

userChoice = input('Rock, paper or scissors?: ')
comChoice = random.choice(['paper', 'rock', 'scissors'])

if userChoice == comChoice:
    print('Tie!')
elif userChoice == 'rock' and comChoice == 'paper':
    print('You lost!')
elif userChoice == 'rock' and comChoice == 'scissors':
    print('You win!')
elif userChoice == 'paper' and comChoice == 'rock':
    print('You lost!')
elif userChoice == 'paper' and comChoice == 'scissors':
    print('You won!')
elif userChoice == 'scissors' and comChoice == 'rock':
    print('You lost!')
elif userChoice == 'scissors' and comChoice == 'paper':
    print('You won!')
else:
    print('Enter rock, paper or scissors.')
