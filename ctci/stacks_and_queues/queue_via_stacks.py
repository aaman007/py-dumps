"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""


class Queue:

    def __init__(self):
        self.stackOldest = []
        self.stackNewest = []

    def size(self):
        return len(self.stackOldest) + len(self.stackNewest)

    def push(self, val):
        self.stackNewest.append(val)

    def shiftStacks(self):
        if not self.stackOldest:
            while self.stackNewest:
                self.stackOldest.append(self.stackNewest.pop())

    def pop(self):
        self.shiftStacks()
        return self.stackOldest.pop()

    def peek(self):
        self.shiftStacks()
        return self.stackOldest[-1]

    def empty(self) -> bool:
        return not self.size()
