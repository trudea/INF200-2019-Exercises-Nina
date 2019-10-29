# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'


from walker_sim import Walker
from walker_sim import Simulation


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        super().__init__(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        super().__init__(start, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit


if __name__ == "__main__":
    for left_limit in [0, - 10, -100, -1000, -10000]:
        walker_class = BoundedSimulation(0, 20, 3, left_limit, 20)
        liste = walker_class.run_simulation(20)
        print(f'With left limit = {left_limit}: ', liste)
