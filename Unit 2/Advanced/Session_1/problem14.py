from typing import Dict, List


def find_travelers(anomolies):
    time_delta: Dict = {}
    result: List[List[int]] = []
    traveler, anomoly = (0, 1)
