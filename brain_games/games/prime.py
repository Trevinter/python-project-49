from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_even(game_question):
    for i in range(2, int(game_question ** 0.5) + 1):
        if game_question % i == 0:
            return False
    return True


def get_game():
    game_question = randint(2, 101)
    if is_even(game_question):
        answer = 'yes'
    else:
        answer = 'no'
    return game_question, answer
