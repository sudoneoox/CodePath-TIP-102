from typing import Dict, List


def find_min_index_of_repeating(arr: List) -> int | None:
    occurence_counter: Dict = {}
    for i, ele in enumerate(arr):
        if ele in occurence_counter:
            return occurence_counter[ele]
        occurence_counter[ele] = i
