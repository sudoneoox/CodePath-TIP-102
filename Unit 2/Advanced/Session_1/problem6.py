"""
Given:
    group_sizes: List[int]
    group_sizes[i] -> size of the group that pirate i should be in
Return:
    groups: List[List[int]] -> s.t each pirate is in a group
"""

from collections import defaultdict
from typing import DefaultDict, Dict, List


def organize_pirate_crew(group_sizes: List[int]) -> List[List[int]]:
    # each bucket should hold max group_sizes[i]
    result: List[List[int]] = []
    size_groups: DefaultDict = defaultdict(lambda: defaultdict(list))

    for idx, size in enumerate(group_sizes):
        bucket_num: int = 0
        while len(size_groups[size][bucket_num]) >= size:
            bucket_num += 1

        # add pirate to this group
        size_groups[size][bucket_num].append(idx)

    for size in size_groups:
        for bucket_num in size_groups[size]:
            result.append(size_groups[size][bucket_num])

    return result


group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
# [[5], [0, 1, 2], [3, 4, 6]]
print(organize_pirate_crew(group_sizes2))
# [[1], [0, 5], [2, 3, 4]]
