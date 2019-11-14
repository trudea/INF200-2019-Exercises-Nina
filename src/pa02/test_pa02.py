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






