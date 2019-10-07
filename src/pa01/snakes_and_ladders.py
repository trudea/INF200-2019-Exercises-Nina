# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun', 'Elin Woelner Bjoernson'
__email__ = 'nive@nmbu.no', 'elinbj@nmbu.no'


import random

def chute_or_ladder(position):
    from_ladder = [1, 8, 36, 43, 49, 65, 68]

    return new_position


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
    for i in num_players:
        player_position.append(0)  # everybody starts at position 0
        player_moves.append(0)  # starts with 0 moves
    play = True
    while play is True:
        for player in num_players:
            dice = random.randint(1, 6)
            player_position[player] += dice
            player_moves[player] += 1



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
