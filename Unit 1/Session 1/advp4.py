from typing import List


def non_decreasing(nums: List[int]) -> bool:
    """
    checks if nums could become non-decreasing by
    modifying at most one element

    We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i
    """
    if len(nums) == 0:
        return True

    threshold: int = -1  # start at -1 since were double checking the starting element
    lowest_num: int = nums[0]
    for _, value in enumerate(nums):
        if lowest_num >= value:
            lowest_num = value
            threshold += 1
            if threshold > 1:
                return False

    return threshold == 1


nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))
