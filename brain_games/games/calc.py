from random import choice
from random import randint


rules = 'What is the result of the expression?'


def right_answer():
    rand_operator = choice(['+', '-', '*'])
    num1 = str(randint(1, 20))
    num2 = str(randint(1, 20))
    number = f'{str(num1)} {rand_operator} {str(num2)}'
    if rand_operator == '+':
        sum = int(num1) + int(num2)
        return str(number), sum
    elif rand_operator == '-':
        sum = int(num1) - int(num2)
        return str(number), sum
    elif rand_operator == '*':
        sum = int(num1) * int(num2)
        return str(number), sum
