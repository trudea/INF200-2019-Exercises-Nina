# -*- coding: utf-8 -*-

__author__ = 'Trude Haug Almestrand', 'Nina Mariann Vesseltun'
__email__ = 'Trude.haug.almestrand@nmbu.no', 'nive@nmbu.no'


from random import randint


class Board():
    c = [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27), (74, 12), (87, 70)]
    l = [(1, 40), (8, 10), (36, 52), (43, 62), (49, 79), (65, 82), (68, 85)]
    def __init__(self, chutes=c, ladders=l, goal=90):
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
        self.position = 0

    def move(self):
        self.position += randint(1, 6)
        self.position += self.board.position_adjustment(self.position)


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.extra_steps = extra_steps


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.dropped_steps = dropped_steps


class Simulation:
    results = []

    def __init__(self, player_field, board=None, seed=999, randomize_players=True):
        self.player_field = player_field
        self.board = board
        if not self.board:
            self.board = Board()
        self.seed = seed
        self.randomize_players = randomize_players

    def single_game(self):
        moves = 0
        player_list = []
        for field in self.player_field:
            player_list.append(field(self.board))
        print(type(player_list[0]))
        while True:
            for player in player_list:
                player.move()
                moves += 1
                if self.board.goal_reached(player.position):
                    return moves, print(player)

    def get_results(self):
        return self.results

    def run_simulation(self, games=1):
        temp_results = [0]*games
        for i in range(games):
            temp_results[i] = self.single_game()
        self.results.append(temp_results)

    def simulation_results(self):
        pass




b = Board()
p = Player(b)
s = Simulation([Player])
print(type(s.single_game()))

