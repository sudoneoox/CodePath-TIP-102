import enum
from typing import Dict, List


def declutter(souvenirs, threshold):
    filter_item: Dict = {}
    filter_idx: Dict = {}
    result: List = []
    for idx, souvenir in enumerate(souvenirs):
        if souvenir not in filter_item:
            filter_item[souvenir] = 0
            filter_idx[souvenir] = idx
        filter_item[souvenir] += 1

    for k, v in filter_item.items():
        if v < threshold:
            for i in range(0, v):
                result.append(souvenirs[filter_idx[k]])

    return result


souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3
print(declutter(souvenirs1, threshold1))
souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold2 = 2
print(declutter(souvenirs2, threshold2))
