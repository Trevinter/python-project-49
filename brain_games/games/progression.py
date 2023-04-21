from random import randint


GAME_RULE = 'What number is missing in the progression?'


def get_sequence(num_list):
    step = randint(2, 10)
    number = num_list[::step]
    number = number[:10]
    return number


def get_game():
    num_list = list(range(1, 101))
    list_game = get_sequence(num_list)
    hidden_num = randint(0, len(list_game) - 1)
    answer = str(list_game[hidden_num])
    list_game[hidden_num] = '..'
    game_question = ' '.join(str(x) for x in list_game)
    return str(game_question), answer
