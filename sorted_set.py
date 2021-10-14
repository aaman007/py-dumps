from bisect import bisect_left
from collections.abc import Sequence, MutableSet
from itertools import chain


class SortedSet(Sequence, MutableSet):
    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        # for item in self._items:
        #     yield item
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return "SortedSet({})".format(repr(self._items) if self._items else '')

    def __eq__(self, other):
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items == other._items

    def __ne__(self, other):
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items != other._items

    # def __reversed__(self):
    #     # As __len__ and __getitem__ is implemented this is not required
    #     for item in self._items[::-1]:
    #         yield item

    def __add__(self, other):
        return SortedSet(chain(self._items, other._items))

    def __mul__(self, other):
        return self.copy() if other > 0 else SortedSet()

    def __rmul__(self, other):
        return self * other

    def count(self, value):
        return int(value in self)

    def index(self, value, **kwargs):
        index = bisect_left(self._items, value)
        if index != len(self._items) and self._items[index] == value:
            return index
        raise ValueError("{} not found".format(repr(value)))

    def issubset(self, iterable):
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedSet(iterable)

    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedSet(iterable)

    def difference(self, iterable):
        return self - SortedSet(iterable)

    def copy(self):
        return SortedSet(self._items)

    def add(self, value):
        if value not in self:
            index = bisect_left(self._items, value)
            self._items.insert(index, value)

    def discard(self, value):
        if value in self:
            self._items.remove(value)
