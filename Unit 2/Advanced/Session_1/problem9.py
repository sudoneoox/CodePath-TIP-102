from typing import DefaultDict, Dict
from collections import defaultdict


def analyze_library(library_catalog, actual_distribution):
    result: Dict = {}
    for key, value in actual_distribution.items():
        result[key] = value - library_catalog.get(key, 0)

    return result


library_catalog = {"Room A": 150, "Room B": 200, "Room C": 250, "Room D": 300}

actual_distribution = {"Room A": 150, "Room B": 190, "Room C": 260, "Room D": 300}


print(analyze_library(library_catalog, actual_distribution))
