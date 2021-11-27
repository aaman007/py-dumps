"""
Power Set: Write a method to return all subsets of a set.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int], cur: int = 0) -> List[List[int]]:
        if cur == len(nums):
            return [[]]
        _subsets = self.subsets(nums, cur+1)
        return [x + [nums[cur]] for x in _subsets] + _subsets


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []

        for mask in range(0, (1 << n)):
            results.append([])

            for bit in range(n):
                if mask & (1 << bit):
                    results[-1].append(nums[bit])

        return results
