"""
Given:
    dict 'treasure_map' where k is location_name and v are integers representing the
    number of treasures buried at those locations

Return total_treasures():
    that returns the total number of treasures buried on the island
"""

from typing import Dict


def total_treasures(treasure_map: Dict) -> int:
    sum: int = 0
    for k, v in treasure_map.items():
        sum += v
    return sum


treasure_map1 = {"Cove": 3, "Beach": 7, "Forest": 5}

treasure_map2 = {"Shipwreck": 10, "Cave": 20, "Lagoon": 15, "Island Peak": 5}

print(total_treasures(treasure_map1))
print(total_treasures(treasure_map2))
