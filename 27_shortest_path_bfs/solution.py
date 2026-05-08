"""
Problem 27: Shortest Path in a Grid (BFS)

Given a 2D grid where:
    0 = passable cell
    1 = blocked cell

Return the LENGTH of the shortest path (counted as the number of cells
visited, including both start and end) from `(0, 0)` to
`(rows-1, cols-1)`, moving only 4-directionally (up/down/left/right).

If `(0, 0)` or the destination is blocked, or no path exists, return -1.

Example:
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    shortest_path(grid) -> 5
        (path: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2), 5 cells)

More examples:
    shortest_path([[0]]) -> 1
    shortest_path([[1]]) -> -1   (start blocked)
    shortest_path([[0, 1], [1, 0]]) -> -1   (no path; diagonals not allowed)
    shortest_path([[0, 0], [0, 0]]) -> 3

Assumptions:
    - The grid is rectangular and non-empty.

What this tests:
    BFS with `collections.deque`:
        - Push the start with its distance.
        - On each pop, check if you've reached the destination.
        - Otherwise, push every unvisited 4-neighbor with distance + 1.
    Always use `popleft()` (O(1)) — never `pop(0)` (O(n) on a list).
    A `visited` set prevents re-enqueuing.
"""

from collections import deque


def shortest_path(grid):
    pass


if __name__ == "__main__":
    assert shortest_path([[0, 0, 0], [1, 1, 0], [0, 0, 0]]) == 5
    assert shortest_path([[0]]) == 1
    assert shortest_path([[1]]) == -1
    assert shortest_path([[0, 1], [1, 0]]) == -1
    assert shortest_path([[0, 0], [0, 0]]) == 3
    # Destination blocked
    assert shortest_path([[0, 0], [0, 1]]) == -1

    print("All tests passed.")
