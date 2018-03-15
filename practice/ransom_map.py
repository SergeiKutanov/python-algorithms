import unittest


class Solution:
    @staticmethod
    def map_method(magazine, ransom):
        magazine_map = Solution.build_map(magazine)
        for word in ransom:
            if word not in magazine_map or magazine_map[word] < 1:
                return False
            magazine_map[word] -= 1
        return True

    @staticmethod
    def build_map(data):
        data_map = {}
        for word in data:
            if word in data_map:
                data_map[word] += 1
            else:
                data_map.update({word: 1})
        return data_map


class TestSolution(unittest.TestCase):
    def test_map_method(self):
        result = Solution.map_method(
            "give me one grand today night",
            "give one grand today"
        )
        self.assertEqual(True, result)

        result = Solution.map_method(
            "two times three is not four",
            "two times two is four"
        )
        self.assertEqual(False, result)

if __name__ == '__main__':
    unittest.main()