from random import randint


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
no = 'no'
yes = 'yes'


def right_answer():
    number = randint(2, 101)
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return str(number), no
    return str(number), yes
