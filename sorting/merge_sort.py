import unittest


class Solution:
    @staticmethod
    def merge_sort(data, p, r):
        if p < r:
            q = (p + r) // 2
            Solution.merge_sort(data, p, q)
            Solution.merge_sort(data, q + 1, r)
            Solution.merge(data, p, q, r)

    @staticmethod
    def merge(data, p, q, r):
        n1 = q - p
        n2 = r - q
        left = []
        right = []
        for i in range(0, n1 + 1):
            left.append(data[p + i])
        for i in range(0, n2):
            right.append(data[q + i + 1])
        i, j = 0, 0
        k = p
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1


class TestSolution(unittest.TestCase):
    def test(self):
        data = [100, -5, 0, -5, 3, 1, -200]
        Solution.merge_sort(data, 0, len(data) - 1)
        self.assertEqual(
            [-200, -5, -5, 0, 1, 3, 100],
            data
        )


if __name__ == "__main__":
    unittest.main()