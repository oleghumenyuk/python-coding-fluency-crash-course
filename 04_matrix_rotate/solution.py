"""
Problem 4: Rotate an n x n Matrix 90 Degrees Clockwise, In Place

Given an n x n matrix, rotate it 90 degrees clockwise WITHOUT allocating
a new matrix. Mutate the input in place and return None (or return the
mutated matrix — your call, but don't build a fresh 2D list).

Example:
    Input:
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    After rotate_in_place(matrix), the matrix becomes:
        [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]

Another example (2x2):
    Input:  [[1, 2], [3, 4]]
    After:  [[3, 1], [4, 2]]

Assumptions:
    - The matrix is square (n x n) and non-empty.

What this tests:
    The classic transpose-then-reverse-each-row trick, OR the four-cell
    cycle swap. Either approach must mutate in place — no `return [...]`
    with a freshly built matrix.
"""


def rotate_in_place(matrix):
    pass


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_in_place(m)
    assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]], f"got {m}"

    m = [[1, 2], [3, 4]]
    rotate_in_place(m)
    assert m == [[3, 1], [4, 2]], f"got {m}"

    m = [[1]]
    rotate_in_place(m)
    assert m == [[1]]

    print("All tests passed.")
