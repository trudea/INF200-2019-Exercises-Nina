# -*- coding: utf-8 -*-

__author__ = 'Nina Mariann Vesseltun'
__email__ = 'nive@nmbu.no'


def bubble_sort(datavariable):
    copy = list(datavariable)
    for i in range(len(copy) - 1):
        for j in range(len(copy) - i - 1):
            if copy[j] > copy[j + 1]:
                copy[j], copy[j + 1] = copy[j + 1], copy[j]
    return copy


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1] == [1])


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    liste = [3, 1, 2]
    assert id(liste) != id(bubble_sort(liste))


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 1, 2]
    sorted_data = bubble_sort(data)
    sorted_data += 1
    assert data == data


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [3, 1, 2]
    sorted_data = bubble_sort(data)
    doubly_sorted_data = bubble_sort(sorted_data)
    assert doubly_sorted_data == sorted_data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = list(range(10))
    reversed_data = data[::-1]
    assert bubble_sort(reversed_data) == bubble_sort(data)


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [1] * 10
    assert bubble_sort(data) == data


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    numeric_data = [9, 4, 3, 7, 1, 6, 8, 2, 5]
    correct_numeric = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    string_data = 'afecdb'
    correct_string = 'abcdef'
    assert numeric_data == correct_numeric and string_data == correct_string
