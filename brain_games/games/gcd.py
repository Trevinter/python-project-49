from random import randint


GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_answer(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    sum = num1 + num2
    return sum


def get_game():
    num1 = randint(3, 100)
    num2 = randint(3, 100)
    game_question = f'{str(num1)} {str(num2)}'
    return str(game_question), get_answer(num1, num2)
