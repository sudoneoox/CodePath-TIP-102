from typing import List, Set


def find_common_artifacts(artifacts1, artifacts2):
    artifacts1_set: Set = set()
    artifacts2_set: Set = set()
    for item in artifacts1:
        artifacts1_set.add(item)
    for item in artifacts2:
        artifacts2_set.add(item)

    return list(artifacts1_set & artifacts2_set)


artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))
