"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""


class Solution:
    @staticmethod
    def is_unique(text):
        """ TC: O(n)   ||   SC: O(1) """

        mask = 0
        for ch in text:
            position = ord(ch) - ord('a')
            if mask & (1 << position):
                return False
            mask |= (1 << position)

        return True
