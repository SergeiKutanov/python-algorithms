import unittest


class Solution:

    def __init__(self, matrix):
        self.matrix = matrix
        self.visited = []

    def solve(self, matrix):
        pass


    def find_region_size(self, i, j):
        pass


class TestSolution(unittest.TestCase):
    def test(self):
        matrix = [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 0]
        ]
        size = Solution.solve(matrix)
        self.assertEqual(5, size)