#!/usr/bin/env python3
"""
setup.py — generates the directory structure and boilerplate solution.py
files for all 35 Python fluency problems.

Usage:
    python setup.py

Drop this file in the root of your repo and run it. It will create 35
directories (e.g. 01_matrix_print/), each containing a solution.py with:
    - a clear problem description with examples
    - function signature(s) stubbed with `pass`
    - assertion-based tests under `if __name__ == "__main__":`

Re-running is safe: directories are created with exist_ok, but solution.py
files WILL be overwritten. Implement, then run `python solution.py` from
inside any problem directory to verify.
"""
from pathlib import Path


PROBLEMS = [
    # =====================================================================
    # 2D MATRIX MECHANICS
    # =====================================================================
    {
        "dir": "01_matrix_print",
        "content": '''"""
Problem 1: Print a Matrix Row by Row, Then Column by Column

Given a 2D list `matrix`, implement two functions that PRINT (not return)
its contents in two different orders.

    print_by_rows(matrix)    -> prints each row on its own line
    print_by_columns(matrix) -> prints each column on its own line

Values within a line should be separated by single spaces.

Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    print_by_rows(matrix) prints:
        1 2 3
        4 5 6

    print_by_columns(matrix) prints:
        1 4
        2 5
        3 6

Assumptions:
    - The matrix is rectangular (every row has the same length).
    - The matrix is non-empty.

What this tests:
    Reflexive use of nested for-loops in both row-major and column-major
    order. There is no clever algorithm here; the point is to write the
    indexing without thinking.
"""


def print_by_rows(matrix):
    pass


def print_by_columns(matrix):
    pass


if __name__ == "__main__":
    # Visual verification — eyeball the output against the expected block.
    m = [[1, 2, 3], [4, 5, 6]]

    print("By rows (expect: '1 2 3' then '4 5 6'):")
    print_by_rows(m)

    print("\\nBy columns (expect: '1 4' then '2 5' then '3 6'):")
    print_by_columns(m)
''',
    },
    {
        "dir": "02_matrix_sums",
        "content": '''"""
Problem 2: Row Sums and Column Sums

Given a 2D list `matrix`, return a tuple (row_sums, col_sums) where:
    - row_sums[i] is the sum of the values in row i
    - col_sums[j] is the sum of the values in column j

Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    row_sums = [6, 15]   (1+2+3, 4+5+6)
    col_sums = [5, 7, 9] (1+4, 2+5, 3+6)

    row_and_col_sums(matrix) -> ([6, 15], [5, 7, 9])

Another example:
    matrix = [[10]]
    row_and_col_sums(matrix) -> ([10], [10])

Assumptions:
    - The matrix is rectangular and non-empty.

What this tests:
    Indexed iteration without losing track of which dimension is which.
    Try to do it in a single pass over the matrix (one set of nested loops,
    not two).
"""


def row_and_col_sums(matrix):
    pass


if __name__ == "__main__":
    rows, cols = row_and_col_sums([[1, 2, 3], [4, 5, 6]])
    assert rows == [6, 15], f"expected [6, 15], got {rows}"
    assert cols == [5, 7, 9], f"expected [5, 7, 9], got {cols}"

    rows, cols = row_and_col_sums([[10]])
    assert rows == [10] and cols == [10]

    rows, cols = row_and_col_sums([[1, -1], [-1, 1]])
    assert rows == [0, 0] and cols == [0, 0]

    print("All tests passed.")
''',
    },
    {
        "dir": "03_matrix_transpose",
        "content": '''"""
Problem 3: Transpose a Matrix (By Hand, Then with zip)

Given a 2D list `matrix`, return its transpose: rows become columns and
columns become rows.

Implement TWO versions:
    transpose_manual(matrix) -> use nested loops only
    transpose_zip(matrix)    -> use zip(*matrix) in one line

Both should return a list of lists (not a list of tuples), and both should
return identical output.

Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    transpose -> [
        [1, 4],
        [2, 5],
        [3, 6],
    ]

Another example:
    matrix = [[1]]
    transpose -> [[1]]

Assumptions:
    - The matrix is rectangular and non-empty.

What this tests:
    The by-hand mechanic of building a new matrix with swapped dimensions,
    plus recognition of the idiomatic `[list(col) for col in zip(*matrix)]`
    shortcut. zip returns tuples, so the list() wrap matters.
"""


def transpose_manual(matrix):
    pass


def transpose_zip(matrix):
    pass


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert transpose_manual(m) == expected
    assert transpose_zip(m) == expected

    assert transpose_manual([[1]]) == [[1]]
    assert transpose_zip([[1]]) == [[1]]

    square = [[1, 2], [3, 4]]
    assert transpose_manual(square) == [[1, 3], [2, 4]]
    assert transpose_zip(square) == [[1, 3], [2, 4]]

    print("All tests passed.")
''',
    },
    {
        "dir": "04_matrix_rotate",
        "content": '''"""
Problem 4: Rotate an n x n Matrix 90 Degrees Clockwise, In Place

Given an n x n matrix, rotate it 90 degrees clockwise WITHOUT allocating
a new matrix. Mutate the input in place and return None (or return the
mutated matrix — your call, but don't build a fresh 2D list).

Example:
    Input:
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    After rotate_in_place(matrix), the matrix becomes:
        [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]

Another example (2x2):
    Input:  [[1, 2], [3, 4]]
    After:  [[3, 1], [4, 2]]

Assumptions:
    - The matrix is square (n x n) and non-empty.

What this tests:
    The classic transpose-then-reverse-each-row trick, OR the four-cell
    cycle swap. Either approach must mutate in place — no `return [...]`
    with a freshly built matrix.
"""


def rotate_in_place(matrix):
    pass


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_in_place(m)
    assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]], f"got {m}"

    m = [[1, 2], [3, 4]]
    rotate_in_place(m)
    assert m == [[3, 1], [4, 2]], f"got {m}"

    m = [[1]]
    rotate_in_place(m)
    assert m == [[1]]

    print("All tests passed.")
''',
    },
    {
        "dir": "05_matrix_spiral",
        "content": '''"""
Problem 5: Spiral Order Traversal

Given an m x n matrix, return a list of its elements in spiral order:
right across the top row, down the right column, left across the bottom
row, up the left column, then spiral inward.

Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    spiral_order(matrix) -> [1, 2, 3, 6, 9, 8, 7, 4, 5]

Another example (rectangular):
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    spiral_order(matrix) -> [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

Edge case:
    spiral_order([[1]]) -> [1]
    spiral_order([[1, 2, 3]]) -> [1, 2, 3]   (single row)
    spiral_order([[1], [2], [3]]) -> [1, 2, 3]   (single column)

Assumptions:
    - The matrix is rectangular and non-empty.
    - m and n may differ.

What this tests:
    The four-boundary-pointers pattern (top, bottom, left, right) and
    careful loop termination. This pattern reappears in many grid problems.
"""


def spiral_order(matrix):
    pass


if __name__ == "__main__":
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert spiral_order([[1]]) == [1]
    assert spiral_order([[1, 2, 3]]) == [1, 2, 3]
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]

    print("All tests passed.")
''',
    },
    {
        "dir": "06_matrix_flood_fill",
        "content": '''"""
Problem 6: Flood Fill

Given a 2D grid `image`, a starting cell `(sr, sc)`, and a `new_color`,
replace the color of the starting cell and ALL 4-connected cells of the
same original color with `new_color`. Return the modified image.

"4-connected" means up, down, left, right (no diagonals).

Example:
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]
    sr, sc = 1, 1
    new_color = 2

    flood_fill(image, sr, sc, new_color) -> [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]

    The bottom-right 1 is NOT changed because it isn't connected to (1,1)
    through cells of value 1.

Edge case — same color (no-op):
    image = [[0, 0], [0, 0]]
    flood_fill(image, 0, 0, 0) -> [[0, 0], [0, 0]]
    Be careful: if you don't guard against this, you'll infinite-loop.

Assumptions:
    - The grid is rectangular and non-empty.
    - (sr, sc) is a valid cell.

What this tests:
    Recursive (or stack-based) traversal with a directions array
    `[(-1, 0), (1, 0), (0, -1), (0, 1)]`, plus the "guard against
    same color" edge case.
"""


def flood_fill(image, sr, sc, new_color):
    pass


if __name__ == "__main__":
    img = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    assert flood_fill(img, 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    # Same-color no-op
    img2 = [[0, 0], [0, 0]]
    assert flood_fill(img2, 0, 0, 0) == [[0, 0], [0, 0]]

    # Single cell
    assert flood_fill([[5]], 0, 0, 9) == [[9]]

    # Disconnected region — only the connected component changes
    img3 = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    assert flood_fill(img3, 0, 0, 7) == [[7, 0, 1], [0, 0, 0], [1, 0, 1]]

    print("All tests passed.")
''',
    },

    # =====================================================================
    # LIST & COMPREHENSION FLUENCY
    # =====================================================================
    {
        "dir": "07_squares_of_evens",
        "content": '''"""
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
''',
    },
    {
        "dir": "08_flatten_2d",
        "content": '''"""
Problem 8: Flatten a 2D List

Given a list of lists, return a single flat list containing every element
in row-major order (left-to-right, top-to-bottom).

Constraint: write the body as a SINGLE nested list comprehension.

Example:
    flatten([[1, 2], [3, 4], [5]]) -> [1, 2, 3, 4, 5]
    flatten([[1, 2, 3]])           -> [1, 2, 3]
    flatten([])                    -> []
    flatten([[]])                  -> []

What this tests:
    Reading order of nested comprehensions. The "outer" loop comes first:
        [x for row in matrix for x in row]
    The order matches what you'd write as nested for-loops, which is
    backwards from how many people first read it.
"""


def flatten(matrix):
    pass


if __name__ == "__main__":
    assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert flatten([[1, 2, 3]]) == [1, 2, 3]
    assert flatten([]) == []
    assert flatten([[]]) == []
    assert flatten([[1], [2], [3]]) == [1, 2, 3]

    print("All tests passed.")
''',
    },
    {
        "dir": "09_multi_key_sort",
        "content": '''"""
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
''',
    },
    {
        "dir": "10_enumerate_threshold",
        "content": '''"""
Problem 10: Enumerate Above Threshold

Given a list of numbers and a threshold, return a list of (index, value)
tuples for every value STRICTLY greater than the threshold, preserving
original order.

Constraint: use `enumerate`, not `range(len(nums))`.

Example:
    nums = [10, 5, 20, 3, 15]
    threshold = 8

    above_threshold(nums, 8) -> [(0, 10), (2, 20), (4, 15)]

More examples:
    above_threshold([1, 2, 3], 5) -> []
    above_threshold([], 0)        -> []
    above_threshold([5, 5, 5], 5) -> []   (strictly greater, not >=)

What this tests:
    Reflexive use of `enumerate(nums)` instead of indexing manually.
"""


def above_threshold(nums, threshold):
    pass


if __name__ == "__main__":
    assert above_threshold([10, 5, 20, 3, 15], 8) == [(0, 10), (2, 20), (4, 15)]
    assert above_threshold([1, 2, 3], 5) == []
    assert above_threshold([], 0) == []
    assert above_threshold([5, 5, 5], 5) == []
    assert above_threshold([-1, 0, 1], -1) == [(1, 0), (2, 1)]

    print("All tests passed.")
''',
    },
    {
        "dir": "11_zip_even_sums",
        "content": '''"""
Problem 11: Zip Two Lists, Keep Pairs with Even Sum

Given two lists `a` and `b` of equal length, return a list of (a[i], b[i])
tuples where a[i] + b[i] is even.

Constraint: use `zip` and a list comprehension.

Example:
    a = [1, 2, 3, 4]
    b = [1, 3, 5, 8]
    sums: 2, 5, 8, 12 — even sums at indices 0, 2, 3
    even_sum_pairs(a, b) -> [(1, 1), (3, 5), (4, 8)]

More examples:
    even_sum_pairs([2, 4], [2, 4]) -> [(2, 2), (4, 4)]
    even_sum_pairs([1, 2], [2, 1]) -> []   (both sums are 3, odd)
    even_sum_pairs([], [])         -> []

Assumptions:
    - len(a) == len(b)

What this tests:
    `zip` combined with a filter inside a comprehension:
        [(x, y) for x, y in zip(a, b) if (x + y) % 2 == 0]
"""


def even_sum_pairs(a, b):
    pass


if __name__ == "__main__":
    assert even_sum_pairs([1, 2, 3, 4], [1, 3, 5, 8]) == [(1, 1), (3, 5), (4, 8)]
    assert even_sum_pairs([2, 4], [2, 4]) == [(2, 2), (4, 4)]
    assert even_sum_pairs([1, 2], [2, 1]) == []
    assert even_sum_pairs([], []) == []
    assert even_sum_pairs([0], [0]) == [(0, 0)]

    print("All tests passed.")
''',
    },

    # =====================================================================
    # STRING MANIPULATION
    # =====================================================================
    {
        "dir": "12_reverse_words",
        "content": '''"""
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
''',
    },
    {
        "dir": "13_palindrome_check",
        "content": '''"""
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
''',
    },
    {
        "dir": "14_char_frequency",
        "content": '''"""
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
''',
    },
    {
        "dir": "15_caesar_cipher",
        "content": '''"""
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
''',
    },
    {
        "dir": "16_most_common_word",
        "content": '''"""
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
''',
    },

    # =====================================================================
    # DICT / COUNTER / DEFAULTDICT
    # =====================================================================
    {
        "dir": "17_group_anagrams",
        "content": '''"""
Problem 17: Group Anagrams

Given a list of strings, group strings that are anagrams of each other.
Return a list of groups (each group is a list of the original strings).
The order of groups and the order within groups do NOT matter — the test
will normalize before comparing.

Two strings are anagrams if they contain the same characters with the
same counts (just rearranged).

Example:
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
       (in any order, e.g. [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        is also fine)

More examples:
    group_anagrams([""]) -> [[""]]
    group_anagrams(["a"]) -> [["a"]]
    group_anagrams([])    -> []

What this tests:
    `defaultdict(list)` keyed by a canonical form of each string. Two
    common keys:
        - tuple(sorted(s))     — simple, O(k log k) per string
        - a 26-letter count tuple — O(k) per string but more code
    Either is fine here.
"""


def group_anagrams(strs):
    pass


def _normalize(groups):
    """Helper: sort within each group, then sort the groups themselves."""
    return sorted([sorted(g) for g in groups])


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert _normalize(result) == _normalize(expected), f"got {result}"

    assert _normalize(group_anagrams([""])) == _normalize([[""]])
    assert _normalize(group_anagrams(["a"])) == _normalize([["a"]])
    assert group_anagrams([]) == []

    print("All tests passed.")
''',
    },
    {
        "dir": "18_top_k_frequent",
        "content": '''"""
Problem 18: Top K Frequent Elements

Given a list of integers `nums` and an integer `k`, return the `k` most
frequent elements. The order of the returned list does not matter — the
test will compare as a set.

Example:
    top_k_frequent([1, 1, 1, 2, 2, 3], 2) -> [1, 2]   (or [2, 1])
    top_k_frequent([1], 1)                -> [1]
    top_k_frequent([4, 4, 4, 5, 5, 6], 1) -> [4]
    top_k_frequent([1, 2, 3, 4], 4)       -> [1, 2, 3, 4]   (any order)

Assumptions:
    - 1 <= k <= number of distinct values in nums
    - nums is non-empty

What this tests:
    `Counter(nums).most_common(k)` is the one-liner. Try this first, then
    rewrite using a heap (`heapq.nlargest`) as a follow-up to practice
    the heap version of the pattern.
"""

from collections import Counter


def top_k_frequent(nums, k):
    pass


if __name__ == "__main__":
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert top_k_frequent([1], 1) == [1]
    assert set(top_k_frequent([4, 4, 4, 5, 5, 6], 1)) == {4}
    assert set(top_k_frequent([1, 2, 3, 4], 4)) == {1, 2, 3, 4}

    print("All tests passed.")
''',
    },
    {
        "dir": "19_invert_dict",
        "content": '''"""
Problem 19: Invert a Dict (Collecting Duplicate Values)

Given a dict whose values may collide, return an inverted dict where
each original value becomes a key, mapped to a list of the original
keys that had that value. The lists should be sorted (so the test is
deterministic).

Example:
    invert({"a": 1, "b": 2, "c": 1})
    -> {1: ["a", "c"], 2: ["b"]}

    invert({"a": "x", "b": "x", "c": "y"})
    -> {"x": ["a", "b"], "y": ["c"]}

    invert({})  -> {}
    invert({"only": 42}) -> {42: ["only"]}

What this tests:
    `defaultdict(list).append(...)` keyed by the original value, then
    sorting each list before returning. Reflexive grouping pattern.
"""

from collections import defaultdict


def invert(d):
    pass


if __name__ == "__main__":
    assert invert({"a": 1, "b": 2, "c": 1}) == {1: ["a", "c"], 2: ["b"]}
    assert invert({"a": "x", "b": "x", "c": "y"}) == {"x": ["a", "b"], "y": ["c"]}
    assert invert({}) == {}
    assert invert({"only": 42}) == {42: ["only"]}

    print("All tests passed.")
''',
    },
    {
        "dir": "20_two_sum",
        "content": '''"""
Problem 20: Two Sum

Given a list of integers `nums` and an integer `target`, return the
indices of the two numbers that add up to `target`. Return them as a
list `[i, j]` with i < j. You may assume exactly one solution exists,
and you may not use the same element twice.

Example:
    two_sum([2, 7, 11, 15], 9) -> [0, 1]   (because 2 + 7 == 9)
    two_sum([3, 2, 4], 6)      -> [1, 2]   (because 2 + 4 == 6)
    two_sum([3, 3], 6)         -> [0, 1]   (same value, different indices)

What this tests:
    The single-pass dict lookup pattern:
        seen = {}
        for i, x in enumerate(nums):
            if (target - x) in seen:
                return [seen[target - x], i]
            seen[x] = i
    O(n) time, O(n) space — much better than the O(n^2) double loop.
"""


def two_sum(nums, target):
    pass


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

    print("All tests passed.")
''',
    },
    {
        "dir": "21_first_unique_char",
        "content": '''"""
Problem 21: First Non-Repeating Character

Given a string `s`, return the FIRST character that appears exactly once.
If every character repeats (or the string is empty), return None.

Example:
    first_unique("leetcode")     -> "l"
    first_unique("loveleetcode") -> "v"
    first_unique("aabb")         -> None
    first_unique("")             -> None
    first_unique("z")            -> "z"

What this tests:
    A two-pass pattern:
        1. Count characters with a dict (or Counter).
        2. Iterate the string in order and return the first char with
           count == 1.
    The key insight: order matters, so you have to revisit the original
    string — you can't read it off the counts dict directly.
"""


def first_unique(s):
    pass


if __name__ == "__main__":
    assert first_unique("leetcode") == "l"
    assert first_unique("loveleetcode") == "v"
    assert first_unique("aabb") is None
    assert first_unique("") is None
    assert first_unique("z") == "z"
    assert first_unique("aabbcc d") == " "  # space appears exactly once

    print("All tests passed.")
''',
    },

    # =====================================================================
    # SETS
    # =====================================================================
    {
        "dir": "22_find_duplicates",
        "content": '''"""
Problem 22: Find Duplicates

Given a list of values, return the SET of values that appear more than
once.

Example:
    find_duplicates([1, 2, 3, 2, 4, 3, 5]) -> {2, 3}
    find_duplicates([1, 2, 3])             -> set()
    find_duplicates([])                    -> set()
    find_duplicates([1, 1, 1, 1])          -> {1}
    find_duplicates(["a", "b", "a", "c"])  -> {"a"}

What this tests:
    The two-set pattern — one set tracks "seen at least once", another
    tracks "seen more than once":
        seen = set()
        dupes = set()
        for x in values:
            if x in seen:
                dupes.add(x)
            else:
                seen.add(x)
        return dupes
    O(n) time, O(n) space.
"""


def find_duplicates(values):
    pass


if __name__ == "__main__":
    assert find_duplicates([1, 2, 3, 2, 4, 3, 5]) == {2, 3}
    assert find_duplicates([1, 2, 3]) == set()
    assert find_duplicates([]) == set()
    assert find_duplicates([1, 1, 1, 1]) == {1}
    assert find_duplicates(["a", "b", "a", "c"]) == {"a"}

    print("All tests passed.")
''',
    },
    {
        "dir": "23_ordered_intersection",
        "content": '''"""
Problem 23: Ordered Intersection of Two Lists

Given two lists `a` and `b`, return a list of values that appear in
BOTH lists. Preserve the order of first occurrence as it appears in `a`,
and deduplicate the result.

Example:
    ordered_intersection([1, 2, 2, 3, 4], [2, 4, 5]) -> [2, 4]
    ordered_intersection([3, 1, 2], [2, 1, 3])       -> [3, 1, 2]
        (order from `a`)
    ordered_intersection([1, 2], [3, 4])             -> []
    ordered_intersection([], [1, 2])                 -> []
    ordered_intersection([1, 1, 1], [1])             -> [1]

What this tests:
    Combining a set (for fast O(1) membership in `b`) with a list and a
    "seen" set (for order preservation and dedup):
        b_set = set(b)
        seen = set()
        out = []
        for x in a:
            if x in b_set and x not in seen:
                out.append(x)
                seen.add(x)
        return out
"""


def ordered_intersection(a, b):
    pass


if __name__ == "__main__":
    assert ordered_intersection([1, 2, 2, 3, 4], [2, 4, 5]) == [2, 4]
    assert ordered_intersection([3, 1, 2], [2, 1, 3]) == [3, 1, 2]
    assert ordered_intersection([1, 2], [3, 4]) == []
    assert ordered_intersection([], [1, 2]) == []
    assert ordered_intersection([1, 1, 1], [1]) == [1]

    print("All tests passed.")
''',
    },
    {
        "dir": "24_longest_unique_substring",
        "content": '''"""
Problem 24: Longest Substring Without Repeating Characters

Given a string `s`, return the LENGTH of the longest substring that
contains no repeated characters.

A substring is a contiguous slice of the original string.

Example:
    longest_unique("abcabcbb") -> 3   ("abc")
    longest_unique("bbbbb")    -> 1   ("b")
    longest_unique("pwwkew")   -> 3   ("wke")
    longest_unique("")         -> 0
    longest_unique("abcdef")   -> 6
    longest_unique(" ")        -> 1

What this tests:
    The classic sliding-window-with-set pattern:
        - Two pointers `left` and `right`, both starting at 0.
        - Expand `right` and add s[right] to the set.
        - If s[right] is already in the set, shrink from the left
          (removing characters from the set) until it's gone.
        - Track the maximum window size as you go.
    O(n) time, O(min(n, alphabet)) space.
"""


def longest_unique(s):
    pass


if __name__ == "__main__":
    assert longest_unique("abcabcbb") == 3
    assert longest_unique("bbbbb") == 1
    assert longest_unique("pwwkew") == 3
    assert longest_unique("") == 0
    assert longest_unique("abcdef") == 6
    assert longest_unique(" ") == 1
    assert longest_unique("dvdf") == 3   # "vdf"

    print("All tests passed.")
''',
    },

    # =====================================================================
    # STACK & QUEUE
    # =====================================================================
    {
        "dir": "25_valid_parentheses",
        "content": '''"""
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
''',
    },
    {
        "dir": "26_daily_temperatures",
        "content": '''"""
Problem 26: Daily Temperatures (Next Greater Element)

Given a list `temps` of daily temperatures, return a list `answer` where
`answer[i]` is the number of days you have to wait after day `i` to get
a warmer temperature. If no future day is warmer, set answer[i] = 0.

Example:
    daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
    -> [1, 1, 4, 2, 1, 1, 0, 0]

    Walking through:
        day 0 (73): next warmer is day 1 (74) -> 1 day later
        day 1 (74): next warmer is day 2 (75) -> 1 day later
        day 2 (75): next warmer is day 6 (76) -> 4 days later
        day 3 (71): next warmer is day 5 (72) -> 2 days later
        day 4 (69): next warmer is day 5 (72) -> 1 day later
        day 5 (72): next warmer is day 6 (76) -> 1 day later
        day 6 (76): no warmer day -> 0
        day 7 (73): no warmer day -> 0

More examples:
    daily_temperatures([30, 40, 50, 60]) -> [1, 1, 1, 0]
    daily_temperatures([60, 50, 40, 30]) -> [0, 0, 0, 0]
    daily_temperatures([50])             -> [0]

What this tests:
    The monotonic stack pattern. Critically, the stack stores INDICES,
    not values:
        stack = []   # indices of days awaiting a warmer day
        for i, t in enumerate(temps):
            while stack and temps[stack[-1]] < t:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
    O(n) time — each index is pushed and popped at most once.
"""


def daily_temperatures(temps):
    pass


if __name__ == "__main__":
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([60, 50, 40, 30]) == [0, 0, 0, 0]
    assert daily_temperatures([50]) == [0]
    assert daily_temperatures([]) == []

    print("All tests passed.")
''',
    },
    {
        "dir": "27_shortest_path_bfs",
        "content": '''"""
Problem 27: Shortest Path in a Grid (BFS)

Given a 2D grid where:
    0 = passable cell
    1 = blocked cell

Return the LENGTH of the shortest path (counted as the number of cells
visited, including both start and end) from `(0, 0)` to
`(rows-1, cols-1)`, moving only 4-directionally (up/down/left/right).

If `(0, 0)` or the destination is blocked, or no path exists, return -1.

Example:
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    shortest_path(grid) -> 5
        (path: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2), 5 cells)

More examples:
    shortest_path([[0]]) -> 1
    shortest_path([[1]]) -> -1   (start blocked)
    shortest_path([[0, 1], [1, 0]]) -> -1   (no path; diagonals not allowed)
    shortest_path([[0, 0], [0, 0]]) -> 3

Assumptions:
    - The grid is rectangular and non-empty.

What this tests:
    BFS with `collections.deque`:
        - Push the start with its distance.
        - On each pop, check if you've reached the destination.
        - Otherwise, push every unvisited 4-neighbor with distance + 1.
    Always use `popleft()` (O(1)) — never `pop(0)` (O(n) on a list).
    A `visited` set prevents re-enqueuing.
"""

from collections import deque


def shortest_path(grid):
    pass


if __name__ == "__main__":
    assert shortest_path([[0, 0, 0], [1, 1, 0], [0, 0, 0]]) == 5
    assert shortest_path([[0]]) == 1
    assert shortest_path([[1]]) == -1
    assert shortest_path([[0, 1], [1, 0]]) == -1
    assert shortest_path([[0, 0], [0, 0]]) == 3
    # Destination blocked
    assert shortest_path([[0, 0], [0, 1]]) == -1

    print("All tests passed.")
''',
    },

    # =====================================================================
    # HEAP / TOP-K
    # =====================================================================
    {
        "dir": "28_k_closest_points",
        "content": '''"""
Problem 28: K Closest Points to the Origin

Given a list of 2D points (each as `[x, y]`) and an integer `k`, return
the `k` points closest to the origin `(0, 0)` by Euclidean distance.
The order of returned points does not matter — the test compares as a
set of tuples.

Note: you can compare using SQUARED distance (x*x + y*y) since the sqrt
is monotonic. Skipping it is faster and avoids floating point.

Example:
    k_closest([[1, 3], [-2, 2]], 1) -> [[-2, 2]]
        (distances: 1+9=10, 4+4=8 — second is closer)

    k_closest([[3, 3], [5, -1], [-2, 4]], 2) -> [[3, 3], [-2, 4]]
        (distances: 18, 26, 20 — closest two are [3,3] and [-2,4])

    k_closest([[1, 0]], 1) -> [[1, 0]]

Assumptions:
    - 1 <= k <= len(points)

What this tests:
    `heapq` mechanics. Two solid approaches:
        1. heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)
        2. Push all points into a min-heap as (dist, point), then pop k.
    Try the one-liner first, then the explicit-heap version.
"""

import heapq


def k_closest(points, k):
    pass


def _normalize(points):
    return sorted(tuple(p) for p in points)


if __name__ == "__main__":
    assert _normalize(k_closest([[1, 3], [-2, 2]], 1)) == _normalize([[-2, 2]])
    assert _normalize(k_closest([[3, 3], [5, -1], [-2, 4]], 2)) == _normalize([[3, 3], [-2, 4]])
    assert _normalize(k_closest([[1, 0]], 1)) == _normalize([[1, 0]])
    assert _normalize(k_closest([[0, 1], [1, 0], [2, 2]], 2)) == _normalize([[0, 1], [1, 0]])

    print("All tests passed.")
''',
    },
    {
        "dir": "29_merge_k_sorted",
        "content": '''"""
Problem 29: Merge K Sorted Lists

Given a list of lists, where each inner list is already sorted in
ascending order, merge them into a single sorted list.

Example:
    merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]])
    -> [1, 1, 2, 3, 4, 4, 5, 6]

    merge_k_sorted([])              -> []
    merge_k_sorted([[]])            -> []
    merge_k_sorted([[1, 2, 3]])     -> [1, 2, 3]
    merge_k_sorted([[], [1], []])   -> [1]

What this tests:
    The min-heap merge pattern. Push one element from each list as a
    tuple `(value, list_idx, elem_idx)`. Pop the smallest, append it to
    the result, and push the next element from that same list (if any).

    Why include `list_idx` in the tuple? If two values are equal, Python
    breaks the tie by comparing the next tuple element. Including the
    index makes that comparison safe even if the elements aren't
    naturally orderable.

    O(N log k) where N is total elements and k is the number of lists.
"""

import heapq


def merge_k_sorted(lists):
    pass


if __name__ == "__main__":
    assert merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_k_sorted([]) == []
    assert merge_k_sorted([[]]) == []
    assert merge_k_sorted([[1, 2, 3]]) == [1, 2, 3]
    assert merge_k_sorted([[], [1], []]) == [1]
    assert merge_k_sorted([[1, 1, 1], [1, 1], [1]]) == [1, 1, 1, 1, 1, 1]

    print("All tests passed.")
''',
    },

    # =====================================================================
    # TUPLES & UNPACKING
    # =====================================================================
    {
        "dir": "30_reverse_in_place",
        "content": '''"""
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
''',
    },
    {
        "dir": "31_min_max_mean",
        "content": '''"""
Problem 31: Min, Max, Mean in One Pass

Given a non-empty list of numbers, return a tuple `(min_val, max_val, mean)`
computed in a SINGLE pass over the list. Do not use the built-in `min`,
`max`, or `sum` on the list.

The mean should be a float.

Example:
    min_max_mean([1, 2, 3, 4, 5]) -> (1, 5, 3.0)
    min_max_mean([42])            -> (42, 42, 42.0)
    min_max_mean([-1, -5, -3])    -> (-5, -1, -3.0)
    min_max_mean([2, 2, 2, 2])    -> (2, 2, 2.0)

Assumptions:
    - The list is non-empty.

What this tests:
    Multi-return tuples and tracking multiple accumulators in one loop:
        lo = hi = nums[0]
        total = 0
        for x in nums:
            if x < lo: lo = x
            if x > hi: hi = x
            total += x
        return (lo, hi, total / len(nums))
"""


def min_max_mean(nums):
    pass


if __name__ == "__main__":
    assert min_max_mean([1, 2, 3, 4, 5]) == (1, 5, 3.0)
    assert min_max_mean([42]) == (42, 42, 42.0)
    assert min_max_mean([-1, -5, -3]) == (-5, -1, -3.0)
    assert min_max_mean([2, 2, 2, 2]) == (2, 2, 2.0)

    print("All tests passed.")
''',
    },

    # =====================================================================
    # ITERTOOLS, RECURSION, MEMOIZATION
    # =====================================================================
    {
        "dir": "32_subsets",
        "content": '''"""
Problem 32: Generate All Subsets (Power Set)

Given a list of distinct integers `nums`, return all possible subsets
(the power set). Each subset is itself a list. The order of subsets,
and the order of elements within a subset, do NOT matter — the test
will normalize before comparing.

Example:
    subsets([1, 2, 3]) -> [
        [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
    ]
    (any ordering of those 8 subsets is fine)

    subsets([])    -> [[]]
    subsets([7])   -> [[], [7]]
    subsets([1, 2]) -> [[], [1], [2], [1, 2]]

For a list of n elements, there are 2**n subsets.

What this tests:
    The classic include/exclude recursion pattern:
        def helper(i, current):
            if i == len(nums):
                result.append(list(current))
                return
            # exclude nums[i]
            helper(i + 1, current)
            # include nums[i]
            current.append(nums[i])
            helper(i + 1, current)
            current.pop()
    Iterative version with `for x in nums: result += [s + [x] for s in result]`
    is also fair game.
"""


def subsets(nums):
    pass


def _normalize(subs):
    return sorted([sorted(s) for s in subs])


if __name__ == "__main__":
    expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert _normalize(subsets([1, 2, 3])) == _normalize(expected)
    assert _normalize(subsets([])) == _normalize([[]])
    assert _normalize(subsets([7])) == _normalize([[], [7]])
    assert _normalize(subsets([1, 2])) == _normalize([[], [1], [2], [1, 2]])

    # Size check
    assert len(subsets([1, 2, 3, 4])) == 16

    print("All tests passed.")
''',
    },
    {
        "dir": "33_permutations",
        "content": '''"""
Problem 33: Generate All Permutations

Given a list of distinct integers `nums`, return all possible
permutations. Order of returned permutations does NOT matter — the test
compares as a set of tuples.

Implement TWO versions:
    permutations_manual(nums) -> by hand, recursively
    permutations_lib(nums)    -> using itertools.permutations

Both should return a list of lists with identical content (order may vary).

Example:
    permutations_manual([1, 2, 3]) -> [
        [1, 2, 3], [1, 3, 2],
        [2, 1, 3], [2, 3, 1],
        [3, 1, 2], [3, 2, 1],
    ]   (in any order)

    permutations_manual([])  -> [[]]
    permutations_manual([5]) -> [[5]]
    permutations_manual([1, 2]) -> [[1, 2], [2, 1]]

For a list of n elements, there are n! permutations.

What this tests:
    Recursive enumeration where you "pick one, recurse on the rest":
        def helper(remaining, current):
            if not remaining:
                result.append(list(current))
                return
            for i, x in enumerate(remaining):
                helper(remaining[:i] + remaining[i+1:], current + [x])
    Then the one-liner with `itertools.permutations` for muscle memory.
"""

from itertools import permutations as _perm


def permutations_manual(nums):
    pass


def permutations_lib(nums):
    pass


def _normalize(perms):
    return sorted(tuple(p) for p in perms)


if __name__ == "__main__":
    expected = [
        [1, 2, 3], [1, 3, 2],
        [2, 1, 3], [2, 3, 1],
        [3, 1, 2], [3, 2, 1],
    ]
    assert _normalize(permutations_manual([1, 2, 3])) == _normalize(expected)
    assert _normalize(permutations_lib([1, 2, 3])) == _normalize(expected)

    assert _normalize(permutations_manual([])) == _normalize([[]])
    assert _normalize(permutations_lib([])) == _normalize([[]])

    assert _normalize(permutations_manual([5])) == _normalize([[5]])
    assert _normalize(permutations_manual([1, 2])) == _normalize([[1, 2], [2, 1]])

    # Size check (4! = 24)
    assert len(permutations_manual([1, 2, 3, 4])) == 24

    print("All tests passed.")
''',
    },
    {
        "dir": "34_memoized_fib",
        "content": '''"""
Problem 34: Memoized Fibonacci

Compute the n-th Fibonacci number, where:
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n - 1) + fib(n - 2)  for n >= 2

Implement TWO versions:
    fib_manual_memo(n) -> recursion + manual memo dict
    fib_lru_cache(n)   -> recursion + @functools.lru_cache decorator

Both should return identical results.

Example:
    fib_manual_memo(0)  -> 0
    fib_manual_memo(1)  -> 1
    fib_manual_memo(10) -> 55
    fib_manual_memo(20) -> 6765
    fib_manual_memo(50) -> 12586269025

Assumptions:
    - n >= 0

What this tests:
    The manual memo pattern (`memo = {}`, check before computing, store
    after computing) and the `@lru_cache(maxsize=None)` decorator
    shortcut. Without memoization, naive recursion is O(2**n); with it,
    it's O(n).
"""

from functools import lru_cache


def fib_manual_memo(n):
    pass


def fib_lru_cache(n):
    pass


if __name__ == "__main__":
    for impl in (fib_manual_memo, fib_lru_cache):
        assert impl(0) == 0
        assert impl(1) == 1
        assert impl(2) == 1
        assert impl(10) == 55
        assert impl(20) == 6765
        assert impl(50) == 12586269025

    print("All tests passed.")
''',
    },
    {
        "dir": "35_word_break",
        "content": '''"""
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
''',
    },
]


def main():
    root = Path(__file__).parent
    created = 0
    for p in PROBLEMS:
        d = root / p["dir"]
        d.mkdir(exist_ok=True)
        (d / "solution.py").write_text(p["content"])
        created += 1
    print(f"Created {created} problem directories under {root}")
    print("Each contains a solution.py with the problem spec, function stubs, and tests.")
    print("Implement the function(s), then run `python solution.py` from the directory to verify.")


if __name__ == "__main__":
    main()
