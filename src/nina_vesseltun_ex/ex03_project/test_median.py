# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'


import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """
    try:
        sorted_data = sorted(data)
        num_elements = len(sorted_data)
        if num_elements % 2 == 1:
            return sorted_data[num_elements // 2]
        else:
            return (
                sorted_data[num_elements // 2 - 1] + sorted_data[num_elements
                                                                 // 2]) / 2
    except ValueError as err:
        raise err


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
    ordered_dataset = [1, 2, 3, 4, 5]  # burde brukt sorted?
    reversed_dataset = ordered_dataset[::-1]
    assert (median(unordered_dataset) == 3 and median(ordered_dataset) == 3 and
            median(reversed_dataset) == 3)


def test_req_empty():
    with pytest.raises(Exception):
        assert median([])


def test_unchanged():
    dataset = [1, 2, 3]
    assert dataset is not median(dataset)


def test_tuple():
    dataset = (1, 2, 3)
    assert median(dataset) == 2
