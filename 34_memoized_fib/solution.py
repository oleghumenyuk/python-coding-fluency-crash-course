"""
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
