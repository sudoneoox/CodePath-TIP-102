from collections import defaultdict
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_1 = {}
        dict_2 = {}
        result = defaultdict(list)

        for idx, value in enumerate(list1):
            dict_1[value] = idx

        for idx, value in enumerate(list2):
            dict_2[value] = idx

        for k, v in dict_1.items():
            if k in dict_2:
                result[v + dict_2[k]].append(k)

        return result[min(result)]


l1 = ["happy", "sad", "good"]
l2 = ["sad", "happy", "good"]
s = Solution()
s.findRestaurant(l1, l2)
