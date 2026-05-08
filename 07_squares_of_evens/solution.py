"""
Problem 7: Squares of Even Numbers

Given a list of integers, return a list containing the squares of only
the even numbers, in their original order.

Constraint: write the body as a SINGLE list comprehension.

Example:
    squares_of_evens([1, 2, 3, 4, 5]) -> [4, 16]
    squares_of_evens([0, -2, 7, 8])   -> [0, 4, 64]
    squares_of_evens([1, 3, 5])       -> []
    squares_of_evens([])              -> []

What this tests:
    The filter-then-transform shape of a list comprehension:
        [expr for x in iterable if condition]
    Note that 0 is even.
"""


def squares_of_evens(nums):
    pass


if __name__ == "__main__":
    assert squares_of_evens([1, 2, 3, 4, 5]) == [4, 16]
    assert squares_of_evens([0, -2, 7, 8]) == [0, 4, 64]
    assert squares_of_evens([1, 3, 5]) == []
    assert squares_of_evens([]) == []

    print("All tests passed.")
