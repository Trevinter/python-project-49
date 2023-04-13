#!/usr/bin/env python3
from random import randint
from random import choice
from brain_games import cli
import prompt


def calc_game():
    name = cli.welcome_user()
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        rand_operator = choice(['+', '-', '*'])
        num1 = str(randint(1, 20))
        num2 = str(randint(1, 20))
        issue = prompt.string('Question: ' + num1 + rand_operator + num2)
        if rand_operator == '+':
            sum = int(num1) + int(num2)
        elif rand_operator == '-':
            sum = int(num1) - int(num2)
        elif rand_operator == '*':
            sum = int(num1) * int(num2)
        if str(sum) == issue:
            count += 1
            print('Correct!')
        else:
            print(f"'{issue}' is wrong answer ;(. Correct answer was '{sum}'.")
            return print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
