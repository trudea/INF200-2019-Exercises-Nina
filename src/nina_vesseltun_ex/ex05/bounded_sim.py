# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'


from random import randint
# noinspection PyUnresolvedReferences
from walker_sim import Simulation
# noinspection PyUnresolvedReferences
from walker_sim import Walker


class BoundedWalker(Walker):
    def __init__(self, start, home, left_lim, right_lim):
        super().__init__(start, home)
        self.left_limit = left_lim
        self.right_limit = right_lim

    def move(self):
        if randint(0, 1):
            if self.x < right_limit:
                self.x += 1
                self.steps += 1
        else:
            if self.x > left_limit:
                self.x -= 1
                self.steps += 1


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_lim, right_lim):
        super().__init__(start, home, seed)
        self.left_limit = left_lim
        self.right_limit = right_lim

    def single_walk(self):
        pedestrian = BoundedWalker(self.start, self.home, self.left_limit,
                                   self.right_limit)
        play = True
        while play:
            pedestrian.move()
            if pedestrian.is_at_home():
                play = False
        return pedestrian.get_steps()


if __name__ == "__main__":
    right_limit = 20
    for left_limit in [0, - 10, -100, -1000, -10000]:
        walker_class = BoundedSimulation(0, 20, 7, left_limit, right_limit)
        liste = walker_class.run_simulation(20)
        print(f'With left limit = {left_limit}: ', liste)
