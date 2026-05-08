"""
Problem 14: Character Frequency (Raw Dict, No Counter)

Given a string `s`, return a dict mapping each character to the number
of times it appears.

Constraint: use a plain `dict`. Do NOT use `collections.Counter`.

Example:
    char_frequency("hello") -> {"h": 1, "e": 1, "l": 2, "o": 1}
    char_frequency("aaa")   -> {"a": 3}
    char_frequency("")      -> {}
    char_frequency("ab ab") -> {"a": 2, "b": 2, " ": 1}

What this tests:
    The `d[k] = d.get(k, 0) + 1` pattern. (You can also use
    `if k not in d: d[k] = 0; d[k] += 1`, but `.get` is the cleaner one
    to have on autopilot.)
"""


def char_frequency(s):
    pass


if __name__ == "__main__":
    assert char_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert char_frequency("aaa") == {"a": 3}
    assert char_frequency("") == {}
    assert char_frequency("ab ab") == {"a": 2, "b": 2, " ": 1}

    print("All tests passed.")
