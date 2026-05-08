"""
Problem 17: Group Anagrams

Given a list of strings, group strings that are anagrams of each other.
Return a list of groups (each group is a list of the original strings).
The order of groups and the order within groups do NOT matter — the test
will normalize before comparing.

Two strings are anagrams if they contain the same characters with the
same counts (just rearranged).

Example:
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
       (in any order, e.g. [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        is also fine)

More examples:
    group_anagrams([""]) -> [[""]]
    group_anagrams(["a"]) -> [["a"]]
    group_anagrams([])    -> []

What this tests:
    `defaultdict(list)` keyed by a canonical form of each string. Two
    common keys:
        - tuple(sorted(s))     — simple, O(k log k) per string
        - a 26-letter count tuple — O(k) per string but more code
    Either is fine here.
"""


def group_anagrams(strs):
    pass


def _normalize(groups):
    """Helper: sort within each group, then sort the groups themselves."""
    return sorted([sorted(g) for g in groups])


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert _normalize(result) == _normalize(expected), f"got {result}"

    assert _normalize(group_anagrams([""])) == _normalize([[""]])
    assert _normalize(group_anagrams(["a"])) == _normalize([["a"]])
    assert group_anagrams([]) == []

    print("All tests passed.")
