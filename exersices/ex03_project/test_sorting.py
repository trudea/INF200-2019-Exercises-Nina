# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'

def bubble_sort(data):    # endrer koden inne i funksjonen også listen utenfor?
    copy = list(data)     # er dette ok?
    for i in range(len(copy)-1):
        for j in range(len(copy)-i-1):
            if copy[j] > copy[j+1]:
                copy[j], copy[j+1] = copy[j+1], copy[j]
    return copy

def test_empty():
        """Test that the sorting function works for empty list"""
    pass


def test_single():
    """Test that the sorting function works for single-element list"""
    pass


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    pass


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    pass


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    pass


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    pass


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    pass


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    pass