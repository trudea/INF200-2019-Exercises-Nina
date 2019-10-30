# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'


class LCGRand:
    a = 16807
    m = 2 ** 31 - 1

    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        while True:
            self.seed = self.a * self.seed % self.m
            return self.seed

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        while True:
            yield self.rand()


class RandIter:
    def __init__(self, random_number_generator, length):
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        if self.num_generated_numbers is not None:
            raise RuntimeError(
                'Iterator is already initialised'
            )
        self.num_generated_numbers = 0
        return self

    def __next__(self):
        if self.num_generated_numbers is None:
            raise RuntimeError('RandIter is not initialised yet')
        if self.num_generated_numbers == self.length:
            raise StopIteration
        generated_number = self.generator.rand()
        self.num_generated_numbers += 1
        return generated_number


if __name__ == "__main__":
    generator = LCGRand(1)

    for rand in generator.random_sequence(10):
        print(rand)

    for i, rand in enumerate(generator.infinite_random_sequence()):
        print(f'The {i}-th random number is {rand}')
        if i > 100:
            break
