from random import randint as make_random_number

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'


def ask_for_guess():
    guess = 0
    while guess < 1:
        guess = int(input('Your guess: '))
    return guess


def create_random_number():
    return make_random_number(1, 6) + make_random_number(1, 6)


def check_if_correct(right_number, guess):
    return right_number == guess


if __name__ == '__main__':

    stop_game = False
    number_of_tries = 3
    n = create_random_number()
    while not stop_game and number_of_tries > 0:
        guessed_number = ask_for_guess()
        number = check_if_correct(n, guessed_number)
        if not stop_game:
            print('Wrong, try again!')
            number_of_tries -= 1

    if number_of_tries > 0:
        print('You won {} points.'.format(number_of_tries))
    else:
        print('You lost. Correct answer: {}.'.format(n))
