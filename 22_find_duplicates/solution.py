"""
Problem 22: Find Duplicates

Given a list of values, return the SET of values that appear more than
once.

Example:
    find_duplicates([1, 2, 3, 2, 4, 3, 5]) -> {2, 3}
    find_duplicates([1, 2, 3])             -> set()
    find_duplicates([])                    -> set()
    find_duplicates([1, 1, 1, 1])          -> {1}
    find_duplicates(["a", "b", "a", "c"])  -> {"a"}

What this tests:
    The two-set pattern — one set tracks "seen at least once", another
    tracks "seen more than once":
        seen = set()
        dupes = set()
        for x in values:
            if x in seen:
                dupes.add(x)
            else:
                seen.add(x)
        return dupes
    O(n) time, O(n) space.
"""


def find_duplicates(values):
    pass


if __name__ == "__main__":
    assert find_duplicates([1, 2, 3, 2, 4, 3, 5]) == {2, 3}
    assert find_duplicates([1, 2, 3]) == set()
    assert find_duplicates([]) == set()
    assert find_duplicates([1, 1, 1, 1]) == {1}
    assert find_duplicates(["a", "b", "a", "c"]) == {"a"}

    print("All tests passed.")
