import random
from time import sleep
number = random.randint(0,5)
guess = None
print(20 * '\033[31m=\033[0m')
while guess != number:
    try:
     guess= int(input('Try to guess the number between 0 and 5 :'))
    except ValueError:
        print('Type a valid number')
        continue
    print ("\033[35mLoading...\033[0m")
    sleep(2)
    if guess == number:
        print('Congratulations!! You Guessed it!!!')
        print(20 * '\033[31m=\033[0m')
    else:
        print('Wrong Guess. Try Again!!! ')
        print(20 * '\033[31m=\033[0m')
