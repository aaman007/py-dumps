"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getNewHead(self, head, cur):
        while cur:
            cur = cur.next
            head = head.next
        return head

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB

        while curA and curB:
            curA = curA.next
            curB = curB.next

        headA = self.getNewHead(headA, curA)
        headB = self.getNewHead(headB, curB)

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA
