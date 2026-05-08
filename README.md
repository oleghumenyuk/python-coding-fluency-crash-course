# Python Fluency Practice

A collection of 35 problems designed to build muscle memory for core Python idioms and standard-library patterns. The goal is **mechanical fluency**, not algorithmic difficulty — each problem targets a specific building block I want to be able to write without thinking.

## Ground Rules

- **Standard library only.** No third-party packages (`numpy`, `pandas`, etc.). `collections`, `heapq`, `itertools`, `functools`, `math` are all fair game.
- **One file per problem.** Each file contains a docstring spec and assertion-based tests at the bottom.
- **Write it twice when it helps.** Problems that have an idiomatic shortcut (e.g., `zip(*m)` for transpose) are solved by hand first, then with the shortcut.

## Topics

1. [2D Matrix Mechanics](#1-2d-matrix-mechanics-6-problems)
2. [List & Comprehension Fluency](#2-list--comprehension-fluency-5-problems)
3. [String Manipulation](#3-string-manipulation-5-problems)
4. [Dict / Counter / defaultdict](#4-dict--counter--defaultdict-5-problems)
5. [Sets](#5-sets-3-problems)
6. [Stack & Queue](#6-stack--queue-3-problems)
7. [Heap / Top-K](#7-heap--top-k-2-problems)
8. [Tuples & Unpacking](#8-tuples--unpacking-2-problems)
9. [Itertools, Recursion, Memoization](#9-itertools-recursion-memoization-4-problems)

---

## 1. 2D Matrix Mechanics (6 problems)

Tests row/column/diagonal traversal, in-place mutation, and the standard "directions array" pattern for grid problems.

| # | Problem | What it tests |
|---|---------|---------------|
| 01 | Print rows then columns | Given a 2D list, print it row by row, then column by column. Forces the `for r in range(rows): for c in range(cols)` pattern in both orders. |
| 02 | Row and column sums | Return two lists: sum of each row and sum of each column. Tests indexed iteration without losing track of which dimension is which. |
| 03 | Transpose | First by hand using nested loops, then in one line with `zip(*m)`. Tests the by-hand mechanic and recognition of the idiomatic shortcut. |
| 04 | Rotate 90° clockwise, in place | Rotate an `n × n` matrix without allocating a new one. Tests the transpose-then-reverse-rows trick and in-place index swapping. |
| 05 | Spiral order traversal | Return matrix elements in spiral order. Tests the four-boundary-pointers pattern that shows up constantly in grid problems. |
| 06 | Flood fill | Starting from `(r, c)`, replace all 4-connected cells of the same value with a new value. Tests recursion or stack-based traversal with a directions array `[(-1,0),(1,0),(0,-1),(0,1)]`. |

## 2. List & Comprehension Fluency (5 problems)

Tests reflexive use of comprehensions, `enumerate`, `zip`, and key-based sorting.

| # | Problem | What it tests |
|---|---------|---------------|
| 07 | Squares of evens | Return `[x*x for x in nums if x % 2 == 0]` in a single comprehension. Tests filter-then-transform shape. |
| 08 | Flatten 2D list | Flatten a list of lists with a nested comprehension `[x for row in m for x in row]`. Tests reading order of nested comprehensions (the gotcha that trips everyone). |
| 09 | Multi-key sort | Sort `(name, age, score)` tuples by score descending, then name ascending. Tests `key=lambda` with negation and tuple keys. |
| 10 | Enumerate with threshold | Return `(index, value)` pairs where value > threshold. Tests reflexive use of `enumerate` instead of `range(len(...))`. |
| 11 | Zip with even sums | Zip two lists, return the pairs whose sum is even. Tests `zip` + filter in one comprehension. |

## 3. String Manipulation (5 problems)

Tests slicing, `split`/`join`, character arithmetic with `ord`/`chr`, and counting patterns.

| # | Problem | What it tests |
|---|---------|---------------|
| 12 | Reverse words | Reverse the order of words in a sentence (`"hello world"` → `"world hello"`). Tests `split` + `[::-1]` + `join`. |
| 13 | Palindrome check | Ignoring case and non-alphanumerics, is the string a palindrome? Tests filtering with `str.isalnum`, lowercasing, and the `s == s[::-1]` idiom. |
| 14 | Character frequency (raw dict) | Count character occurrences using a plain dict — no `Counter`. Tests the `d[k] = d.get(k, 0) + 1` pattern. |
| 15 | Caesar cipher | Shift each letter by `k`, preserving case, leaving non-letters alone. Tests `ord`/`chr` arithmetic and modular wrap-around. |
| 16 | Most common word | In a paragraph, return the word that appears most often (case-insensitive, punctuation stripped). Tests tokenizing, normalizing, and counting. |

## 4. Dict / Counter / defaultdict (5 problems)

Tests reflexive reach for the right `collections` tool and the most common dict-shaped patterns.

| # | Problem | What it tests |
|---|---------|---------------|
| 17 | Group anagrams | Group strings that are anagrams of each other. Tests `defaultdict(list)` keyed by `tuple(sorted(s))` or a 26-letter count signature. |
| 18 | Top K frequent | Return the K most frequent elements in a list. Tests `Counter.most_common(k)` and the manual heap version as a follow-up. |
| 19 | Invert a dict | Invert a dict where values may collide; collect duplicates into lists. Tests `defaultdict(list)` and the inverted-mapping pattern. |
| 20 | Two-sum with a dict | Return indices of two numbers that sum to a target. Tests the `seen = {}` lookup pattern in a single pass. |
| 21 | First non-repeating char | Return the first character that appears exactly once. Tests counting, then re-iterating the original string in order. |

## 5. Sets (3 problems)

Tests using sets for dedup, fast membership, and the sliding-window pattern.

| # | Problem | What it tests |
|---|---------|---------------|
| 22 | Find duplicates | Return all values that appear more than once in a list. Tests `seen` + `dupes` two-set pattern. |
| 23 | Ordered intersection | Return the intersection of two lists, preserving the order of the first. Tests set-for-membership combined with list-for-order. |
| 24 | Longest substring without repeats | Return the length of the longest substring with all unique characters. Tests the sliding-window-with-set pattern. |

## 6. Stack & Queue (3 problems)

Tests list-as-stack mechanics, `deque` for BFS, and recognizing when each is the right tool.

| # | Problem | What it tests |
|---|---------|---------------|
| 25 | Valid parentheses | Validate a string of `()`, `[]`, `{}`. Tests stack push/pop and the close-to-open mapping dict. |
| 26 | Daily temperatures | For each day, how many days until a warmer one? Tests the monotonic-stack pattern (storing indices, not values). |
| 27 | Shortest path in grid (BFS) | Shortest path from `(0,0)` to `(rows-1, cols-1)` in a 0/1 grid. Tests `deque` with `popleft`, a `visited` set, and the directions-array pattern. |

## 7. Heap / Top-K (2 problems)

Tests `heapq` mechanics, including the negate-for-max-heap trick.

| # | Problem | What it tests |
|---|---------|---------------|
| 28 | K closest points to origin | Return the K points closest to `(0, 0)`. Tests `heapq.nsmallest` with a key, plus the manual heap version using `heappush`/`heappop`. |
| 29 | Merge K sorted lists | Merge K already-sorted lists into one sorted list. Tests pushing tuples `(value, list_idx, elem_idx)` onto a min-heap. |

## 8. Tuples & Unpacking (2 problems)

Tests the swap idiom, multi-return, and unpacking inside loops.

| # | Problem | What it tests |
|---|---------|---------------|
| 30 | Reverse list in place | Reverse using two pointers and tuple-swap `a[i], a[j] = a[j], a[i]`. Tests the swap idiom without a temp variable. |
| 31 | Min, max, mean in one pass | Return `(min_val, max_val, mean)` from a list in a single pass. Tests multi-return tuples and tracking multiple accumulators. |

## 9. Itertools, Recursion, Memoization (4 problems)

Tests recursive enumeration patterns and memoization mechanics.

| # | Problem | What it tests |
|---|---------|---------------|
| 32 | All subsets | Generate the power set of a list, recursively. Tests the include/exclude branching pattern. |
| 33 | All permutations | Generate all permutations, first by hand recursively, then with `itertools.permutations`. Tests the swap-based recursion and recognition of the stdlib shortcut. |
| 34 | Memoized Fibonacci | Compute `fib(n)` with a manual memo dict, then with `@lru_cache`. Tests the memo pattern and the decorator shortcut. |
| 35 | Word break | Given a string and a dict of words, can the string be segmented into dict words? Tests recursion with memoization on the start index. |

---

## Repo Structure

```
.
├── README.md
├── 01_matrix_print/
│   └── solution.py
├── 02_matrix_sums/
│   └── solution.py
...
```

Each `solution.py` contains:
1. A docstring with the problem spec
2. The function signature
3. An `assert`-based test block under `if __name__ == "__main__":`
