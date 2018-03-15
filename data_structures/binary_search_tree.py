class BST:
    _root = None

    def get_root(self):
        return self._root

    def insert(self, node):
        y = None
        x = self._root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self._root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def delete(self, node):
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            y = self.tree_minimum(node.right)
            if y.parent != node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y

    def transplant(self, u, v):
        if u.parent is None:
            self._root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def tree_minimum(self, node=None):
        if node is None:
            node = self._root
        while node.left is not None:
            node = node.left
        return node

    def tree_maximum(self, node=None):
        if node is None:
            node = self._root
        while node.right is not None:
            node = node.right
        return node

    def search(self, key, node=None):
        if node is None:
            x = self._root
        else:
            x = node
        if x is None or key == x.key:
            return x
        if key < x.key:
            return self.search(key, x.left)
        else:
            return self.search(key, x.right)

    def successor(self, node):
        if node.right is not None:
            return self.tree_minimum(node.right)
        y = node.parent
        while y is not None and node == y.right:
            node = y
            y = y.parent
        return y

    def predecessor(self, node):
        if node.left is not None:
            return self.tree_maximum(node.left)
        y = node.parent
        while y is not None and node == y.left:
            node = y
            y = y.parent
        return y

    class Node:

        key = None
        left = None
        right = None
        parent = None

        def __init__(self, key):
            self.key = key


def main():
    bst = BST()
    bst.insert(BST.Node(12))
    bst.insert(BST.Node(15))
    bst.insert(BST.Node(19))
    bst.insert(BST.Node(13))
    bst.insert(BST.Node(2))
    bst.insert(BST.Node(9))
    bst.insert(BST.Node(5))
    bst.insert(BST.Node(18))
    bst.insert(BST.Node(17))

    next_node = bst.tree_minimum()
    while next_node is not None:
        print(next_node.key)
        next_node = bst.successor(next_node)

    print("-------------------------")

    next_node = bst.tree_maximum()
    while next_node is not None:
        print(next_node.key)
        next_node = bst.predecessor(next_node)


if __name__ == "__main__":
    main()