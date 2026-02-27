import random
number = random.randint(0,5)
guess = None
while guess != number:
    guess= int(input('Try to guess the number between 0 and 5 :'))
    if guess == number:
        print('Congratulations!! You Guessed it!!!')
    else:
        print('Wrong Guess. Try Again!!! ')