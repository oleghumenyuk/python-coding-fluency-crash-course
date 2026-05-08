"""
Problem 11: Zip Two Lists, Keep Pairs with Even Sum

Given two lists `a` and `b` of equal length, return a list of (a[i], b[i])
tuples where a[i] + b[i] is even.

Constraint: use `zip` and a list comprehension.

Example:
    a = [1, 2, 3, 4]
    b = [1, 3, 5, 8]
    sums: 2, 5, 8, 12 — even sums at indices 0, 2, 3
    even_sum_pairs(a, b) -> [(1, 1), (3, 5), (4, 8)]

More examples:
    even_sum_pairs([2, 4], [2, 4]) -> [(2, 2), (4, 4)]
    even_sum_pairs([1, 2], [2, 1]) -> []   (both sums are 3, odd)
    even_sum_pairs([], [])         -> []

Assumptions:
    - len(a) == len(b)

What this tests:
    `zip` combined with a filter inside a comprehension:
        [(x, y) for x, y in zip(a, b) if (x + y) % 2 == 0]
"""


def even_sum_pairs(a, b):
    pass


if __name__ == "__main__":
    assert even_sum_pairs([1, 2, 3, 4], [1, 3, 5, 8]) == [(1, 1), (3, 5), (4, 8)]
    assert even_sum_pairs([2, 4], [2, 4]) == [(2, 2), (4, 4)]
    assert even_sum_pairs([1, 2], [2, 1]) == []
    assert even_sum_pairs([], []) == []
    assert even_sum_pairs([0], [0]) == [(0, 0)]

    print("All tests passed.")
