"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        lists = []
        queue = deque([(root, 0)])

        while queue:
            node, depth = queue.popleft()

            if depth >= len(lists):
                lists.append([node.val])
            else:
                lists[depth].append(node.val)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return lists


class SolutionWithDFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lists = []

        def rec(cur, depth):
            if not cur:
                return

            if len(lists) <= depth:
                lists.append([])

            lists[depth].append(cur.val)
            rec(cur.left, depth + 1)
            rec(cur.right, depth + 1)

        rec(root, 0)
        return lists


class AlternativeSolution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        lists = []
        current = []

        if root:
            current.append(root)

        while current:
            parents = current
            new_list = []
            current = []

            for parent in parents:
                new_list.append(parent.val)

                if parent.left:
                    current.append(parent.left)
                if parent.right:
                    current.append(parent.right)

            lists.append(new_list)

        return lists
