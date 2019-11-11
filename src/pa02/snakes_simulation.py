# -*- coding: utf-8 -*-

__author__ = 'Trude Haug Almestrand', 'Nina Mariann Vesseltun'
__email__ = 'Trude.haug.almestrand@nmbu.no', 'nive@nmbu.no'

class Board():
    c = [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27), (74, 12), (87, 70)]
    l = [(1, 40), (8, 10), (36, 52), (43, 62), (49, 79), (65, 82), (68, 85)]
    def __init__(self, chutes=[(24, 5), (33, 3), (42, 30), (56, 37), (64, 27),
        (74, 12), (87, 70)], ladders=[(1, 40), (8, 10), (36, 52), (43, 62),
                                      (49, 79), (65, 82), (68, 85)], goal=90):
        self.chutes = chutes
        self.ladders = ladders
        self.goal = goal

    def goal_reached(self, position):
        return position >= 90

    def position_adjustment(self, position):
        # NB! Husk at denne ikke faktisk endrer posisjonen, bare sier hvor mye
        # den skal endres
        for i in range(len(self.chutes)):
            if position == self.chutes[i][0]:
                return self.chutes[i][1] - position
            if position == self.ladders[i][0]:
                return self.ladders[i][1] - position
        else:
            return 0


class Player:
    def __init__(self, board):
        self.board = board

    def move(self):
        pass

b = Board()
p = Player(b)

