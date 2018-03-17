from unittest import TestCase


class Solution:
    @staticmethod
    def add_on(data):
        if not data:
            return []
        result = [0] * len(data)
        carry = 1
        for i in range(len(data) - 1, -1, -1):
            sum = data[i] + carry
            if sum == 10:
                carry = 1
                sum = 0
            else:
                carry = 0
            result[i] = sum
        if carry == 1:
            new_array = [1]
            for digit in result:
                new_array.append(digit)
            result = new_array
        return result


class TestSolution(TestCase):
    def test(self):

        result = Solution.add_on([1, 2, 3, 4])
        self.assertEqual([1, 2, 3, 5], result)

        result = Solution.add_on([])
        self.assertEqual([], result)

        result = Solution.add_on([1])
        self.assertEqual([2], result)

        result = Solution.add_on([9, 9, 9])
        self.assertEqual([1, 0, 0, 0], result)

