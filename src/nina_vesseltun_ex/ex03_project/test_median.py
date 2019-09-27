# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
        else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


def test_single():
    dataset = [1]
    assert median(dataset) == 1


def test_odd():
    dataset = [1, 2, 3]
    assert median(dataset) == 2


def test_even():
    dataset = [1, 2, 3]
    assert median(dataset) == 2


def test_order():
    unordered_dataset = [3, 4, 5, 1, 2]
    ordered_dataset = [1, 2, 3, 4, 5]
    reversed_dataset = ordered_dataset[::-1]
    assert median(unordered_dataset) == 3 and median(ordered_dataset) ==3 and
    median(reversed_dataset) == 3


def test_req_empty():
    assert median([]) == ValueError


def test_unchanged():
    dataset = [1, 2, 3]
    temp = median(dataset)
    assert dataset == dataset


def test_tuple():
    dataset = (1, 2, 3)
    assert median(dataset) == 2


test_single()