"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
"""


class Solution:
    def findMin(self, node):
        if not node:
            return None
        while node.left:
            node = node.left
        return node

    def findSuccessor(self, node):
        if node.right:
            return self.findMin(node.right)
        else:
            parent = node.parent
            while parent and parent.left != node:
                node = parent
                parent = parent.parent
            return parent
