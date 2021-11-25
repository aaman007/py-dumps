"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
"""


import heapq
from sortedcontainers import SortedList


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = []

    def isEmpty(self):
        return not self.values

    def isFull(self):
        return len(self.values) == self.capacity

    def push(self, val):
        if self.isFull():
            raise Exception('stack is full')
        self.values.append(val)

    def pop(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        return self.values.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        return self.values[-1]


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.leftmost, self.leftmost_set = [], set()
        self.rightmost, self.rightmost_set = [], set()

    def getStack(self, index):
        if index >= len(self.stacks):
            return None
        return self.stacks[index]

    def push(self, val: int) -> None:
        if not self.leftmost:
            self.stacks.append(Stack(self.capacity))
            index = len(self.stacks) - 1
            heapq.heappush(self.leftmost, index)
            self.leftmost_set.add(index)

        top = self.leftmost[0]
        stack = self.getStack(top)
        stack.push(val)

        if -top not in self.rightmost_set:
            heapq.heappush(self.rightmost, -top)
            self.rightmost_set.add(-top)

        if stack.isFull():
            heapq.heappop(self.leftmost)
            self.leftmost_set.discard(top)

    def pop(self) -> int:
        while self.rightmost and self.rightmost[0] not in self.rightmost_set:
            self.rightmost_set.discard(self.rightmost[0])
            heapq.heappop(self.rightmost)

        if not self.rightmost:
            return -1

        top = -1 * self.rightmost[0]
        stack = self.getStack(top)
        value = stack.pop()

        if top not in self.leftmost_set:
            self.leftmost_set.add(top)
            heapq.heappush(self.leftmost, top)

        if stack.isEmpty():
            heapq.heappop(self.rightmost)
            self.rightmost_set.discard(-top)

        return value

    def popAtStack(self, index: int) -> int:
        stack = self.getStack(index)
        if not stack or stack.isEmpty():
            return -1

        value = stack.pop()
        if stack.isEmpty() and -index in self.rightmost_set:
            self.rightmost_set.discard(-index)

        if index not in self.leftmost_set:
            self.leftmost_set.add(index)
            heapq.heappush(self.leftmost, index)

        return value

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


class DinnerPlatesWithSortedList:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.empty = SortedList()
        self.nonempty = SortedList()

    def getStack(self, index):
        if index >= len(self.stacks):
            return None
        return self.stacks[index]

    def push(self, val: int) -> None:
        if not self.empty:
            self.stacks.append(Stack(self.capacity))
            self.empty.add(len(self.stacks) - 1)

        top = self.empty[0]
        stack = self.getStack(top)
        stack.push(val)

        if not self.nonempty.count(-top):
            self.nonempty.add(-top)

        if stack.isFull():
            self.empty.discard(top)

    def pop(self) -> int:
        if not self.nonempty:
            return -1

        top = -1 * self.nonempty[0]
        stack = self.getStack(top)
        value = stack.pop()

        if not self.empty.count(top):
            self.empty.add(top)

        if stack.isEmpty():
            self.nonempty.discard(-top)

        return value

    def popAtStack(self, index: int) -> int:
        stack = self.getStack(index)
        if not stack or stack.isEmpty():
            return -1

        value = stack.pop()
        if stack.isEmpty() and self.nonempty.count(-index):
            self.nonempty.discard(-index)

        if not self.empty.count(index):
            self.empty.add(index)

        return value
