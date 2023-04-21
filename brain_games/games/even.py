from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(game_question):
    if int(game_question) % 2 == 0:
        return True
    else:
        return False


def get_game():
    game_question = str(randint(1, 20))
    if is_even(game_question):
        answer = 'yes'
    else:
        answer = 'no'
    return game_question, answer
