from random import randint


rules = 'What number is missing in the progression?'
num_list = list(range(1, 101))
len_list = len


def right_answer():
    step = randint(2, 10)
    number = num_list[::step]
    number = number[:10]
    hidden_num = randint(0, len(number) - 1)
    answer = str(number[hidden_num])
    number[hidden_num] = '..'
    return str(number), answer
