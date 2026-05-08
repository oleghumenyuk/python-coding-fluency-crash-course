"""
Problem 35: Word Break

Given a string `s` and a list of dictionary words `word_dict`, return
True if `s` can be segmented into a space-separated sequence of one or
more dictionary words. The same dictionary word may be reused.

Example:
    word_break("leetcode", ["leet", "code"]) -> True
        ("leet" + "code")

    word_break("applepenapple", ["apple", "pen"]) -> True
        ("apple" + "pen" + "apple" — "apple" reused)

    word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) -> False
        (no way to split it cleanly)

    word_break("", ["a", "b"])   -> True   (empty string trivially yes)
    word_break("a", ["a"])       -> True
    word_break("ab", ["a"])      -> False

Assumptions:
    - All words in word_dict are non-empty.

What this tests:
    Recursion with memoization on the START INDEX:
        - At index i, try every word in the dict: does s[i:] start with
          this word? If so, recurse on i + len(word).
        - Memoize results keyed by i so each index is solved once.
    Without memoization, this is exponential. With it, it's polynomial.

    Convert word_dict to a set for O(1) membership / startswith checks.
"""

from functools import lru_cache


def word_break(s, word_dict):
    pass


if __name__ == "__main__":
    assert word_break("leetcode", ["leet", "code"]) is True
    assert word_break("applepenapple", ["apple", "pen"]) is True
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    assert word_break("", ["a", "b"]) is True
    assert word_break("a", ["a"]) is True
    assert word_break("ab", ["a"]) is False
    # Reuse same word multiple times
    assert word_break("aaaaaaa", ["aaa", "aaaa"]) is True

    print("All tests passed.")
