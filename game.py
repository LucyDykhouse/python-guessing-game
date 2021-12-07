"""A number-guessing game."""

from random import randint

count = 0
maxTries = 15
bestScore = maxTries
worstScore = 0

print('\nHowdy, what\'s your name?')

name = input('(Type in your name): ')

while True:
    lower = input(f'Hi {name}! Type a lower bound for guessing: ')

    try:
        lower = int(lower)
        break
    except ValueError:
        print(f'{lower} is not a number!')
        continue

while True:
    upper = input(f'Hi {name}! Type an upper bound for guessing: ')

    try:
        upper = int(upper)
        randNum = randint(lower, upper)        
        break
    except ValueError:
        print(f'{upper} is not a number or is less than the lower limit, {lower}!')
        continue

print(f'Great! Try to guess my number between {lower} and {upper}.\n')



while True:
    
    # Get the user's guess
    guess = input('Your guess? ')

    # Ensure that the guess is a number
    try:
        guess = int(guess)
    except ValueError:
        print(f'{guess} is not a number')
        continue

    # Ensure that the guess is between 1 and 100
    if guess < 1 or guess > 100:
        print('Your guess must be between 0 and 100')
        continue

    # Increment the number of guesses
    count += 1

    # Check to see if maxTries has been reached
    if count >= maxTries:
        print('Sorry, you have exceeded your allotted tries.')
        replay = input('Would you like to play again? Enter yes or no: ')

        if replay.lower() == 'yes':
            print('Here we go again!\n')
            count = 0
            worstScore = maxTries
            randNum = randint(lower, upper)
            continue

        else:
            print(f'I\'ll take that as a no. Thanks for playing, {name}!')
            break

    # Compare user's guess to the random number
    if guess < randNum:
        print('Your guess is too low, try again.')
    
    elif guess > randNum:
        print('Your guess is too high, try again.')
    
    else:
        print(f'\nWell done, {name}! You found my number in {count} tries!')
        
        # Update user's best score or worst score
        if count > worstScore:
            worstScore = count

        if count < bestScore:
            bestScore = count

        # Relay best and worst scores    
        print(f'Your best score is currently {bestScore}. Your worst score is currently {worstScore}')
        
        # Ask about another round
        replay = input('Would you like to play again? Enter yes or no: ')

        if replay.lower() == 'yes':
            print('Here we go again!\n')
            count = 0
            randNum = randint(lower, upper)
            continue

        else:
            print(f'I\'ll take that as a no. Thanks for playing, {name}!')
            break

