"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""

from collections import Counter


class Solution:
    @staticmethod
    def check_permutation_slow(s1, s2):
        """ TC: O(nlogn + mlogn)  |||  SC: O(1) """
        return sorted(s1) == sorted(s2)

    @staticmethod
    def check_permutation_fast(s1, s2):
        """ TC: O(n+m)  |||   SC: O(n) """

        freq = Counter(s1)
        for ch in s2:
            if not freq.get(ch):
                return False
            freq[ch] -= 1
        return True

