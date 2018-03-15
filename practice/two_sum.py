# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
import unittest


class Solution:

    # time - O(n^2)
    # memory - O(1)
    @staticmethod
    def brute_force(nums, target):
        for i in range(0, len(nums)):
            for k in range(i+1, len(nums)):
                if nums[i] + nums[k] == target:
                    return [i, k]

    # time - O(2n) = O(n)
    # memory - O(n)
    @staticmethod
    def two_pass_hash_table(nums, target):
        num_map = {}
        for i in range(0, len(nums)):
            num_map.update({nums[i]: i})
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [i, num_map[complement]]

    # time - O(n)
    # memory - O(n)
    @staticmethod
    def one_pass_hash_table(nums, target):
        num_map = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [i, num_map[complement]]
            num_map.update({nums[i]: i})


class SolutionTest(unittest.TestCase):

    def test_brute_force(self):
        data = [-3, 0, 3, 4, 6, 9]
        result = Solution.brute_force(data, 0)
        self.assertEqual(0, result[0])
        self.assertEqual(2, result[1])

        result = Solution.brute_force(data, 9)
        self.assertEqual(1, result[0])
        self.assertEqual(5, result[1])

    def test_two_way_hash_table(self):
        data = [-3, 0, 3, 4, 6, 9]
        result = Solution.two_pass_hash_table(data, 0)
        self.assertEqual(0, result[0])
        self.assertEqual(2, result[1])

        result = Solution.two_pass_hash_table(data, 9)
        self.assertEqual(1, result[0])
        self.assertEqual(5, result[1])

    def test_one_pass_hash_table(self):
        data = [-3, 0, 3, 4, 6, 9]
        result = Solution.one_pass_hash_table(data, 0)
        self.assertEqual(2, len(result))
        self.assertIn(0, result)
        self.assertIn(2, result)

        result = Solution.one_pass_hash_table(data, 9)
        self.assertEqual(2, len(result))
        self.assertIn(2, result)
        self.assertIn(4, result)


if __name__ == "__main__":
    unittest.main()
