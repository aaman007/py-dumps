"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list

1 -> 2 -> 3 -> 4 -> 5
3

Step 1: Go to ListNode(4) with a pointer
Step 2: Get another pointer for head and move them forward simultaneously
Step 3: Kth node is the second pointer (Basically with the first iteration we figured out how many nodes to skip)
"""


class ListNode:
    def __init__(self, val=None, _next=None):
        self.val = val
        self.next = _next


def kth_last(head, k):
    p1, p2 = head, head

    for _ in range(k):
        p1 = p1.next

    while p1:
        p1 = p1.next
        p2 = p2.next

    return p2


