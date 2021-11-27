"""
Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative) . Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
"""

from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        result = 0

        def rec(node, total):
            if not node:
                return

            total += node.val
            nonlocal result
            result += freq[total - targetSum]

            freq[total] += 1
            rec(node.left, total)
            rec(node.right, total)

            freq[total] -= 1

        rec(root, 0)
        return result


class Solution2:
    def countPathSum(self, root, targetSum, runningSum, pathCount):
        if not root:
            return 0

        runningSum += root.val
        totalPaths = pathCount[runningSum - targetSum] + (runningSum == targetSum)

        pathCount[runningSum] += 1
        totalPaths += self.countPathSum(root.left, targetSum, runningSum, pathCount)
        totalPaths += self.countPathSum(root.right, targetSum, runningSum, pathCount)
        pathCount[runningSum] -= 1

        return totalPaths

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.countPathSum(root, targetSum, 0, defaultdict(int))
