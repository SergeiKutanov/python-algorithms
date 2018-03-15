import unittest
from collections import Counter


class Solution:

    # time O(2n + 2m)
    # memory O(2n + 2m)
    @staticmethod
    def maps_solution(a, b):
        a_map = Solution.build_map(a)
        b_map = Solution.build_map(b)
        result = 0
        for ch in a_map:
            if ch not in b_map:
                result += a_map[ch]
            else:
                diff = a_map[ch] - b_map[ch]
                if diff < 1:
                    diff *= -1
                result += diff
        for ch in b_map:
            if ch not in a_map:
                result += b_map[ch]
        return result

    @staticmethod
    def build_map(a):
        a_map = {}
        for ch in a:
            if ch in a_map:
                a_map[ch] += 1
            else:
                a_map.update({ch: 1})
        return a_map

    # time O(n)
    # memory O(n)
    @staticmethod
    def shrink_method(a, b):
        for ch in a:
            if ch in b:
                a = a.replace(ch, "", 1)
                b = b.replace(ch, "", 1)
        return len(a) + len(b)

    # basically same as shrink
    @staticmethod
    def featured_solution(a, b):
        a = Counter(a)
        b = Counter(b)
        c = a - b
        d = b - a
        e = c + d
        return len(list(e.elements()))


class TestSolution(unittest.TestCase):
    def test_map_method(self):
        result = Solution.maps_solution("cde", "abc")
        self.assertEqual(4, result)

        result = Solution.maps_solution("fsqoiaidfaukvngpsugszsnseskicpejjvytviya", "ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget")
        self.assertEqual(42, result)

    def test_string_shrink(self):
        result = Solution.shrink_method("cde", "abc")
        self.assertEqual(4, result)

        result = Solution.shrink_method("fsqoiaidfaukvngpsugszsnseskicpejjvytviya", "ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget")
        self.assertEqual(42, result)

    def test_featured_solution(self):
        result = Solution.featured_solution("cde", "abc")
        self.assertEqual(4, result)

        result = Solution.featured_solution("fsqoiaidfaukvngpsugszsnseskicpejjvytviya", "ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget")
        self.assertEqual(42, result)


if __name__ == "__main__":
    unittest.main()