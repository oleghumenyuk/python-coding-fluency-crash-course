"""
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
