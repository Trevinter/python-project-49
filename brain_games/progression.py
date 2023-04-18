from random import randint
from brain_games import cli
import prompt


num_list = list(range(1, 101))


def progression_game():
    name = cli.welcome_user()
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        step = randint(2, 10)
        new_num_list = num_list[::step]
        print(f'Question: {new_num_list[:10]} ')
        issue = prompt.string('Your answer:' + " ")
        if int(issue) == step:
            count += 1
            print('Correct!')
        else:
            print(f"'{issue}' is wrong answer ;(. Correct answer was '{step}'.")
            return print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
