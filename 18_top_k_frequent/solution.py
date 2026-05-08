"""
Problem 18: Top K Frequent Elements

Given a list of integers `nums` and an integer `k`, return the `k` most
frequent elements. The order of the returned list does not matter — the
test will compare as a set.

Example:
    top_k_frequent([1, 1, 1, 2, 2, 3], 2) -> [1, 2]   (or [2, 1])
    top_k_frequent([1], 1)                -> [1]
    top_k_frequent([4, 4, 4, 5, 5, 6], 1) -> [4]
    top_k_frequent([1, 2, 3, 4], 4)       -> [1, 2, 3, 4]   (any order)

Assumptions:
    - 1 <= k <= number of distinct values in nums
    - nums is non-empty

What this tests:
    `Counter(nums).most_common(k)` is the one-liner. Try this first, then
    rewrite using a heap (`heapq.nlargest`) as a follow-up to practice
    the heap version of the pattern.
"""

from collections import Counter


def top_k_frequent(nums, k):
    pass


if __name__ == "__main__":
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert top_k_frequent([1], 1) == [1]
    assert set(top_k_frequent([4, 4, 4, 5, 5, 6], 1)) == {4}
    assert set(top_k_frequent([1, 2, 3, 4], 4)) == {1, 2, 3, 4}

    print("All tests passed.")
