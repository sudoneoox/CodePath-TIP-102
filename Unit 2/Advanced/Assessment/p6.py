from typing import Dict


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    mapping_dict_1: Dict = {}
    mapping_dict_2: Dict = {}
    iterance_ctr_reversed_1: Dict = {}
    iterance_ctr_reversed_2: Dict = {}

    for i in range(0, len(s)):
        if s[i] not in mapping_dict_1:
            mapping_dict_1[s[i]] = 0
        if t[i] not in mapping_dict_2:
            mapping_dict_2[t[i]] = 0
        mapping_dict_1[s[i]] += 1
        mapping_dict_2[t[i]] += 1

    for k, v in mapping_dict_1.items():
        iterance_ctr_reversed_1[v] = k
    for k, v in mapping_dict_2.items():
        iterance_ctr_reversed_2[v] = k

    if len(iterance_ctr_reversed_1) != len(iterance_ctr_reversed_2):
        return False

    return True
