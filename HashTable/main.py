from typing import Any, Union


class ListNode:
    def __init__(self, key, value, nxt=None):
        self.key: str = key
        self.value: Any = value
        self.next: Union[ListNode, None] = nxt


class HashTable:
    def __init__(self):
        self._SIZE: int = 100
        self._BASE: int = 1331
        self._hash_table: list = [None] * self._SIZE
        self._keys = set()

    def __str__(self):
        return self._keys.__str__()

    def __repr__(self):
        representation = ['{ ']
        for key in self._keys:
            if len(representation) > 1:
                representation.append(', ')
            representation.append(f"{key}: {self.__getitem__(key)}")
        representation.append(' }')
        return ''.join(representation)

    def __len__(self):
        return self._keys.__len__()

    def __getitem__(self, key):
        """ Gets the value for a key """

        index = self._get_index(key)
        node = self._get_node(self._hash_table[index], key)
        if not node:
            raise KeyError('key does not exists.')
        return node.value

    def __setitem__(self, key, value):
        """
        Sets a new key in the hash_table

        If the mapped index in the hash_table does not contain a LinkedList
        creates a new one

        If does exists, then checks if that key is already in the LinkedList
        If Yes, changes it's value
        Otherwise, creates a new node and makes it the head of the LinkedList
        """

        index = self._get_index(key)
        self._keys.add(key)
        if not self._hash_table[index]:
            self._hash_table[index] = ListNode(key, value)
        else:
            node = self._get_node(self._hash_table[index], key)
            if not node:
                node = ListNode(key, value)
                node.next = self._hash_table[index]
                self._hash_table[index] = node
            else:
                node.value = value

    def __delitem__(self, key):
        """ Deletes a key from the hash_table """

        index = self._get_index(key)
        self._keys.remove(key)
        node, prev = self._get_node(self._hash_table[index], key, include_prev=True)
        if not node:
            raise KeyError('key does not exists.')

        if prev:
            """ In case the node was not head, changes it's previous node's next pointer """
            prev.next = node.next
        else:
            """ If it was a head, points hash_table index to new head """
            self._hash_table[index] = node.next
        node.next = None

    @staticmethod
    def _get_node(head, key, include_prev=False) -> Union[ListNode, tuple, None]:
        """
        Searches for a given key in a LinkedList
        Returns None if it does not exists
        Or Returns the node itself and optionally it's previous node
        """

        prev = None
        while head:
            if head.key == key:
                if not include_prev:
                    return head
                return head, prev
            prev = head
            head = head.next
        return None

    @staticmethod
    def _get_order(char) -> int:
        """ Gets order of a char in integer value """
        if 'a' <= char <= 'z':
            return ord(char) - ord('a')
        elif 'A' <= char <= 'Z':
            return 26 + ord(char) - ord('A')
        elif '0' <= char <= '9':
            return 52 + ord(char) - ord('0')
        raise KeyError('key cannot contain anything other than alphabets and digits.')

    @staticmethod
    def _normalize(key) -> str:
        """ Converts key to string """
        return str(key)

    def _get_hash_value(self, key) -> int:
        """ Hashes the given key """
        hash_value = 0
        for ch in self._normalize(key):
            hash_value = hash_value * self._BASE + self._get_order(ch)
        return hash_value

    def _get_index(self, key) -> int:
        """ Maps hash_value to a index in hash_table """
        return self._get_hash_value(key) % self._SIZE
