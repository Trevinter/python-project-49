from random import randint
from brain_games import cli
import prompt


def evclid(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    sum = num1 + num2
    return sum


def gcd_game():
    name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        num1 = randint(3, 100)
        num2 = randint(3, 100)
        sum = evclid(num1, num2)
        print(f'Question: {num1}, {num2} ')
        issue = prompt.string('Your answer:' + ' ')
        if int(issue) == sum:
            count += 1
            print('Correct!')
        else:
            count += 4
            print(f"'{issue}' is wrong answer ;(. Correct answer was '{sum}'.")
            return print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
