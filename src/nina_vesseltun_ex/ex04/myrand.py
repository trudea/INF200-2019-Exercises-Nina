# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'

from random import randint


class LCGRand:
    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        a = 16807
        m = 2 ** 31 - 1
        self.seed = a * self.seed % m
        return self.seed


class ListRand:

    def __init__(self, liste):
        self.liste = liste
        self.index = -1

    def rand(self):
        self.index += 1
        if self.index >= len(self.liste):
            raise RuntimeError
        else:
            return self.liste[self.index]


if __name__ == "__main__":
    numbers = [randint(0, 10) for i in range(5)]
    random_by_list = ListRand(numbers)
    random_by_LCG = LCGRand(3)

    for i in range(5):
        print(f'By using ListRand: {random_by_list.rand()}')
        print(f'By using LCGRand: {random_by_LCG.rand()}')
