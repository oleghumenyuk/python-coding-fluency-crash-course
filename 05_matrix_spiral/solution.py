"""
Problem 5: Spiral Order Traversal

Given an m x n matrix, return a list of its elements in spiral order:
right across the top row, down the right column, left across the bottom
row, up the left column, then spiral inward.

Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    spiral_order(matrix) -> [1, 2, 3, 6, 9, 8, 7, 4, 5]

Another example (rectangular):
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    spiral_order(matrix) -> [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

Edge case:
    spiral_order([[1]]) -> [1]
    spiral_order([[1, 2, 3]]) -> [1, 2, 3]   (single row)
    spiral_order([[1], [2], [3]]) -> [1, 2, 3]   (single column)

Assumptions:
    - The matrix is rectangular and non-empty.
    - m and n may differ.

What this tests:
    The four-boundary-pointers pattern (top, bottom, left, right) and
    careful loop termination. This pattern reappears in many grid problems.
"""


def spiral_order(matrix):
    pass


if __name__ == "__main__":
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert spiral_order([[1]]) == [1]
    assert spiral_order([[1, 2, 3]]) == [1, 2, 3]
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]

    print("All tests passed.")
