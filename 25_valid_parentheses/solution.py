"""
Problem 25: Valid Parentheses

Given a string containing only the characters `()`, `[]`, and `{}`,
return True if the brackets are correctly opened and closed:
    - Every opening bracket has a matching closing bracket of the same type.
    - Brackets are closed in the correct nested order.

Example:
    is_valid("()")         -> True
    is_valid("()[]{}")     -> True
    is_valid("(])")        -> False
    is_valid("([{}])")     -> True
    is_valid("(")          -> False   (unclosed)
    is_valid(")")          -> False   (unmatched close)
    is_valid("")           -> True
    is_valid("([)]")       -> False   (wrong nesting)

What this tests:
    The stack pattern:
        - Push every opener.
        - On a closer, pop and verify the popped opener matches.
        - At the end, the stack must be empty.
    The close->open mapping dict is the standard companion:
        pairs = {")": "(", "]": "[", "}": "{"}
"""


def is_valid(s):
    pass


if __name__ == "__main__":
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(])") is False
    assert is_valid("([{}])") is True
    assert is_valid("(") is False
    assert is_valid(")") is False
    assert is_valid("") is True
    assert is_valid("([)]") is False

    print("All tests passed.")
