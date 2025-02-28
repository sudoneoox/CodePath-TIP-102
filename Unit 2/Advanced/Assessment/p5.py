from typing import Dict, List


def two_sum(nums: List[int], target: int) -> List[int]:
    result: List = []
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                result = [i, j]
                break

    return result
