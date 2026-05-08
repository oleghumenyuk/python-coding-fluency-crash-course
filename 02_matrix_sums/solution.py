"""
Problem 2: Row Sums and Column Sums

Given a 2D list `matrix`, return a tuple (row_sums, col_sums) where:
    - row_sums[i] is the sum of the values in row i
    - col_sums[j] is the sum of the values in column j

Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    row_sums = [6, 15]   (1+2+3, 4+5+6)
    col_sums = [5, 7, 9] (1+4, 2+5, 3+6)

    row_and_col_sums(matrix) -> ([6, 15], [5, 7, 9])

Another example:
    matrix = [[10]]
    row_and_col_sums(matrix) -> ([10], [10])

Assumptions:
    - The matrix is rectangular and non-empty.

What this tests:
    Indexed iteration without losing track of which dimension is which.
    Try to do it in a single pass over the matrix (one set of nested loops,
    not two).
"""


def row_and_col_sums(matrix):
    pass


if __name__ == "__main__":
    rows, cols = row_and_col_sums([[1, 2, 3], [4, 5, 6]])
    assert rows == [6, 15], f"expected [6, 15], got {rows}"
    assert cols == [5, 7, 9], f"expected [5, 7, 9], got {cols}"

    rows, cols = row_and_col_sums([[10]])
    assert rows == [10] and cols == [10]

    rows, cols = row_and_col_sums([[1, -1], [-1, 1]])
    assert rows == [0, 0] and cols == [0, 0]

    print("All tests passed.")
