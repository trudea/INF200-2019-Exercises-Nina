# -*- coding: utf-8 -*-

__author__ = 'Trude Haug Almestrand', 'Nina Mariann Vesseltun'
__email__ = 'Trude.haug.almestrand@nmbu.no', 'nive@nmbu.no'

import src.pa02.snakes_simulation as cs
import pytest
import random

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

def test_random_order():
    """Adds test to see if elements in a list is same sorted as unsorted"""
    list_of_players = [cs.Player, cs.LazyPlayer, cs.ResilientPlayer]
    b = cs.Board()
    s1 = cs.Simulation(list_of_players, b, 999)
    s2 = cs.Simulation(list_of_players, b, 999, False)
    dict1 = s1.players_per_type()
    dict2 = s2.players_per_type()
    assert dict1 == dict2




