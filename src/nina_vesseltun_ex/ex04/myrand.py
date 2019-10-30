# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'


from random import randint


class ListRand:
    def __init__(self, liste):
        self.liste = liste
        self.current_idx = -1

    def rand(self):
        if self.current_idx == len(self.liste) - 1:
            raise RuntimeError
        else:
            self.current_idx += 1
            return self.liste[self.current_idx]


class LCGRand:
    def __init__(self, seed):
        self.a = 16807
        self.m = 2 ** 31 - 1
        self.seed = seed

    def rand(self):
        while True:
            self.seed = self.a * self.seed % self.m
            return self.seed


if __name__ == "__main__":
    numbers = [randint(0, 100) for i in range(5)]
    print(numbers)
    ListRand_instance = ListRand(numbers)
    LCG_instance = LCGRand(3)
    for _ in range(5):
        print('Generated by ListRand: ', ListRand_instance.rand(),
              'Generated by LCGRand: ', LCG_instance.rand())