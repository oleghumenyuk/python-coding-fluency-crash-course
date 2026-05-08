"""
Problem 24: Longest Substring Without Repeating Characters

Given a string `s`, return the LENGTH of the longest substring that
contains no repeated characters.

A substring is a contiguous slice of the original string.

Example:
    longest_unique("abcabcbb") -> 3   ("abc")
    longest_unique("bbbbb")    -> 1   ("b")
    longest_unique("pwwkew")   -> 3   ("wke")
    longest_unique("")         -> 0
    longest_unique("abcdef")   -> 6
    longest_unique(" ")        -> 1

What this tests:
    The classic sliding-window-with-set pattern:
        - Two pointers `left` and `right`, both starting at 0.
        - Expand `right` and add s[right] to the set.
        - If s[right] is already in the set, shrink from the left
          (removing characters from the set) until it's gone.
        - Track the maximum window size as you go.
    O(n) time, O(min(n, alphabet)) space.
"""


def longest_unique(s):
    pass


if __name__ == "__main__":
    assert longest_unique("abcabcbb") == 3
    assert longest_unique("bbbbb") == 1
    assert longest_unique("pwwkew") == 3
    assert longest_unique("") == 0
    assert longest_unique("abcdef") == 6
    assert longest_unique(" ") == 1
    assert longest_unique("dvdf") == 3   # "vdf"

    print("All tests passed.")
