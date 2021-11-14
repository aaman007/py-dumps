class ArrayList:
    def __init__(self, items=None):
        self._capacity = 1 if not items else self._get_possible_size(len(items))
        self._pointer = 0 if not items else len(items)
        self._data = [0] * self._capacity
        items and self._copy(items)

    def __str__(self):
        return self._data[:self._pointer].__str__()

    def __repr__(self):
        return self._data[:self._pointer].__repr__()

    def __len__(self):
        return self._pointer

    def __iter__(self):
        for i in range(self._pointer):
            yield self._data[i]

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise IndexError("list index must be an integer.")
        if index >= self._pointer or -index > self._pointer:
            raise IndexError("list index out of bound.")
        return self._data[index] if index >= 0 else self._data[index - (self._capacity - self._pointer)]

    @staticmethod
    def _get_possible_size(n):
        x = 1
        while x < n:
            x *= 2
        return x

    def _copy(self, old_list):
        for i in range(len(old_list)):
            self._data[i] = old_list[i]

    def _is_full(self):
        return self._pointer >= self._capacity

    def _resize(self):
        self._capacity *= 2
        old_list = self._data.copy()
        self._data = [0] * self._capacity
        self._copy(old_list)

    def append(self, val):
        self._is_full() and self._resize()
        self._data[self._pointer] = val
        self._pointer += 1

    def pop(self):
        self._pointer -= 1
