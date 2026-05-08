"""
Problem 15: Caesar Cipher

Given a string `s` and an integer shift `k`, return a new string where
every alphabetic character is shifted by `k` positions in the alphabet,
wrapping around as needed. Preserve case. Leave non-letters unchanged.

Example:
    caesar("Hello, World!", 3) -> "Khoor, Zruog!"
    caesar("abc", 1)           -> "bcd"
    caesar("xyz", 3)           -> "abc"   (wraps around)
    caesar("ABC", -1)          -> "ZAB"   (negative shift wraps too)
    caesar("Hello", 0)         -> "Hello"
    caesar("Hello", 26)        -> "Hello" (full cycle)
    caesar("123 abc!", 2)      -> "123 cde!"

What this tests:
    `ord` / `chr` arithmetic with the lowercase 'a' (97) and uppercase
    'A' (65) base offsets, and modular wrap-around with `% 26`. The
    pattern:
        shifted = (ord(c) - base + k) % 26 + base
"""


def caesar(s, k):
    pass


if __name__ == "__main__":
    assert caesar("Hello, World!", 3) == "Khoor, Zruog!"
    assert caesar("abc", 1) == "bcd"
    assert caesar("xyz", 3) == "abc"
    assert caesar("ABC", -1) == "ZAB"
    assert caesar("Hello", 0) == "Hello"
    assert caesar("Hello", 26) == "Hello"
    assert caesar("123 abc!", 2) == "123 cde!"

    print("All tests passed.")
