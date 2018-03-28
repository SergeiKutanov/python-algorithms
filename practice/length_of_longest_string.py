import unittest

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        seen = {}
        a, i, j = 0, 0, 0
        while i < l and j < l:
            if s[j] not in seen:
                seen[s[j]] = 0
                j += 1
                a = max(a, j - i)
            else:
                del seen[s[i]]
                i += 1
        return a


class TestSolution(unittest.TestCase):
    def test(self):
        s = Solution()
        r = s.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(3, r)