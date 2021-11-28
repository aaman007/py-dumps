"""
Stack of Boxes: You have a stack of n boxes, with widths W(i) heights h(i) and depths d(i)• The boxes
cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
larger than the box above it in width, height and depth. Implement a method to compute the
height of the tallest possible stack. The height of a stack is the sum of the heights of each box.
"""

from functools import cache
from typing import List


class Solution:

    def canHold(self, envelopeA, envelopeB):
        # This would be extended to 3 dimensions
        if not envelopeA:
            return True
        return envelopeA[0] < envelopeB[0] and envelopeA[1] < envelopeB[1]

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        @cache
        def findMax(previous_index):
            previous = None if previous_index == -1 else envelopes[previous_index]
            ret = 0

            for next_index in range(previous_index + 1, len(envelopes)):
                _next = envelopes[next_index]

                if self.canHold(previous, _next):
                    ret = max(ret, 1 + findMax(next_index))

            return ret

        envelopes.sort()
        return findMax(-1)


