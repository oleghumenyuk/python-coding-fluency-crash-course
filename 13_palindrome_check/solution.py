"""
Problem 13: Palindrome Check (Ignoring Case and Non-Alphanumerics)

Given a string `s`, return True if it reads the same forwards and
backwards after:
    1. Lowercasing all letters
    2. Removing every character that is NOT alphanumeric

Example:
    is_palindrome("A man, a plan, a canal: Panama") -> True
        (cleaned form: "amanaplanacanalpanama")
    is_palindrome("race a car") -> False
        (cleaned form: "raceacar" — "raceacar" reversed is "racaecar")
    is_palindrome("") -> True   (empty string is trivially a palindrome)
    is_palindrome(".,!?")  -> True   (cleans to "")
    is_palindrome("Was it a car or a cat I saw?") -> True

What this tests:
    `str.isalnum()` for filtering, `str.lower()` for normalization, and
    the `s == s[::-1]` palindrome idiom on the cleaned string.
"""


def is_palindrome(s):
    pass


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome("") is True
    assert is_palindrome(".,!?") is True
    assert is_palindrome("Was it a car or a cat I saw?") is True
    assert is_palindrome("hello") is False

    print("All tests passed.")
