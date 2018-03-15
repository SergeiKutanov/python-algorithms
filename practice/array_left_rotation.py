import unittest
from collections import deque


class Solution:
    # time - O(2n)
    # space = O(3n)
    @staticmethod
    def array_left_rotation(a, n, k):
        res_map = {}
        result = []
        for i in range(0, n):
            new_index = i - k
            if new_index < 0:
                new_index += n
            res_map.update({new_index: a[i]})
        for i in range(n):
            result.append(res_map[i])
        return result

    @staticmethod
    def queue_method(a, n, k):
        a = deque(a)
        a.rotate(k * -1)
        return list(a)

    @staticmethod
    def slicing(a, n, k):
        return a[k:] + a[:k]


class SolutionTest(unittest.TestCase):
    def test_array_left_rotation(self):
        n, k = 5, 4
        a = [1, 2, 3, 4, 5]
        answer = Solution.array_left_rotation(a, n, k)
        self.assertEqual([5, 1, 2, 3, 4], answer)

    def test_queue_method(self):
        n, k = 5, 4
        a = [1, 2, 3, 4, 5]
        answer = Solution.queue_method(a, n, k)
        self.assertEqual([5, 1, 2, 3, 4], answer)

    def test_slicing_method(self):
        n, k = 5, 4
        a = [1, 2, 3, 4, 5]
        answer = Solution.slicing(a, n, k)
        self.assertEqual([5, 1, 2, 3, 4], answer)


if __name__ == "__main__":
    unittest.main()
