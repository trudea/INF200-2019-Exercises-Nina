# -*- coding: utf-8 -*-

__author__ = 'Trude Haug Almestrand', 'Nina Mariann Vesseltun'
__email__ = 'Trude.haug.almestrand@nmbu.no', 'nive@nmbu.no'

class Board():
    chutes_and_ladders = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
                          24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

    def __init__(self, chutes, ladders, goal):
        self.chutes = chutes
        self.ladders = ladders
        self.goal = goal

    def goal_reached(self, position):
        return position >= 90

    def position_adjustment(self, position):
        if position in self.chutes_and_ladders:
            return self.chutes_and_ladders[position] - position
        else:
            return 0


class Player(Board):
    def __init__(self, chutes, ladders, goals):
