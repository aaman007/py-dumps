"""
BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.
EXAMPLE
Input: Node(2, left=Node(1), right=Node(2))
Output: {2, 1, 3}, {2, 3, 1}
"""


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def waveLists(left, right, prefix, results):
    result = prefix.copy()

    if not left or not right:
        result.extend(right)
        result.extend(left)
        results.append(result)
        return results

    prefix.append(left[0])
    waveLists(left[1:], right, prefix, results)
    prefix.pop()

    prefix.append(right[0])
    waveLists(left, right[1:], prefix, results)
    prefix.pop()

    return results


def BSTSequence(root):
    if not root:
        return [[]]

    result = []
    prefix = [root.data]

    leftSequence = BSTSequence(root.left)
    rightSequence = BSTSequence(root.right)

    for left in leftSequence:
        for right in rightSequence:
            result.extend(waveLists(left, right, prefix, []))

    return result
