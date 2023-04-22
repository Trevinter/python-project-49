from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_even(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_game():
    number = randint(2, 101)
    if is_even(number):
        answer = 'yes'
    else:
        answer = 'no'
    return number, answer
