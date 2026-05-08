"""
Problem 8: Flatten a 2D List

Given a list of lists, return a single flat list containing every element
in row-major order (left-to-right, top-to-bottom).

Constraint: write the body as a SINGLE nested list comprehension.

Example:
    flatten([[1, 2], [3, 4], [5]]) -> [1, 2, 3, 4, 5]
    flatten([[1, 2, 3]])           -> [1, 2, 3]
    flatten([])                    -> []
    flatten([[]])                  -> []

What this tests:
    Reading order of nested comprehensions. The "outer" loop comes first:
        [x for row in matrix for x in row]
    The order matches what you'd write as nested for-loops, which is
    backwards from how many people first read it.
"""


def flatten(matrix):
    pass


if __name__ == "__main__":
    assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert flatten([[1, 2, 3]]) == [1, 2, 3]
    assert flatten([]) == []
    assert flatten([[]]) == []
    assert flatten([[1], [2], [3]]) == [1, 2, 3]

    print("All tests passed.")
