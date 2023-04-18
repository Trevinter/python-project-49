from random import randint
from brain_games import cli
import prompt


def even_game():
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = str(randint(1, 20))
        print('Question: ' + number)
        question = prompt.string('Your answer:' + " ")
        if (int(number) % 2 == 0 and question == "yes") or \
                (int(number) % 2 != 0 and question == "no"):
            counter += 1
            print('Correct!')
        elif int(number) % 2 == 0 and question != "yes":
            counter += 4
            print(f"'{question}' is wrong answer ;(. Correct answer was 'yes'.")
            return print(f"Let's try again, {name}!")
        else:
            counter += 4
            print(f"'{question}' is wrong answer ;(. Correct answer was 'no'.")
            return print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
