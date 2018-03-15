import unittest


class Solution:
    @staticmethod
    def is_matched(expression):
        brackets_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = list()
        for ch in expression:
            if ch not in brackets_dict:
                stack.append(ch)
            else:
                if len(stack) < 1:
                    return False
                recent_opening_bracket = stack.pop()
                if recent_opening_bracket != brackets_dict[ch]:
                    return False
        return len(stack) == 0


class TestSolution(unittest.TestCase):
    def test_is_matched(self):

        result = Solution.is_matched("[()][{}()][](){}([{}(())([[{}]])][])[]([][])(){}{{}{[](){}}}()[]({})[{}{{}([{}][])}]")
        self.assertEqual(True, result)

        result = Solution.is_matched("[()][{}[{}[{}]]][]{}[]{}[]{{}({}(){({{}{}[([[]][[]])()]})({}{{}})})}")
        self.assertEqual(True, result)

        result = Solution.is_matched("(])[{{{][)[)])(]){(}))[{(})][[{)(}){[(]})[[{}(])}({)(}[[()}{}}]{}{}}()}{({}](]{{[}}(([{]")
        self.assertEqual(False, result)

        result = Solution.is_matched("){[]()})}}]{}[}}})}{]{](]](()][{))])(}]}))(}[}{{)}{[[}[]")
        self.assertEqual(False, result)


if __name__ == "__main__":
    unittest.main()