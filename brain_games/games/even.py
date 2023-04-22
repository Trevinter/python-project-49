from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if int(number) % 2 == 0:
        return True
    else:
        return False


def get_game():
    number = str(randint(1, 20))
    if is_even(number):
        answer = 'yes'
    else:
        answer = 'no'
    return number, answer
