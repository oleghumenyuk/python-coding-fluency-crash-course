"""
Problem 33: Generate All Permutations

Given a list of distinct integers `nums`, return all possible
permutations. Order of returned permutations does NOT matter — the test
compares as a set of tuples.

Implement TWO versions:
    permutations_manual(nums) -> by hand, recursively
    permutations_lib(nums)    -> using itertools.permutations

Both should return a list of lists with identical content (order may vary).

Example:
    permutations_manual([1, 2, 3]) -> [
        [1, 2, 3], [1, 3, 2],
        [2, 1, 3], [2, 3, 1],
        [3, 1, 2], [3, 2, 1],
    ]   (in any order)

    permutations_manual([])  -> [[]]
    permutations_manual([5]) -> [[5]]
    permutations_manual([1, 2]) -> [[1, 2], [2, 1]]

For a list of n elements, there are n! permutations.

What this tests:
    Recursive enumeration where you "pick one, recurse on the rest":
        def helper(remaining, current):
            if not remaining:
                result.append(list(current))
                return
            for i, x in enumerate(remaining):
                helper(remaining[:i] + remaining[i+1:], current + [x])
    Then the one-liner with `itertools.permutations` for muscle memory.
"""

from itertools import permutations as _perm


def permutations_manual(nums):
    pass


def permutations_lib(nums):
    pass


def _normalize(perms):
    return sorted(tuple(p) for p in perms)


if __name__ == "__main__":
    expected = [
        [1, 2, 3], [1, 3, 2],
        [2, 1, 3], [2, 3, 1],
        [3, 1, 2], [3, 2, 1],
    ]
    assert _normalize(permutations_manual([1, 2, 3])) == _normalize(expected)
    assert _normalize(permutations_lib([1, 2, 3])) == _normalize(expected)

    assert _normalize(permutations_manual([])) == _normalize([[]])
    assert _normalize(permutations_lib([])) == _normalize([[]])

    assert _normalize(permutations_manual([5])) == _normalize([[5]])
    assert _normalize(permutations_manual([1, 2])) == _normalize([[1, 2], [2, 1]])

    # Size check (4! = 24)
    assert len(permutations_manual([1, 2, 3, 4])) == 24

    print("All tests passed.")
