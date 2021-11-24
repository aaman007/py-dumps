"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -) 5 -) 8 -) 5 -) 113 -) 2 -) 1 [partition = 5]
Output: 3 -) 1 -) 2 -) 113 -) 5 -) 8
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head_a = ListNode()
        head_b = ListNode()

        cur_a, cur_b = head_a, head_b
        while head:
            nxt = head.next

            if head.val < x:
                cur_a.next = head
                cur_a = cur_a.next
            else:
                cur_b.next = head
                cur_b = cur_b.next

            head.next = None
            head = nxt

        cur_a.next = head_b.next
        return head_a.next
