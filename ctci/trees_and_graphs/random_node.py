"""
Random Node: You are implementing a binary search tree class from scratch, which, in addition
to insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for get RandomNode, and explain how you would implement the rest of the methods.
"""

import random


class TreeNode:
    def __init__(self, value):
        self._value = value
        self._size = 1
        self.left = None
        self.right = None

    def size(self):
        return self._size

    def value(self):
        return self._value

    def insert_in_order(self, value):
        if value <= self.value():
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.insert_in_order(value)
        else:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.insert_in_order(value)
        self._size += 1

    def get_kth_node(self, k):
        if k < 1:
            return None

        left_size = 0 if not self.left else self.left.size()
        if k <= left_size:
            return self.left.get_kth_node(k)
        elif k == left_size + 1:
            return self
        return self.right.get_kth_node(k - left_size - 1)


class Tree:
    def __init__(self):
        self.root = None

    def size(self):
        return 0 if not self.root else self.root.size()

    def get_random_node(self):
        if not self.root:
            return None

        k = random.randint(1, self.size())
        return self.root.get_kth_node(k)

    def insert_in_order(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self.root.insert_in_order(value)

