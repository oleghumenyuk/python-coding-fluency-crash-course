"""
Problem 10: Enumerate Above Threshold

Given a list of numbers and a threshold, return a list of (index, value)
tuples for every value STRICTLY greater than the threshold, preserving
original order.

Constraint: use `enumerate`, not `range(len(nums))`.

Example:
    nums = [10, 5, 20, 3, 15]
    threshold = 8

    above_threshold(nums, 8) -> [(0, 10), (2, 20), (4, 15)]

More examples:
    above_threshold([1, 2, 3], 5) -> []
    above_threshold([], 0)        -> []
    above_threshold([5, 5, 5], 5) -> []   (strictly greater, not >=)

What this tests:
    Reflexive use of `enumerate(nums)` instead of indexing manually.
"""


def above_threshold(nums, threshold):
    pass


if __name__ == "__main__":
    assert above_threshold([10, 5, 20, 3, 15], 8) == [(0, 10), (2, 20), (4, 15)]
    assert above_threshold([1, 2, 3], 5) == []
    assert above_threshold([], 0) == []
    assert above_threshold([5, 5, 5], 5) == []
    assert above_threshold([-1, 0, 1], -1) == [(1, 0), (2, 1)]

    print("All tests passed.")
