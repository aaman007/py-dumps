"""
Palindrome: Implement a function to check if a linked list is a palindrome.
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head):
        prev = None

        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast:
            slow = slow.next

        slow = self.reverse(slow)

        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next

        return True


class SolutionWithStack:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        if fast:
            slow = slow.next

        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True


class SolutionRecursive:
    def getLength(self, head):
        sz = 0
        while head:
            sz += 1
            head = head.next
        return sz

    def isPalindromeRecurse(self, head, length):
        if length in [0, 1]:
            return head if not length else head.next, True

        node, result = self.isPalindromeRecurse(head.next, length - 2)
        if not result or not node:
            return node, result
        return node.next, node.val == head.val

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        sz = self.getLength(head)
        return self.isPalindromeRecurse(head, sz)[1]
