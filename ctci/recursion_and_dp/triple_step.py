"""
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
"""

from functools import cache


@cache
def count_ways(n):
    if n <= 0:
        return not n
    return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)


# LEETCODE

class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return not n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution2:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2
        for i in range(n - 2):
            temp = a
            a = b
            b = temp + b

        return b
