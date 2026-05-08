"""
Problem 19: Invert a Dict (Collecting Duplicate Values)

Given a dict whose values may collide, return an inverted dict where
each original value becomes a key, mapped to a list of the original
keys that had that value. The lists should be sorted (so the test is
deterministic).

Example:
    invert({"a": 1, "b": 2, "c": 1})
    -> {1: ["a", "c"], 2: ["b"]}

    invert({"a": "x", "b": "x", "c": "y"})
    -> {"x": ["a", "b"], "y": ["c"]}

    invert({})  -> {}
    invert({"only": 42}) -> {42: ["only"]}

What this tests:
    `defaultdict(list).append(...)` keyed by the original value, then
    sorting each list before returning. Reflexive grouping pattern.
"""

from collections import defaultdict


def invert(d):
    pass


if __name__ == "__main__":
    assert invert({"a": 1, "b": 2, "c": 1}) == {1: ["a", "c"], 2: ["b"]}
    assert invert({"a": "x", "b": "x", "c": "y"}) == {"x": ["a", "b"], "y": ["c"]}
    assert invert({}) == {}
    assert invert({"only": 42}) == {42: ["only"]}

    print("All tests passed.")
