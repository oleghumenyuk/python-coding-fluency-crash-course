"""
Problem 6: Flood Fill

Given a 2D grid `image`, a starting cell `(sr, sc)`, and a `new_color`,
replace the color of the starting cell and ALL 4-connected cells of the
same original color with `new_color`. Return the modified image.

"4-connected" means up, down, left, right (no diagonals).

Example:
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]
    sr, sc = 1, 1
    new_color = 2

    flood_fill(image, sr, sc, new_color) -> [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]

    The bottom-right 1 is NOT changed because it isn't connected to (1,1)
    through cells of value 1.

Edge case — same color (no-op):
    image = [[0, 0], [0, 0]]
    flood_fill(image, 0, 0, 0) -> [[0, 0], [0, 0]]
    Be careful: if you don't guard against this, you'll infinite-loop.

Assumptions:
    - The grid is rectangular and non-empty.
    - (sr, sc) is a valid cell.

What this tests:
    Recursive (or stack-based) traversal with a directions array
    `[(-1, 0), (1, 0), (0, -1), (0, 1)]`, plus the "guard against
    same color" edge case.
"""


def flood_fill(image, sr, sc, new_color):
    pass


if __name__ == "__main__":
    img = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    assert flood_fill(img, 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    # Same-color no-op
    img2 = [[0, 0], [0, 0]]
    assert flood_fill(img2, 0, 0, 0) == [[0, 0], [0, 0]]

    # Single cell
    assert flood_fill([[5]], 0, 0, 9) == [[9]]

    # Disconnected region — only the connected component changes
    img3 = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    assert flood_fill(img3, 0, 0, 7) == [[7, 0, 1], [0, 0, 0], [1, 0, 1]]

    print("All tests passed.")
