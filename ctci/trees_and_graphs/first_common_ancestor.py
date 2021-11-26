"""
First Common Ancestor: Design an algorithm and wri te code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def rec(cur):
            if not cur:
                return False

            l, r = rec(cur.left), rec(cur.right)
            now = cur == p or cur == q
            if l + r + now >= 2:
                nonlocal ans
                ans = cur

            return now or l or r

        rec(root)
        return ans
