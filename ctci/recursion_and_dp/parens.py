"""
Parens: Implement an algorithm to print all valid (Le., properly opened and closed) combinations
of n pairs of parentheses.
EXAMPLE
Input: 3
Output:
((())), (()()), (())(), ()(()), ()()()
"""

from typing import List


class Solution:
    def generate(self, left, opened):
        if not left and not opened:
            return ['']

        result = []
        if left:
            result.extend(['(' + parenthesis for parenthesis in self.generate(left - 1, opened + 1)])
        if opened:
            result.extend([')' + parenthesis for parenthesis in self.generate(left, opened - 1)])

        return result

    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate(n, 0)


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        self.results = []

        def rec(taken, left, available, prefix):
            if not left:
                self.results.append(prefix)
                return

            if taken < n:
                rec(taken + 1, left, available + 1, prefix + '(')

            if available:
                rec(taken, left - 1, available - 1, prefix + ')')

        rec(0, n, 0, '')
        return self.results
