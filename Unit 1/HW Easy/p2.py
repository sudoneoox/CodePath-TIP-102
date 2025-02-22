"""
2. Needle in the Haystack
"""

#
# Complete the 'find_needle' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING haystack
#  2. STRING needle
#
from typing import List


def find_needle(haystack: str, needle: str) -> int:
    if needle not in haystack or needle > haystack:
        return -1
    return haystack.find(needle)
