from typing import List


def intersection(nums1: List, nums2: List) -> List:
    set_1 = set(nums1)
    set_2 = set(nums2)
    result: List = list(set_1 & set_2)
    result.sort()
    return result
