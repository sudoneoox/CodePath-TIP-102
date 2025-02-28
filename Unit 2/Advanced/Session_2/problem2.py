from typing import List, Set, DefaultDict
from collections import defaultdict


def is_authentic_collection(art_pieces: List) -> bool:
    base_set: DefaultDict = defaultdict(int)
    art_set: DefaultDict = defaultdict(int)
    max: int = 0

    # add occurence of items into art_set
    for item in art_pieces:
        if max < item:
            max = item
        art_set[item] += 1

    # build base set
    for i in range(1, max + 1):
        base_set[i] += 1
    base_set[max] += 1

    # Check if identical
    for k, v in base_set.items():
        if k not in art_set:
            return False
        art_set[k] -= v
        if art_set[k] < 0:
            return False

    return True


collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
