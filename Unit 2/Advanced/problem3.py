"""
Given:
    integer array 'chests' of length n where all integers in chests are in range [1,n]
    and each integer appears once or twice
Return:
    an array of all integers that appear twice
    representing the treasure chests that have duplicates
"""

from typing import Dict, List
from collections import defaultdict


def find_duplicate_chests(chests: List) -> List:
    chest_map: Dict = defaultdict(int)
    result: List = []

    for item in chests:
        chest_map[item] += 1

    for key, value in chest_map.items():
        if value > 1:
            result.append(key)

    return result


chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
