"""
Given:
    map1: str
    map2: str
    len(map1) == len(map2)

Return:
    min_steps: int
    minimum number of steps to make map2 an anagram of map1
"""

from collections import defaultdict
from typing import DefaultDict, Dict


def min_steps_to_match_maps(map1: str, map2: str) -> int:
    min_steps: int = 0
    changes_made: int = 0

    target_chars: DefaultDict = defaultdict(int)
    input_chars: DefaultDict = defaultdict(int)
    for ch in map1:
        target_chars[ch] += 1
    for ch in map2:
        input_chars[ch] += 1

    for k, v in target_chars.items():
        if k not in input_chars:
            min_steps += v
        else:
            min_steps += abs(v - input_chars[k] + changes_made)
            changes_made = abs(v - input_chars[k])
    return min_steps


map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))
