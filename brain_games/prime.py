from random import randint
from brain_games import cli
import prompt


def prime_number(number):
    no = 'no'
    yes = 'yes'
    if number <= 1:
        return 'no'
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return no
    return yes


def prime_game():
    name = cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        number = randint(2, 101)
        num = prime_number(number)
        issue = prompt.string(f'Question: {number}')
        print(f'Your answer: {issue}')
        if num == 'yes' and issue == 'yes':
            count += 1
            print('Correct!')
        elif num == 'no' and issue == 'no':
            count += 1
            print('Correct!')
        else:
            print(f"'{issue}' is wrong answer ;(. Correct answer was '{num}'.")
            return print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
