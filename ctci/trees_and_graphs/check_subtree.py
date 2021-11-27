"""
Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine if T2 is a subtree of Tl .
A tree T2 is a subtree of T1 if there exists a node n in Tl such that the subtree of n is identical to T2 .
That is, if you cut off the tree at node n, the two trees would be identical.
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def matchTree(self, root1, root2):
        if not root1 or not root2:
            return root1 == root2
        elif root1.val != root2.val:
            return False

        return self.matchTree(root1.left, root2.left) and self.matchTree(root1.right, root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.matchTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
