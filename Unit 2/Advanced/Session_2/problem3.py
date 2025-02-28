from collections import defaultdict
import collections
from typing import Any, DefaultDict, List


def organize_exhibition(collection: List) -> List[List[str]]:
    collection_counter: DefaultDict = defaultdict(int)
    iterence_bucket: DefaultDict = defaultdict(str)
    result: List[List[str]] = []
    for painting in collection:
        collection_counter[painting] += 1
    for k, v in collection_counter.items():
        iterence_bucket[v] = k

    print(collection_counter.items())
    print(iterence_bucket.items())
    print(len(collection_counter))

    i: int = 0
    while len(collection_counter) > 0 and i < len(collection):
        caught_paintings: List[str] = []
        if collection_counter[collection[i]] > 0:
            caught_paintings.append(collection[i])
            collection_counter[collection[i]] -= 1
        else:
            collection_counter.pop(collection[i])
        i += 1

    return result


collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))
