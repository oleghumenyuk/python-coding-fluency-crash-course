"""
Problem 30: Reverse a List In Place (Two Pointers + Tuple Swap)

Given a list `a`, reverse it IN PLACE — no allocating a new list, no
using `a.reverse()`, no using `a[::-1]`. Use two pointers and the
tuple-swap idiom.

Example:
    a = [1, 2, 3, 4, 5]
    reverse_in_place(a)
    # a is now [5, 4, 3, 2, 1]

    a = [1, 2]
    reverse_in_place(a)
    # a is now [2, 1]

    a = []
    reverse_in_place(a)
    # a is still []

What this tests:
    The swap-without-temp idiom:
        a[i], a[j] = a[j], a[i]
    plus a two-pointer loop with `i < j`.
"""


def reverse_in_place(a):
    pass


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    reverse_in_place(a)
    assert a == [5, 4, 3, 2, 1]

    a = [1, 2]
    reverse_in_place(a)
    assert a == [2, 1]

    a = []
    reverse_in_place(a)
    assert a == []

    a = [42]
    reverse_in_place(a)
    assert a == [42]

    a = ["a", "b", "c"]
    reverse_in_place(a)
    assert a == ["c", "b", "a"]

    print("All tests passed.")
