class SimpleList:
    def __init__(self, items=()):
        print("SimpleList.__init__()")
        self._items = list(items)

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)

    def add(self, item):
        print("SimpleList.add()")
        self._items.append(item)

    def sort(self):
        self._items.sort()


class SortedList(SimpleList):
    def __init__(self, items=()):
        print("SortedList.__init__()")
        super().__init__(items)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self))

    def add(self, item):
        print("SortedList.add()")
        super().add(item)
        self.sort()


class IntList(SimpleList):
    def __init__(self, items=()):
        print("IntList.__init__()")
        for x in items:
            self._validate(x)
        super().__init__(items)

    def __repr__(self):
        return "IntList({!r})".format(list(self))

    @staticmethod
    def _validate(val):
        if not isinstance(val, int):
            raise TypeError('IntList only supports integer values.')

    def add(self, item):
        print("IntList.add()")
        self._validate(item)
        super().add(item)


class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedIntList({!r})".format(list(self))
