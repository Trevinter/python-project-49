from random import randint


rules = 'Find the greatest common divisor of given numbers.'


def right_answer():
    num1 = randint(3, 100)
    num2 = randint(3, 100)
    number = f'{str(num1)} {str(num2)}'
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    sum = num1 + num2
    return str(number), sum
