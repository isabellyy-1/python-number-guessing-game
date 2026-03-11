from time import sleep
import random
red = '\033[31m'
reset = '\033[0m'
blue = '\033[34m'
purple = '\033[35m'
print('=~'*20)
print(f'{purple}Number Guessing Game2.0{reset}')
print('=~'*20)
guess = 0
attempts = 0
computer_number = random.randint(1,10)
while guess != computer_number:
    try:
        guess = int(input(f'{blue}Try to Guess Number Between 1,10:{reset}'))
    except ValueError:
        print(f'{red}Type a Valid Number{reset}')
        continue
    except EOFError:
        print(f'{red}Input interrupted{reset}')
        break
    except KeyboardInterrupt:
        print(f'{red}Input interrupted{reset}')
        break
    if guess < 1 or guess > 10:
        print('Number must be between 1 and 10')
        continue
    print(f'{red}Loading...{reset}')
    attempts += 1
    sleep(2)
    print('\n')
    if guess == computer_number:
        print(f'You guessed correctly in {attempts} attempts! ')
        print('=~' * 20)
    else:
        print(f'Wrong Guess. Try Again!!! {attempts} attempts')
        print('=~' * 20)