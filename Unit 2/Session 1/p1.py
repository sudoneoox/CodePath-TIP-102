from typing import Dict


def lineup(artists, set_times) -> Dict:
    if len(artists) > len(set_times) or len(artists) < len(set_times):
        return {}

    result: Dict = {}
    for idx, artist in enumerate(artists):
        result[artist] = set_times[idx]
    return result


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))
