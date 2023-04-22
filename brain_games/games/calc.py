from random import choice
from random import randint


GAME_RULE = 'What is the result of the expression?'


def get_answer(rand_operator, num1, num2):
    if rand_operator == '+':
        sum = int(num1) + int(num2)
    elif rand_operator == '-':
        sum = int(num1) - int(num2)
    else:
        sum = int(num1) * int(num2)
    return sum


def get_game():
    rand_operator = choice(['+', '-', '*'])
    num1 = str(randint(1, 20))
    num2 = str(randint(1, 20))
    game_question = f'{str(num1)} {rand_operator} {str(num2)}'
    return str(game_question), get_answer(rand_operator, num1, num2)
