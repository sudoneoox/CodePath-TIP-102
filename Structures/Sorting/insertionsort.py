from typing import List
from random import randint


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j -= 1
    return arr


unsorted_array: List[int] = []
for i in range(1, 20):
    unsorted_array.append(randint(0, 100))

print(f"Unsorted Array: {unsorted_array}")

insertionSort(unsorted_array)
print(f"Sorted Array: {unsorted_array}")
