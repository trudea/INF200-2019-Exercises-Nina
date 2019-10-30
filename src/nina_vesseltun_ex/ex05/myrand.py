# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'

from random import randint


class LCGRand:
    slope = 7 ** 5
    congruence_class = 2 ** 31 - 1

    def __init__(self, seed):
        self._hidden_state = seed

    def rand(self):
        self._hidden_state *= self.slope
        self._hidden_state %= self.congruence_class
        return self._hidden_state


    def random_sequence(self, length):
        return RandIter(self, length)


    def infinite_random_sequence(self):
        while True:
            yield randint(0,100)

class RandIter:
    def __init__(self, random_number_generator, length):
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = 0
        self.current_idx = None

    def __iter__(self):
        self.current_idx = 0
        return self

    def __next__(self):
        if self.current_idx is None:
            raise RuntimeError(
                f'{type(self)} is not initialised as an iterator.')
        if self.current_idx == self.length:
            raise StopIteration
        generator = self.generator[self.current_idx]
        self.current_idx += 1
        return generator


if __name__ == "__main__":
    generator = LCGRand(1)
    for i in generator.random_sequence(10):
        print(i)

