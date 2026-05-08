"""
Problem 1: Print a Matrix Row by Row, Then Column by Column

Given a 2D list `matrix`, implement two functions that PRINT (not return)
its contents in two different orders.

    print_by_rows(matrix)    -> prints each row on its own line
    print_by_columns(matrix) -> prints each column on its own line

Values within a line should be separated by single spaces.

Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    print_by_rows(matrix) prints:
        1 2 3
        4 5 6

    print_by_columns(matrix) prints:
        1 4
        2 5
        3 6

Assumptions:
    - The matrix is rectangular (every row has the same length).
    - The matrix is non-empty.

What this tests:
    Reflexive use of nested for-loops in both row-major and column-major
    order. There is no clever algorithm here; the point is to write the
    indexing without thinking.
"""


def print_by_rows(matrix):
    pass


def print_by_columns(matrix):
    pass


if __name__ == "__main__":
    # Visual verification — eyeball the output against the expected block.
    m = [[1, 2, 3], [4, 5, 6]]

    print("By rows (expect: '1 2 3' then '4 5 6'):")
    print_by_rows(m)

    print("\nBy columns (expect: '1 4' then '2 5' then '3 6'):")
    print_by_columns(m)
