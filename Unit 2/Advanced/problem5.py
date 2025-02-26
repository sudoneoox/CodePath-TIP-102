"""
Given:
    an array of integers 'gold_amounts' representing the amt of gold
    at each location and an integer 'target'
Return:
    the indices of the two locations whose gold amounts add up to the target
    You can return the answer in any order
    Assume that each input has exactly one solution
"""

from typing import Dict, List


def find_treasure_indices(gold_amounts: List, target: int) -> List:
    gold_amounts.sort()
    start: int = 0
    end: int = len(gold_amounts) - 1

    target_vals: List[int] = []
    while start < end and start != end:
        # you cant have negative gold
        # so if the end is bigger than the target keep decreasing pointer
        while gold_amounts[end] > target:
            end -= 1
        if gold_amounts[start] + gold_amounts[end] == target:
            target_vals.append(start)
            target_vals.append(end)
            break
        start += 1
        end -= 1

    return target_vals


gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))
print(find_treasure_indices(gold_amounts2, target2))
print(find_treasure_indices(gold_amounts3, target3))
