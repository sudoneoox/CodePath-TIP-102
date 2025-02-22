import enum
from typing import List


def harvest(vegetable_patch: List[List[str]]) -> int:
    """
    returns ready to harvest vegetables
    ready to harvest vegetables are marked with 'c'
    """

    harvest: int = 0
    for _, sub_array in enumerate(vegetable_patch):
        for __, patch in enumerate(vegetable_patch[_]):
            if patch == "c":
                harvest += 1
    return harvest


vegetable_patch = [["x", "c", "x"], ["x", "x", "x"], ["x", "c", "c"], ["c", "c", "c"]]
print(harvest(vegetable_patch))
