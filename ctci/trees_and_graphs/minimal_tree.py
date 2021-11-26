"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildBST(self, nums, l, r):
        if l > r:
            return None

        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = self.buildBST(nums, l, mid - 1)
        root.right = self.buildBST(nums, mid + 1, r)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildBST(nums, 0, len(nums) - 1)


class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
