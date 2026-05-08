"""
Problem 31: Min, Max, Mean in One Pass

Given a non-empty list of numbers, return a tuple `(min_val, max_val, mean)`
computed in a SINGLE pass over the list. Do not use the built-in `min`,
`max`, or `sum` on the list.

The mean should be a float.

Example:
    min_max_mean([1, 2, 3, 4, 5]) -> (1, 5, 3.0)
    min_max_mean([42])            -> (42, 42, 42.0)
    min_max_mean([-1, -5, -3])    -> (-5, -1, -3.0)
    min_max_mean([2, 2, 2, 2])    -> (2, 2, 2.0)

Assumptions:
    - The list is non-empty.

What this tests:
    Multi-return tuples and tracking multiple accumulators in one loop:
        lo = hi = nums[0]
        total = 0
        for x in nums:
            if x < lo: lo = x
            if x > hi: hi = x
            total += x
        return (lo, hi, total / len(nums))
"""


def min_max_mean(nums):
    pass


if __name__ == "__main__":
    assert min_max_mean([1, 2, 3, 4, 5]) == (1, 5, 3.0)
    assert min_max_mean([42]) == (42, 42, 42.0)
    assert min_max_mean([-1, -5, -3]) == (-5, -1, -3.0)
    assert min_max_mean([2, 2, 2, 2]) == (2, 2, 2.0)

    print("All tests passed.")
