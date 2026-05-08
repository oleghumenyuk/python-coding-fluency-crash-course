"""
Problem 28: K Closest Points to the Origin

Given a list of 2D points (each as `[x, y]`) and an integer `k`, return
the `k` points closest to the origin `(0, 0)` by Euclidean distance.
The order of returned points does not matter — the test compares as a
set of tuples.

Note: you can compare using SQUARED distance (x*x + y*y) since the sqrt
is monotonic. Skipping it is faster and avoids floating point.

Example:
    k_closest([[1, 3], [-2, 2]], 1) -> [[-2, 2]]
        (distances: 1+9=10, 4+4=8 — second is closer)

    k_closest([[3, 3], [5, -1], [-2, 4]], 2) -> [[3, 3], [-2, 4]]
        (distances: 18, 26, 20 — closest two are [3,3] and [-2,4])

    k_closest([[1, 0]], 1) -> [[1, 0]]

Assumptions:
    - 1 <= k <= len(points)

What this tests:
    `heapq` mechanics. Two solid approaches:
        1. heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)
        2. Push all points into a min-heap as (dist, point), then pop k.
    Try the one-liner first, then the explicit-heap version.
"""

import heapq


def k_closest(points, k):
    pass


def _normalize(points):
    return sorted(tuple(p) for p in points)


if __name__ == "__main__":
    assert _normalize(k_closest([[1, 3], [-2, 2]], 1)) == _normalize([[-2, 2]])
    assert _normalize(k_closest([[3, 3], [5, -1], [-2, 4]], 2)) == _normalize([[3, 3], [-2, 4]])
    assert _normalize(k_closest([[1, 0]], 1)) == _normalize([[1, 0]])
    assert _normalize(k_closest([[0, 1], [1, 0], [2, 2]], 2)) == _normalize([[0, 1], [1, 0]])

    print("All tests passed.")
