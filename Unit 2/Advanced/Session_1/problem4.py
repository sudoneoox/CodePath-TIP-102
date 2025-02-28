"""
Given:
    A 0 indexed string code consisting of only lowercase english letters
Return:
    'is_balanced()' that returns True if its possible to remove one letter so that the frequency
    of all remaining letters is equal and False otherwise
"""

from collections import defaultdict
from typing import DefaultDict, Dict, List


def is_balanced(code: str) -> bool:
    ch_map: DefaultDict = defaultdict(int)
    word_bucket: List = []
    for ch in code:
        ch_map[ch] += 1

    for k, v in ch_map.items():
        if v > 1:
            word_bucket.append(k)
    return len(word_bucket) == 1


code1 = "arghh"
code2 = "haha"

print(is_balanced(code1))
print(is_balanced(code2))
