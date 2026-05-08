"""
Problem 3: Transpose a Matrix (By Hand, Then with zip)

Given a 2D list `matrix`, return its transpose: rows become columns and
columns become rows.

Implement TWO versions:
    transpose_manual(matrix) -> use nested loops only
    transpose_zip(matrix)    -> use zip(*matrix) in one line

Both should return a list of lists (not a list of tuples), and both should
return identical output.

Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    transpose -> [
        [1, 4],
        [2, 5],
        [3, 6],
    ]

Another example:
    matrix = [[1]]
    transpose -> [[1]]

Assumptions:
    - The matrix is rectangular and non-empty.

What this tests:
    The by-hand mechanic of building a new matrix with swapped dimensions,
    plus recognition of the idiomatic `[list(col) for col in zip(*matrix)]`
    shortcut. zip returns tuples, so the list() wrap matters.
"""


def transpose_manual(matrix):
    pass


def transpose_zip(matrix):
    pass


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert transpose_manual(m) == expected
    assert transpose_zip(m) == expected

    assert transpose_manual([[1]]) == [[1]]
    assert transpose_zip([[1]]) == [[1]]

    square = [[1, 2], [3, 4]]
    assert transpose_manual(square) == [[1, 3], [2, 4]]
    assert transpose_zip(square) == [[1, 3], [2, 4]]

    print("All tests passed.")
