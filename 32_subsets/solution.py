"""
Problem 32: Generate All Subsets (Power Set)

Given a list of distinct integers `nums`, return all possible subsets
(the power set). Each subset is itself a list. The order of subsets,
and the order of elements within a subset, do NOT matter — the test
will normalize before comparing.

Example:
    subsets([1, 2, 3]) -> [
        [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
    ]
    (any ordering of those 8 subsets is fine)

    subsets([])    -> [[]]
    subsets([7])   -> [[], [7]]
    subsets([1, 2]) -> [[], [1], [2], [1, 2]]

For a list of n elements, there are 2**n subsets.

What this tests:
    The classic include/exclude recursion pattern:
        def helper(i, current):
            if i == len(nums):
                result.append(list(current))
                return
            # exclude nums[i]
            helper(i + 1, current)
            # include nums[i]
            current.append(nums[i])
            helper(i + 1, current)
            current.pop()
    Iterative version with `for x in nums: result += [s + [x] for s in result]`
    is also fair game.
"""


def subsets(nums):
    pass


def _normalize(subs):
    return sorted([sorted(s) for s in subs])


if __name__ == "__main__":
    expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert _normalize(subsets([1, 2, 3])) == _normalize(expected)
    assert _normalize(subsets([])) == _normalize([[]])
    assert _normalize(subsets([7])) == _normalize([[], [7]])
    assert _normalize(subsets([1, 2])) == _normalize([[], [1], [2], [1, 2]])

    # Size check
    assert len(subsets([1, 2, 3, 4])) == 16

    print("All tests passed.")
