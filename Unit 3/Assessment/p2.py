"""
Given a string s, find first non-repeating character in it and return its index
if it does not exist return -1
"""

from collections import deque


def first_non_repeating_character(s):
    count = {}
    queue = deque()
    for i, ch in enumerate(s):
        if ch not in count:
            count[ch] = 0
            queue.append((ch, i))
        count[ch] += 1

    while queue:
        ch, idx = queue.popleft()
        if count[ch] == 1:
            return idx
    return -1


print(first_non_repeating_character("leetcode"))
