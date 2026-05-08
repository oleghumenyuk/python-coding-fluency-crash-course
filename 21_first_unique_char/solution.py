"""
Problem 21: First Non-Repeating Character

Given a string `s`, return the FIRST character that appears exactly once.
If every character repeats (or the string is empty), return None.

Example:
    first_unique("leetcode")     -> "l"
    first_unique("loveleetcode") -> "v"
    first_unique("aabb")         -> None
    first_unique("")             -> None
    first_unique("z")            -> "z"

What this tests:
    A two-pass pattern:
        1. Count characters with a dict (or Counter).
        2. Iterate the string in order and return the first char with
           count == 1.
    The key insight: order matters, so you have to revisit the original
    string — you can't read it off the counts dict directly.
"""


def first_unique(s):
    pass


if __name__ == "__main__":
    assert first_unique("leetcode") == "l"
    assert first_unique("loveleetcode") == "v"
    assert first_unique("aabb") is None
    assert first_unique("") is None
    assert first_unique("z") == "z"
    assert first_unique("aabbcc d") == " "  # space appears exactly once

    print("All tests passed.")
