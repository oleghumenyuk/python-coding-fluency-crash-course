"""
Problem 16: Most Common Word in a Paragraph

Given a string `paragraph`, return the most frequently occurring word.
Treat words case-insensitively and strip punctuation. If multiple words
are tied for the highest count, return any one of them (the tests will
accept any valid answer).

A "word" is a maximal run of alphabetic characters. Punctuation such as
`.,!?;:` should be treated as a word boundary.

Example:
    most_common_word("The sun is bright. The sky is blue.") -> "the"
        (counts: the=2, sun=1, is=2, bright=1, sky=1, blue=1
         "the" and "is" are tied; either is acceptable.)

    most_common_word("Hello, hello, HELLO!") -> "hello"

    most_common_word("a b c a b a") -> "a"

You may use `collections.Counter` here.

What this tests:
    Tokenizing a paragraph (splitting on non-letters), normalizing case,
    counting, and pulling out the max. The trickiest piece is splitting
    on punctuation cleanly — `re` is the obvious tool, but you can also
    do it by replacing punctuation with spaces and splitting.
"""


def most_common_word(paragraph):
    pass


if __name__ == "__main__":
    # "the" and "is" are tied at 2 each; either is acceptable.
    result = most_common_word("The sun is bright. The sky is blue.")
    assert result in {"the", "is"}, f"got {result}"

    assert most_common_word("Hello, hello, HELLO!") == "hello"
    assert most_common_word("a b c a b a") == "a"
    assert most_common_word("Wow!") == "wow"

    print("All tests passed.")
