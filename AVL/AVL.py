class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.balance_factor = 0
        self.height = 0

    def __str__(self):
        return self.value

    def compare_with(self, value):
        if self.value == value:
            return 0
        return -1 if self.value > value else 1

    def is_leaf(self):
        return not self.left and not self.right

    def is_full(self):
        return self.left and self.right


class AVLIterator:
    def __init__(self, root):
        self.root = root

    def __iter__(self):
        current = self.root
        stack = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                yield current.value
                current = current.right
            else:
                break


class AVL:
    def __init__(self):
        self._root = None
        self._node_count = 0
        self._height = 0

    def __iter__(self):
        return iter(AVLIterator(self._root))

    # Properties
    def height(self):
        """
        The height of a rooted tree is the number of edges between the tree's
        root and its furthest leaf. This means that a tree containing a single
        node has a height of 0.
        :return: int
        """
        return 0 if not self._root else self._root.height

    def size(self):
        """
        Returns the number of nodes in the tree.
        :return: int
        """
        return self._node_count

    def is_empty(self):
        """
        Returns whether or not the tree is empty.
        :return: bool
        """
        return not self.size()

    # Rotations
    def _left_rotate(self, node):
        # IMAGE: https://i.ytimg.com/vi/_nyt5QYel3Q/maxresdefault.jpg
        new_parent = node.right
        node.right = new_parent.left
        new_parent.left = node

        # Update height and balance factor
        self._update(node)
        self._update(new_parent)

        return new_parent

    def _right_rotate(self, node):
        # IMAGE: https://i.ytimg.com/vi/_nyt5QYel3Q/maxresdefault.jpg
        new_parent = node.left
        node.left = new_parent.right
        new_parent.right = node

        # Update height and balance factor
        self._update(node)
        self._update(new_parent)

        return new_parent

    def _left_left_case(self, node):
        return self._right_rotate(node)

    def _left_right_case(self, node):
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)

    def _right_right_case(self, node):
        return self._left_rotate(node)

    def _right_left_case(self, node):
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)

    # queries
    def _contains(self, node, value):
        """  Recursive contains helper method. """

        if not node:
            return False

        comparison = node.compare_with(value)
        if not comparison:
            return True
        return self._contains(node.left, value) if comparison == -1 else self._contains(node.right, value)

    def contains(self, value):
        """
        Return true/false depending on whether a value exists in the tree.
        :param value:
        :return: bool
        """
        return self._contains(self._root, value)

    @staticmethod
    def _update(node):
        """
        Update a node's height and balance factor.
        :param node:
        :return: None
        """
        left_node_height = node.left.height if node.left else -1
        right_node_height = node.right.height if node.right else -1

        # Update this node's height.
        node.height = 1 + max(left_node_height, right_node_height)

        # Update balance factor
        node.balance_factor = right_node_height - left_node_height

    def _balance(self, node):
        """
        Re-balance a node if its balance factor is +2 or -2.
        :param node:
        :return: Node
        """
        # Left heavy subtree
        if node.balance_factor == -2:
            if node.left.balance_factor <= 0:
                # Left-Left Case
                return self._left_left_case(node)
            else:
                # Left-Right Case
                return self._left_right_case(node)
        elif node.balance_factor == 2:
            if node.right.balance_factor >= 0:
                # Right-Right Case
                return self._right_right_case(node)
            else:
                # Right-Left Case
                return self._right_left_case(node)

        # Node either has a balance factor of 0, +1 or -1 which is fine.
        return node

    def _insert(self, node, value):
        """
        Inserts a value inside the AVL tree.
        :param node:
        :param value:
        :return: Node
        """
        if not node:
            return Node(value)

        comparison = node.compare_with(value)
        if comparison == -1:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        # Update balance factor and height values.
        self._update(node)

        # Re-balance tree.
        return self._balance(node)

    def insert(self, value):
        """
        Insert/add a value to the AVL tree. The value must not be null, O(log(n))
        :param value:
        :return: bool
        """
        if value is None or self.contains(value):
            return False

        self._root = self._insert(self._root, value)
        self._node_count += 1
        return True

    @staticmethod
    def _find_max(node):
        """ Finds the maximum value in the subtree """
        while node.right:
            node = node.right
        return node.value

    @staticmethod
    def _find_min(node):
        """ Finds the minimum value in the subtree """
        while node.left:
            node = node.left
        return node.value

    def _remove(self, node, value):
        """ Removes a node """
        if not node:
            return None

        comparison = node.compare_with(value)
        if comparison == -1:
            node.left = self._remove(node.left, value)
        elif comparison == 1:
            node.right = self._remove(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                # Choose to remove from left subtree
                if node.left.height > node.right.height:
                    # Swap the value of the successor into the node.
                    successor = self._find_max(node.left)
                    node.value = successor

                    # Find the largest node in the left subtree.
                    node.left = self._remove(node.left, successor)
                else:
                    # Swap the value of the successor into the node.
                    successor = self._find_min(node.right)
                    node.value = successor

                    # Go into the right subtree and remove the leftmost node we
                    # found and swapped data with. This prevents us from having
                    # two nodes in our tree with the same value.
                    node.right = self._remove(node.right, successor)

        # Update balance factor and height values.
        self._update(node)

        # Re-balance tree
        return self._balance(node)

    def remove(self, value):
        """
        Remove a value from this binary tree if it exists, O(log(n))
        :param value:
        :return: bool
        """
        if value is None or not self.contains(value):
            return False

        self._root = self._remove(self._root, value)
        self._node_count -= 1
        return True
