"""
Problem 23: Ordered Intersection of Two Lists

Given two lists `a` and `b`, return a list of values that appear in
BOTH lists. Preserve the order of first occurrence as it appears in `a`,
and deduplicate the result.

Example:
    ordered_intersection([1, 2, 2, 3, 4], [2, 4, 5]) -> [2, 4]
    ordered_intersection([3, 1, 2], [2, 1, 3])       -> [3, 1, 2]
        (order from `a`)
    ordered_intersection([1, 2], [3, 4])             -> []
    ordered_intersection([], [1, 2])                 -> []
    ordered_intersection([1, 1, 1], [1])             -> [1]

What this tests:
    Combining a set (for fast O(1) membership in `b`) with a list and a
    "seen" set (for order preservation and dedup):
        b_set = set(b)
        seen = set()
        out = []
        for x in a:
            if x in b_set and x not in seen:
                out.append(x)
                seen.add(x)
        return out
"""


def ordered_intersection(a, b):
    pass


if __name__ == "__main__":
    assert ordered_intersection([1, 2, 2, 3, 4], [2, 4, 5]) == [2, 4]
    assert ordered_intersection([3, 1, 2], [2, 1, 3]) == [3, 1, 2]
    assert ordered_intersection([1, 2], [3, 4]) == []
    assert ordered_intersection([], [1, 2]) == []
    assert ordered_intersection([1, 1, 1], [1]) == [1]

    print("All tests passed.")
