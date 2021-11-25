"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def is_empty(self):
        return not self.stack

    def push(self, value):
        if self.is_empty() or self.min() >= value:
            self.min_stack.append(value)
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')

        if self.min() == self.peek():
            self.min_stack.pop()
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')

        return self.stack[-1]

    def min(self):
        if self.is_empty():
            raise Exception('Stack is empty')

        return self.min_stack[-1]

