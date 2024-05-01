from random import randint


NUMBER_START_RAND_FROM = 0
NUMBER_END_RAND_WITH = 100
LENGTH_START_RAND_FROM = 6
LENGTH_END_RAND_WITH = 10
STEP_START_RAND_FROM = 0
STEP_END_RAND_WITH = 10
QUESTION = 'What number is missing in the progression?'


def generate_progression(begin, length, step):
    list_ = []
    i = 0
    while i < length:
        list_.append(begin + i * step)
        i += 1
    return list_


def generate_question():
    begin = randint(NUMBER_START_RAND_FROM, NUMBER_END_RAND_WITH)
    length = randint(LENGTH_START_RAND_FROM, LENGTH_END_RAND_WITH)
    step = randint(STEP_START_RAND_FROM, STEP_END_RAND_WITH)
    missing_point = randint(0, length - 1)
    random_input = ''
    i = 0
    progression = generate_progression(begin, length, step)
    while i < length:
        if i == missing_point:
            random_input += '.. '
        else:
            random_input += str(progression[i]) + ' '
        i += 1
    correct_answer = str(begin + (missing_point * step))
    return (random_input, correct_answer)
