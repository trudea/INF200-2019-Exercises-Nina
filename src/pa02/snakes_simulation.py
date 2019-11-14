# -*- coding: utf-8 -*-

__author__ = 'Trude Haug Almestrand', 'Nina Mariann Vesseltun'
__email__ = 'Trude.haug.almestrand@nmbu.no', 'nive@nmbu.no'


from random import randint, shuffle


class Board():
    chu = [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27), (74, 12), (87, 70)]
    lad = [(1, 40), (8, 10), (36, 52), (43, 62), (49, 79), (65, 82), (68, 85)]

    def __init__(self, chutes=chu, ladders=lad, goal=90):
        """

        :param chutes: Lists of tuples with start and end positions for chutes
        :param ladders: Lists of tuples with start and end positions for
        ladders
        :param goal: End position for board
        """
        self.chutes = chutes
        self.ladders = ladders
        self.goal = goal

    def goal_reached(self, position):
        """

        :param position: The position of player
        :return: Boolean expression
        """
        return position >= 90

    def position_adjustment(self, position):
        """

        :param position: The position of player
        :return: Number of positions the player has to adjust
        """

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
        """

        :return: Updates class variable position
        """
        self.position += randint(1, 6)
        self.position += self.board.position_adjustment(self.position)


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.extra_steps = extra_steps
        self.added_steps = 0

    def move(self):
        """

        :return: Updates class variable position
        """
        self.position += randint(1, 6) + self.added_steps
        remembered_position = self.position
        self.position += self.board.position_adjustment(self.position)
        if self.position < remembered_position:
            self.added_steps = self.extra_steps
        else:
            self.added_steps = 0


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.dropped_steps = dropped_steps
        self.steps_back = 0

    def move(self):
        """

        :return: Updates class variable position
        """
        dice = randint(1, 6)
        if dice - self.steps_back >= 0:
            self.position += dice - self.steps_back
        remembered_position = self.position
        self.position += self.board.position_adjustment(self.position)
        if self.position > remembered_position:
            self.steps_back = self.dropped_steps
        else:
            self.steps_back = 0


class Simulation:
    def __init__(self, player_field, board=None, seed=None,
                 randomize_players=True):
        self.player_field = player_field
        self.board = board
        self.results = []
        if not self.board:
            self.board = Board()
        self.seed = seed
        self.randomize_players = randomize_players

    def single_game(self):
        """

        :return: A tuple of winning number of moves and player type of winner
        """
        moves = 0
        player_list = []
        for field in self.player_field:
            player_list.append(field(self.board))
        if self.randomize_players:
            shuffle(player_list)
        while True:
            for player in player_list:
                player.move()
                if self.board.goal_reached(player.position):
                    # return moves, str(player.__class__.__name__)
                    return moves, type(player).__name__
            moves += 1

    def run_simulation(self, games=1):
        """

        :param games: Number of times to simulate
        """
        temp_results = [0]*games
        for i in range(games):
            temp_results[i] = self.single_game()
        self.results += temp_results

    def get_results(self):
        """

        :return: List of simulation results
        """
        return self.results

    def winners_per_type(self):
        """

        :return: Dictionary with type of player as key, and number of wins as
        value
        """
        winners = {}
        for i in range(len(self.results)):
            if self.results[i][1] not in winners:
                winners[self.results[i][1]] = 1
            else:
                winners[self.results[i][1]] += 1
        return winners

    def durations_per_type(self):
        """

        :return: Dictionary with player as key and a list of durations for
        each type of winner as value
        """
        durations = {}
        for i in range(len(self.results)):
            if self.results[i][1] not in durations:
                durations[self.results[i][1]] = [self.results[i][0]]
            else:
                durations[self.results[i][1]].append(self.results[i][0])
        return durations

    def players_per_type(self):
        """

        :return: Dictionary with types of players as key and number of players
        of that type as value
        """
        player_types = {}
        player_list = []
        for field in self.player_field:
            player_list.append(field(self.board))
        for i in range(len(player_list)):
            player_list[i] = type(player_list[i]).__name__
        for player in player_list:
            if player not in player_types:
                player_types[player] = 1
            else:
                player_types[player] += 1
        return player_types
