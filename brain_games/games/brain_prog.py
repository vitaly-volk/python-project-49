from random import randint


NUMBER_START_RAND_FROM = 0
NUMBER_END_RAND_WITH = 100
LENGTH_START_RAND_FROM = 6
LENGTH_END_RAND_WITH = 10
STEP_START_RAND_FROM = 0
STEP_END_RAND_WITH = 10


def generate_question():
    random_number = randint(NUMBER_START_RAND_FROM, NUMBER_END_RAND_WITH)
    progression_length = randint(LENGTH_START_RAND_FROM, LENGTH_END_RAND_WITH)
    progression_step = randint(STEP_START_RAND_FROM, STEP_END_RAND_WITH)
    missing_point = randint(0, progression_length - 1)
    random_input = ''
    i = 0
    while i < progression_length:
        if i == missing_point:
            random_input += '.. '
        else:
            random_input += str(random_number + (i * progression_step)) + ' '
        i += 1
    correct_answer = str(random_number + (missing_point * progression_step))
    return (random_input, correct_answer)
