from random import randint, choice


NUMBER_FROM_WHICH_RANDINT_STARTS = 0
NUMBER_WITH_WHICH_RANDINT_ENDS = 100


def generate_question():
    random_sign = choice(['+', '-', '*'])
    random_number1 = randint(NUMBER_FROM_WHICH_RANDINT_STARTS, NUMBER_WITH_WHICH_RANDINT_ENDS)
    random_number2 = randint(NUMBER_FROM_WHICH_RANDINT_STARTS, NUMBER_WITH_WHICH_RANDINT_ENDS)
    random_input = f'{random_number1} {random_sign} {random_number2}'
    if random_sign == '+':
        correct_answer = str(random_number1 + random_number2)
    elif random_sign == '-':
        correct_answer = str(random_number1 - random_number2)
    else:
        correct_answer = str(random_number1 * random_number2)
    return (random_input, correct_answer)