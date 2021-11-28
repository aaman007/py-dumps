"""
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.
"""

from functools import cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def rec(cur, left):
            if cur == len(coins) or not left:
                return not left

            ret = 0
            quantity = 0
            while coins[cur] * quantity <= left:
                ret += rec(cur + 1, left - coins[cur] * quantity)
                quantity += 1

            return ret

        return rec(0, amount)

