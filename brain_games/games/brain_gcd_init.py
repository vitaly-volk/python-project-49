from random import randint
from math import gcd


def generate_question():
    random_number1 = randint(0, 100)
    random_number2 = randint(0, 100)
    random_input = f'{random_number1} {random_number2}'
    correct_answer = str(gcd(random_number1, random_number2))
    return (random_input, correct_answer)