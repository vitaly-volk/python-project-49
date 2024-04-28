from random import randint
from math import gcd


START_RANDINT_FROM = 0
END_RANDINT_WITH = 100


def generate_question():
    random_number1 = randint(START_RANDINT_FROM, END_RANDINT_WITH)
    random_number2 = randint(START_RANDINT_FROM, END_RANDINT_WITH)
    random_input = f'{random_number1} {random_number2}'
    correct_answer = str(gcd(random_number1, random_number2))
    return (random_input, correct_answer)
