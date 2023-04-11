#!/usr/bin/env python3
from random import randint
from brain_games import cli
import prompt


def even_game():
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = str(randint(1, 20))
        question = prompt.string('Question: ' + number)
        print(number)
        if int(number) % 2 == 0 and question == "yes":
            counter += 1
            print('Correct!')
        elif int(number) % 2 == 0 and question != "yes":
            counter += 4
            print("yes' is wrong answer ;(. Correct answer was 'no'.")
            return ("Let's try again, {name}!")
        elif int(number) % 2 != 0 and question == "no":
            counter += 1
            print('Correct!')
        elif int(number) % 2 != 0 and question != "no":
            counter += 4
            print("yes' is wrong answer ;(. Correct answer was 'no'.")
            return (f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
