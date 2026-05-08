"""
Problem 29: Merge K Sorted Lists

Given a list of lists, where each inner list is already sorted in
ascending order, merge them into a single sorted list.

Example:
    merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]])
    -> [1, 1, 2, 3, 4, 4, 5, 6]

    merge_k_sorted([])              -> []
    merge_k_sorted([[]])            -> []
    merge_k_sorted([[1, 2, 3]])     -> [1, 2, 3]
    merge_k_sorted([[], [1], []])   -> [1]

What this tests:
    The min-heap merge pattern. Push one element from each list as a
    tuple `(value, list_idx, elem_idx)`. Pop the smallest, append it to
    the result, and push the next element from that same list (if any).

    Why include `list_idx` in the tuple? If two values are equal, Python
    breaks the tie by comparing the next tuple element. Including the
    index makes that comparison safe even if the elements aren't
    naturally orderable.

    O(N log k) where N is total elements and k is the number of lists.
"""

import heapq


def merge_k_sorted(lists):
    pass


if __name__ == "__main__":
    assert merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_k_sorted([]) == []
    assert merge_k_sorted([[]]) == []
    assert merge_k_sorted([[1, 2, 3]]) == [1, 2, 3]
    assert merge_k_sorted([[], [1], []]) == [1]
    assert merge_k_sorted([[1, 1, 1], [1, 1], [1]]) == [1, 1, 1, 1, 1, 1]

    print("All tests passed.")
