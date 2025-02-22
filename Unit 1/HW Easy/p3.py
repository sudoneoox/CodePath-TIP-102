"""
3. Flowerbed
"""

#
# Complete the 'can_place_flowers' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY flowerbed
#  2. INTEGER n
#

from typing import List


def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    total: int = 0
    print(f"{flowerbed} {n}")
    for i in range(0, len(flowerbed) - 1):
        print(f"flowerbed: {flowerbed}")

        if i == 0:
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                total += 1
            continue
        elif i == len(flowerbed) - 1:
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = int(not flowerbed[i])
                total += 1
            break

        elif (
            flowerbed[i] == 0
            and flowerbed[i - 1] == 0
            and flowerbed[i] == 0
            and flowerbed[i + 1] == 0
        ):
            flowerbed[i] = int(not flowerbed[i])
            total += 1
            i += 2

    return total >= n


print(can_place_flowers([1, 0, 0, 0, 1], 1))
