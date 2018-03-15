import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:

    MINIMUM = -1
    MAXIMUM = 10001

    @staticmethod
    def check_bst(root):
        return Solution.bst_util(root, Solution.MINIMUM, Solution.MAXIMUM)

    @staticmethod
    def bst_util(node, minimum, maximum):
        if node is None:
            return True
        if node.data <= minimum or node >= maximum:
            return False
        return Solution.bst_util(node, Solution.MINIMUM, node.data) and Solution.bst_util(node, node.data, Solution.MAXIMUM)