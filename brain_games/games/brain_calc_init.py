from random import randint, choice


START_RANDINT_FROM = 0
END_RANDINT_WITH = 100


def generate_question():
    random_sign = choice(['+', '-', '*'])
    random_number1 = randint(START_RANDINT_FROM, END_RANDINT_WITH)
    random_number2 = randint(START_RANDINT_FROM, END_RANDINT_WITH)
    random_input = f'{random_number1} {random_sign} {random_number2}'
    if random_sign == '+':
        correct_answer = str(random_number1 + random_number2)
    elif random_sign == '-':
        correct_answer = str(random_number1 - random_number2)
    else:
        correct_answer = str(random_number1 * random_number2)
    return (random_input, correct_answer)
