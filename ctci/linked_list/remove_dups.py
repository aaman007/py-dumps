"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""


class ListNode:
    def __init__(self, val=None, _next=None):
        self.val = val
        self.next = _next


def remove_duplicates(head):
    """ TC: O(N) || SC: O(N) """

    seen = set()
    cur, prev = head, None
    while cur:
        if cur.val in seen:
            prev.next = cur.next
        else:
            seen.add(cur.val)
            prev = cur
        cur = cur.next
    return head


def remove_duplicate_followup(head):
    """ TC: O(N^2) || SC: O(1) """

    cur = head
    while cur:
        runner = cur
        while runner.next:
            if runner.next.val == cur.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur = cur.next
    return head
