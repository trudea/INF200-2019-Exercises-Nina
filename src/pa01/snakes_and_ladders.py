# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun', 'Elin Woelner Bjoernson'
__email__ = 'nive@nmbu.no', 'elinbj@nmbu.no'


import random

def chute_or_ladder(position):

    from_position = [1, 8, 36, 43, 49, 65, 68, 24, 33, 42, 56, 64, 74, 87]
    to_position = [40, 10, 52, 62, 79, 82, 85, 5, 3, 30, 37, 27, 12, 70]
    if position in from_position:
        new_position = to_position[from_position.index(position)]
        return new_position
    else:
        return position


def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """
    player_position = []
    player_moves = []
    for i in range(num_players):
        player_position.append(0)  # everybody starts at position 0
        player_moves.append(0)  # starts with 0 moves
    play = True
    winning_moves = 0
    while play is True:
        for player in range(num_players):
            dice = random.randint(1, 6)
            player_position[player] += dice
            player_moves[player] += 1
            player_position[player] = chute_or_ladder(player_position[player])
            if player_position[player] >= 90:
                winning_moves = player_moves[player]
                play = False
    return winning_moves

def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """

if __name__ == '__main__':
    print(single_game(3))