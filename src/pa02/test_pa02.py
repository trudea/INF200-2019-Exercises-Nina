# -*- coding: utf-8 -*-

__author__ = 'Trude Haug Almestrand', 'Nina Mariann Vesseltun'
__email__ = 'Trude.haug.almestrand@nmbu.no', 'nive@nmbu.no'

import src.pa02.snakes_simulation as cs
import random


def test_standard_board():
    """Checking if standard board created is correct"""
    b = cs.Board()
    assert b.chutes == [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27),
                        (74, 12), (87, 70)]
    assert b.ladders == [(1, 40), (8, 10), (36, 52), (43, 62), (49, 79),
                         (65, 82), (68, 85)]
    assert b.goal == 90


def test_goal_reached():
    """Checking if goal_reached works"""
    b = cs.Board()
    assert b.goal_reached(90) is True
    assert b.goal_reached(13) is False
    assert b.goal_reached(100) is True


def test_position_adjustment():
    """Checking if position_adjustment works"""
    b = cs.Board()
    assert b.position_adjustment(24) == -19
    assert b.position_adjustment(68) == 17
    assert b.position_adjustment(7) == 0


def test_player_move():
    """Checking that player is initially at 0, and not in the same position
    after move is called"""
    b = cs.Board()
    p = cs.Player(b)
    assert p.position == 0
    p.position = 5
    p.move()
    assert p.position != 5


def test_resilient_player():
    """Checking if ResilientPlayer behaves as desired"""
    random.seed(999)
    b = cs.Board()
    p = cs.ResilientPlayer(b)
    p.position = 36
    p.move()
    random.seed(999)
    p.move()
    assert p.position == 37


def test_lazy_player():
    """Checking if LazyPlayer behaves as desired"""
    random.seed(999)
    b = cs.Board()
    p = cs.LazyPlayer(b)
    p.position = 2
    p.move()
    random.seed(999)
    p.move()
    assert p.position == 15


def test_types():
    """Checking if returned player types are correct"""
    b = cs.Board()
    rp = cs.ResilientPlayer(b)
    assert type(rp).__name__ == 'ResilientPlayer'
    lp = cs.LazyPlayer(b)
    assert type(lp).__name__ == 'LazyPlayer'


def test_random_order():
    """Adds test to see if elements in a list is same sorted as unsorted"""
    list_of_players = [cs.Player, cs.LazyPlayer, cs.ResilientPlayer]
    b = cs.Board()
    s1 = cs.Simulation(list_of_players, b, 999)
    s2 = cs.Simulation(list_of_players, b, 999, False)
    dict1 = s1.players_per_type()
    dict2 = s2.players_per_type()
    assert dict1 == dict2


def test_single_game():
    """Checking if single_game behaves correctly"""
    s = cs.Simulation(player_field=[cs.Player, cs.ResilientPlayer,
                                    cs.LazyPlayer], seed=999)
    n, winner_type = s.single_game()
    assert type(n) == int
    assert (winner_type == 'Player' or winner_type == 'ResilientPlayer' or
            winner_type == 'LazyPlayer')


def test_run_simulation():
    """Checking that results list changes after run_simulation is called"""
    s = cs.Simulation(player_field=[cs.Player, cs.ResilientPlayer,
                                    cs.LazyPlayer], seed=999)
    s.run_simulation(2)
    first_results = s.results.copy()
    s.run_simulation()
    later_results = s.results
    assert first_results != later_results


def test_get_results():
    """Checking if get_results works"""
    s = cs.Simulation(player_field=[cs.Player, cs.ResilientPlayer,
                                    cs.LazyPlayer], seed=999)
    s.run_simulation(2)
    assert s.get_results() == s.results


def test_players_per_type():
    """Checking if players_per_type returns right result for example"""
    s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer,
                       cs.ResilientPlayer])
    types_dict = s.players_per_type()
    assert types_dict == {'Player': 1, 'ResilientPlayer': 2, 'LazyPlayer': 1}


def test_winners_per_type():
    """Checking if winners_per_type works"""
    s1 = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer,
                       cs.ResilientPlayer])
    s2 = cs.Simulation([cs.LazyPlayer, cs.LazyPlayer, cs.LazyPlayer])
    s1.run_simulation(30)
    s2.run_simulation(30)
    dict1 = s1.winners_per_type()
    dict2 = s2.winners_per_type()
    assert len(dict1) == 3
    assert len(dict2) == 1
    assert 'LazyPlayer' in dict2


def test_durations_per_type():
    """Checking if durations_per_type returns dictionary of correct length"""
    s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer,
                       cs.ResilientPlayer])
    s.run_simulation(30)
    durations_dict = s.durations_per_type()
    assert len(durations_dict) == 3
