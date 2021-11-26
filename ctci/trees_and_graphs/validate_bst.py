"""
Validate 8ST: Implement a function to check if a binary tree is a binary search tree.
"""
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkValidity(self, root, minimum, maximum):
        if not root:
            return True
        elif root.val < minimum or root.val > maximum:
            return False

        ret = self.checkValidity(root.left, minimum, root.val - 1)
        ret &= self.checkValidity(root.right, root.val + 1, maximum)

        return ret

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkValidity(root, -inf, inf)


class SolutionLeftCanBeEqual:
    def checkValidity(self, root, minimum, maximum):
        if not root:
            return True
        elif root.val < minimum or root.val > maximum:
            return False

        ret = self.checkValidity(root.left, minimum, root.val)
        ret &= self.checkValidity(root.right, root.val + 1, maximum)

        return ret

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkValidity(root, -inf, inf)
