from typing import List


def find_missing_clues(clues: List[int], lower: int, upper: int) -> List[List[int]]:
    """
    Return missing intervals (missing clues) with a lower and upper bound
    """
    i: int = 0
    list: List[List[int]] = []

    while i < len(clues):
        if clues[i] - 1 == lower or clues[i] == lower:
            lower = clues[i]
            i += 1
            continue
        else:
            list.append([lower + 1, clues[i] - 1])
            lower = clues[i]
        i += 1

    if clues[i - 1] < upper:
        list.append([clues[i - 1] + 1, upper])
    return list


clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))
