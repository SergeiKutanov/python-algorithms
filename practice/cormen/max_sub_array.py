import unittest

class Solution:

    @staticmethod
    def find_max_crossing(data, low, mid, high):
        left_sum = float("-inf")
        max_left = None
        sum = 0
        for i in range(mid, low - 1, -1):
            sum = sum + data[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i
        sum = 0
        right_sum = float("-inf")
        max_right = None
        for j in range(mid + 1, high + 1):
            sum = sum + data[j]
            if sum > right_sum:
                right_sum = sum
                max_right = j
        return max_left, max_right, left_sum + right_sum

    @staticmethod
    def find_max_subarray(data, low, high):
        if high == low:
            return low, high, data[low]
        else:
            mid = (low + high) // 2
            left_low, left_high, left_sum = Solution.find_max_subarray(data, low, mid)
            right_low, right_high, right_sum = Solution.find_max_subarray(data, mid + 1, high)
            cross_low, cross_high, cross_sum = Solution.find_max_crossing(data, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


class TestSolution(unittest.TestCase):
    def test(self):
        data = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        low, high, sum = Solution.find_max_subarray(data, 0, len(data) - 1)
        self.assertEqual(7, low)
        self.assertEqual(10, high)
        self.assertEqual(43, sum)