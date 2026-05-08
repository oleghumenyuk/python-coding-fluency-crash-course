"""
Problem 12: Reverse the Words in a Sentence

Given a string `sentence`, return a new string with the words in reverse
order. Words are separated by single spaces. Treat the input as
well-formed: no leading/trailing spaces, no multiple spaces in a row.

Example:
    reverse_words("hello world foo")     -> "foo world hello"
    reverse_words("the quick brown fox") -> "fox brown quick the"
    reverse_words("hello")               -> "hello"
    reverse_words("")                    -> ""

What this tests:
    The split / reverse-with-slice / join trio:
        " ".join(sentence.split()[::-1])
"""


def reverse_words(sentence):
    pass


if __name__ == "__main__":
    assert reverse_words("hello world foo") == "foo world hello"
    assert reverse_words("the quick brown fox") == "fox brown quick the"
    assert reverse_words("hello") == "hello"
    assert reverse_words("") == ""

    print("All tests passed.")
