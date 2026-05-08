"""
Problem 20: Two Sum

Given a list of integers `nums` and an integer `target`, return the
indices of the two numbers that add up to `target`. Return them as a
list `[i, j]` with i < j. You may assume exactly one solution exists,
and you may not use the same element twice.

Example:
    two_sum([2, 7, 11, 15], 9) -> [0, 1]   (because 2 + 7 == 9)
    two_sum([3, 2, 4], 6)      -> [1, 2]   (because 2 + 4 == 6)
    two_sum([3, 3], 6)         -> [0, 1]   (same value, different indices)

What this tests:
    The single-pass dict lookup pattern:
        seen = {}
        for i, x in enumerate(nums):
            if (target - x) in seen:
                return [seen[target - x], i]
            seen[x] = i
    O(n) time, O(n) space — much better than the O(n^2) double loop.
"""


def two_sum(nums, target):
    pass


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

    print("All tests passed.")
