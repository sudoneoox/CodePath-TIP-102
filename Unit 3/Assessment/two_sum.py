"""
Given 1 indexed already sorted int array
find two distinct numbers that sum up to a given target
"""


def two_sum(numbers, target):
    i, j = 0, len(numbers) - 1
    while i < j:
        while (numbers[i] + numbers[j]) > target:
            j -= 1
        if numbers[i] + numbers[j] == target:
            return [i, j]
        i += 1
        j -= 1

    return None
