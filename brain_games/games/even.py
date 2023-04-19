from random import randint


rules = 'Answer "yes" if the number is even, otherwise answer "no".'
yes = 'yes'
no = 'no'


def right_answer():
    number = str(randint(1, 20))
    if int(number) % 2 == 0:
        return number, yes
    elif int(number) % 2 != 0:
        return number, no
