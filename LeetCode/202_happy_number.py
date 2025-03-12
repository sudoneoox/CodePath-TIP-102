from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_next(n)
        return n == 1

    def get_next(self, n: int) -> int:
        return sum(int(dig) ** 2 for dig in str(n))


s = Solution()
print(s.isHappy(19))
