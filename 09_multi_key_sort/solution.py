"""
Problem 9: Multi-Key Sort

Given a list of (name, age, score) tuples, sort the list by:
    1. score DESCENDING (highest first)
    2. then name ASCENDING (alphabetical) as a tiebreaker

Return the sorted list.

Example:
    people = [
        ("Alice",   30, 85),
        ("Bob",     25, 90),
        ("Charlie", 35, 85),
    ]

    sort_people(people) -> [
        ("Bob",     25, 90),   # highest score
        ("Alice",   30, 85),   # tied score, "Alice" < "Charlie"
        ("Charlie", 35, 85),
    ]

What this tests:
    `sorted(...)` with a `key=` function that returns a tuple, plus the
    "negate the value to flip order" trick for descending numeric sorts:
        key=lambda p: (-p[2], p[0])
"""


def sort_people(people):
    pass


if __name__ == "__main__":
    people = [
        ("Alice", 30, 85),
        ("Bob", 25, 90),
        ("Charlie", 35, 85),
    ]
    assert sort_people(people) == [
        ("Bob", 25, 90),
        ("Alice", 30, 85),
        ("Charlie", 35, 85),
    ]

    # All same score — pure alphabetical
    same_score = [("Charlie", 1, 50), ("Alice", 2, 50), ("Bob", 3, 50)]
    assert sort_people(same_score) == [
        ("Alice", 2, 50),
        ("Bob", 3, 50),
        ("Charlie", 1, 50),
    ]

    assert sort_people([]) == []

    print("All tests passed.")
