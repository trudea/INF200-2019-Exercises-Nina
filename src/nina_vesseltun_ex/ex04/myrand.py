# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'

from random import randint


class ListRand:
    def __init__(self, liste):
        self.liste = liste
        self.current_idx = 0

    def rand(self):
        for i in self.liste:
            if self.current_idx == len(self.liste):
                raise RuntimeError
            else:
                self.current_idx += 1
                yield i


class LCGRand:
    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        a = 16807
        m = 2 ** 31 - 1
        self.seed = a * self.seed % m
        return self.seed


if __name__ == "__main__":
    numbers = [randint(0, 100) for i in range(5)]
    random_by_list_class = ListRand(numbers)
    random_by_LCG = LCGRand(3)
    x = random_by_list_class.rand()
    numbers = [4, 5, 29, 11]
    lr = ListRand(numbers)


"""
    for i in range(5):
        print(f'By using ListRand: {next(x)}', f'By using LCGRand: {random_by_LCG.rand()}')

    print(next(x))
"""