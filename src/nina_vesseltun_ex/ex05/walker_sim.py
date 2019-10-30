# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'


from random import randint
from random import seed


class Walker:
    def __init__(self, x0, home):
        self.x = x0
        self.h = home
        self.steps = 0

    def move(self):
        if randint(0, 1):
            self.x += 1
        else:
            self.x -= 1
        self.steps += 1

    def is_at_home(self):
        return self.x == self.h

    def get_position(self):
        return self.x

    def get_steps(self):
        return self.steps


class Simulation:
    def __init__(self, start, home, seed):
        self.start = start
        self.home = home
        self.seed = seed

    def single_walk(self):
        pedestrian = Walker(self.start, self.home)
        play = True
        while play:
            pedestrian.move()
            if pedestrian.is_at_home():
                play = False
        return pedestrian.get_steps()

    def run_simulation(self, num_walks):
        seed(self.seed)
        return [self.single_walk() for _ in range(num_walks)]


if __name__ == "__main__":
    for _ in range(2):
        walker_class = Simulation(0, 10, 12345)
        liste = walker_class.run_simulation(20)
        print('Number of steps from 0 to 10 w/12345 as seed: ', liste)
    for _ in range(2):
        walker_class = Simulation(10, 0, 12345)
        liste = walker_class.run_simulation(20)
        print('Number of steps from 10 to 0 w/12345 as seed: ', liste)
    walker_class = Simulation(0, 10, 54321)
    liste = walker_class.run_simulation(20)
    print('Number of steps from 0 to 10 w/54321 as seed: ', liste)
    walker_class = Simulation(10, 0, 54321)
    liste = walker_class.run_simulation(20)
    print('Number of steps from 10 to 0 w/54321 as seed: ', liste)
