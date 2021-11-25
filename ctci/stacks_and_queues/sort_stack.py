"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array) . The stack supports the following operations: push, pop, peek, and isEmpty.
"""


def sort_stack(unsorted_stack):
    sorted_stack = []

    while unsorted_stack:
        top = unsorted_stack.pop()
        while sorted_stack and sorted_stack[-1] > top:
            unsorted_stack.append(sorted_stack.pop())
        sorted_stack.append(top)

    while sorted_stack:
        unsorted_stack.append(sorted_stack.pop())

    return unsorted_stack

