from typing import Dict, List


def contains_duplicate(nums: List) -> bool:
    iterance_ctr: Dict = {}
    for num in nums:
        if num in iterance_ctr:
            return True
        iterance_ctr[num] = 0
    return False
