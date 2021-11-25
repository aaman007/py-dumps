"""
Three in One: Describe how you could use a single array to implement three stacks.
"""


class FullStackError(Exception):
    pass


class EmptyStackError(Exception):
    pass


class MultiStack:
    def __init__(self, number_of_stacks=3, stack_capacity=1):
        self.number_of_stacks = number_of_stacks
        self.stack_capacity = stack_capacity
        self.stack = [0] * (self.number_of_stacks * stack_capacity)
        self.pointers = [0] * self.number_of_stacks

    # Properties
    def is_full(self, stack_num=None):
        if stack_num is not None:
            return self.pointers[stack_num] == self.stack_capacity
        return all(self.is_full(stack_num) for stack_num in range(self.number_of_stacks))

    def is_empty(self, stack_num=None):
        if stack_num is not None:
            return not self.pointers[stack_num]
        return all(self.is_empty(stack_num) for stack_num in range(self.number_of_stacks))

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_capacity
        return offset + self.pointers[stack_num] - 1

    def size(self, stack_num=None):
        if stack_num is not None:
            return self.pointers[stack_num]
        return sum(self.size(stack_num) for stack_num in range(self.number_of_stacks))

    # Operations
    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise FullStackError('Stack is full')

        self.pointers[stack_num] += 1
        self.stack[self.index_of_top(stack_num)] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise EmptyStackError('Stack is empty')

        top_index = self.index_of_top(stack_num)
        value = self.stack[top_index]
        self.stack[top_index] = 0
        self.pointers[stack_num] -= 1

        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise EmptyStackError('Stack is empty')

        return self.stack[self.index_of_top(stack_num)]
