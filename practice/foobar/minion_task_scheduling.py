import unittest


class Solution:
    @staticmethod
    def answer(data, n):
        counter = {}
        for i in range(0, len(data)):
            if data[i] in counter:
                counter[data[i]] += 1
            else:
                counter[data[i]] = 0
        result = []
        for i in range(0, len(data)):
            if counter[data[i]] < n:
                result.append(data[i])
        return result


class TestSolution(unittest.TestCase):
    def test(self):
        answer = Solution.answer([1, 2, 3], 0)
        self.assertEqual([], answer)

        answer = Solution.answer([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
        self.assertEqual([1, 4], answer)

        answer = Solution.answer([1, 2, 3], 6)
        self.assertEqual([1, 2, 3], answer)


if __name__ == "__main__":
    unittest.main()