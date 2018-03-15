class TreeNode:
    def __init__(self, key = None):
        self.key = key

    RED = 1
    BLACK = 2

    left = None
    right = None
    key = None
    parent = None
    color = None


class RedBlackTree:

    root = None
    nil = None

    def __init__(self):
        self.nil = TreeNode()
        self.root = self.nil

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def rb_insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = TreeNode.RED
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z):
        while z.parent.color == TreeNode.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == TreeNode.RED:
                    z.parent.color = TreeNode.BLACK
                    y.color = TreeNode.BLACK
                    z.parent.parent.color = TreeNode.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = TreeNode.BLACK
                    z.parent.parent.color = TreeNode.RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == TreeNode.RED:
                    z.parent.color = TreeNode.BLACK
                    y.color = TreeNode.BLACK
                    z.parent.parent.color = TreeNode.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = TreeNode.BLACK
                    z.parent.parent.color = TreeNode.RED
                    self.left_rotate(z.parent.parent)
        self.root.color = TreeNode.BLACK

    def rb_transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def rb_delete(self, z):
        y = z
        y_or_color = y.color
        if z.left == self.nil:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_or_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_or_color == TreeNode.BLACK:
            self.rb_delete_fixup(x)

    def tree_minimum(self, node=None):
        if node is None:
            node = self.root
        while node.left != self.nil:
            node = node.left
        return node

    def tree_maximum(self, node=None):
        if node is None:
            node = self.root
        while node.right != self.nil:
            node = node.right
        return node

    def rb_delete_fixup(self, x):
        while x != self.root and x.color == TreeNode.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == TreeNode.RED:
                    w.color = TreeNode.BLACK
                    x.parent.color = TreeNode.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == TreeNode.BLACK and w.right.color == TreeNode.BLACK:
                    w.color = TreeNode.RED
                    x = x.parent
                else:
                    if w.right.color == TreeNode.BLACK:
                        w.left.color = TreeNode.BLACK
                        w.color = TreeNode.RED
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = TreeNode.BLACK
                    w.right.color = TreeNode.BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == TreeNode.RED:
                    w.color = TreeNode.BLACK
                    x.parent.color = TreeNode.RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == TreeNode.BLACK and w.left.color == TreeNode.BLACK:
                    w.color = TreeNode.RED
                    x = x.parent
                else:
                    if w.left.color == TreeNode.BLACK:
                        w.right.color = TreeNode.BLACK
                        w.color = TreeNode.RED
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = TreeNode.BLACK
                    w.left.color = TreeNode.BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = TreeNode.BLACK

    def search(self, key, node=None):
        if node is None:
            x = self.root
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


def main():
    reb_black_tree = RedBlackTree()
    reb_black_tree.rb_insert(TreeNode(11))
    reb_black_tree.rb_insert(TreeNode(2))
    reb_black_tree.rb_insert(TreeNode(1))
    reb_black_tree.rb_insert(TreeNode(7))
    reb_black_tree.rb_insert(TreeNode(5))
    reb_black_tree.rb_insert(TreeNode(8))
    reb_black_tree.rb_insert(TreeNode(4))
    reb_black_tree.rb_insert(TreeNode(14))
    reb_black_tree.rb_insert(TreeNode(15))

    node = reb_black_tree.search(7)
    reb_black_tree.rb_delete(node)
    t = 1


if __name__ == '__main__':
    main()