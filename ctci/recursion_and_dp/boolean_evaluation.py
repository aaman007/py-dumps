"""
Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
(AND), | (OR), and ^ (XOR), and a desired boolean result value result, implement a function to
count the number of ways of parenthesizing the expression such that it evaluates to result . The
expression should be fully parenthesized (e.g., (0) ^ (1) but not extraneously ( e.g., (((0)) ^ (1)) ).
EXAMPLE
countEval("1^0|0|1", false) -> 2
countEval("0&0&0&1^1|0", true) - > 10
"""

from functools import lru_cache


class Solution:
    def __init__(self):
        self.A = None

    def to_boolean(self, ch):
        return True if ch == 'T' else False

    def cnttrue(self, A):
        self.A = A
        return self.count(0, len(A) - 1)

    @lru_cache(None)
    def count(self, l, r, target=True):
        if l > r:
            return 0
        elif l == r:
            return self.to_boolean(self.A[l]) == target

        MOD = 10 ** 3 + 3
        ans = 0
        for index in range(l + 1, r, 2):
            left_true = self.count(l, index - 1, True)
            left_false = self.count(l, index - 1, False)
            right_true = self.count(index + 1, r, True)
            right_false = self.count(index + 1, r, False)

            total = (left_true + left_false) * (right_true + right_false)

            total_true = 0
            if self.A[index] == '&':
                total_true += left_true * right_true
            elif self.A[index] == '^':
                total_true += (left_true * right_false) + (left_false * right_true)
            else:
                total_true += (left_true * right_false) + (left_false * right_true)
                total_true += left_true * right_true

            ans += total_true if target else total - total_true
            ans %= MOD

        return ans
