# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'

from random import randint


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


def walking(start, goal):
    pedestrian = Walker(start, goal)
    play = True
    while play:
        pedestrian.move()
        if pedestrian.is_at_home():
            play = False
    return pedestrian.get_steps()


if __name__ == "__main__":
    distance = [1, 2, 5, 10, 20, 50, 100]
    for i in distance:
        starting_point = 0
        end_point = starting_point + i
        simulations = []
        for j in range(5):
            simulations.append(walking(starting_point, end_point))
        print(f'Distance: {i} --> Path lengths: {simulations}')
