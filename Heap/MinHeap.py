class EmptyHeapException(Exception):
    pass


class MinHeap:
    def __init__(self):
        self._heap = []

    @staticmethod
    def _parent(index):
        return (index - 1) // 2

    @staticmethod
    def _left_child(index):
        return index * 2 + 1

    @staticmethod
    def _right_child(index):
        return index * 2 + 2

    def _is_valid(self, index):
        return index < self.size()

    def _swap(self, index1, index2):
        self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]

    def _propagate_to_ancestors(self, index):
        if not index:
            return

        parent = self._parent(index)
        if self._heap[parent] > self._heap[index]:
            self._swap(parent, index)
            self._propagate_to_ancestors(parent)

    def _propagate_to_descendents(self, index):
        left = self._left_child(index)
        right = self._right_child(index)

        if not self._is_valid(left) and not self._is_valid(right):
            return

        go_right = not self._is_valid(left) or (self._is_valid(right) and self._heap[right] < self._heap[left])
        if go_right and self._heap[right] < self._heap[index]:
            self._swap(right, index)
            self._propagate_to_descendents(right)
        elif not go_right and self._heap[left] < self._heap[index]:
            self._swap(left, index)
            self._propagate_to_descendents(left)

    def is_empty(self):
        return not self._heap

    def size(self):
        return len(self._heap)

    def push(self, value):
        self._heap.append(value)
        self._propagate_to_ancestors(self.size() - 1)

    def pop(self):
        if self.is_empty():
            raise EmptyHeapException('heap is empty')
        value = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        self._propagate_to_descendents(0)
        return value

    def peek(self):
        if self.is_empty():
            raise EmptyHeapException('heap is empty')
        return self._heap[0]

