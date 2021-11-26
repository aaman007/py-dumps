"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
"""
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkHeights(self, root, depth):
        if not root:
            return 0, True

        left_height, left_result = self.checkHeights(root.left, depth + 1)
        right_height, right_result = self.checkHeights(root.right, depth + 1)

        height = 1 + max(left_height, right_height)
        result = abs(left_height - right_height) <= 1
        result &= left_result
        result &= right_result

        return height, result

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkHeights(root, 0)[1]


class Solution2:
    def checkHeights(self, root, depth):
        if not root:
            return 0

        left = self.checkHeights(root.left, depth + 1)
        right = self.checkHeights(root.right, depth + 1)

        return inf if abs(left - right) > 1 else 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkHeights(root, 0) != inf
