"""A number-guessing game."""

from random import randint

randNum = randint(1, 100)
count = 0

print('\nHowdy, what\'s your name?')

name = input('(Type in your name): ')

print(f'{name}, I\'m thinking of a number between 1 and 100.')
print('Try to guess my number.\n')


while True:
    guess = input('Your guess? ')

    try:
        guess = int(guess)
    except ValueError:
        print(f'{guess} is not a number')
        continue

    if guess < 1 or guess > 100:
        print('Your guess must be between 0 and 100')
        continue

    count += 1

    if guess < randNum:
        print('Your guess is too low, try again.')
    
    elif guess > randNum:
        print('Your guess is too high, try again.')
    
    else:
        print(f'Well done, {name}! You found my number in {count} tries!')
        break

