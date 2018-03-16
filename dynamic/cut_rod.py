import unittest


class CutRod:

    # time 2^n
    @staticmethod
    def cut_rod_brute(prices, n):
        if n == 0:
            return 0
        q = float("-inf")
        for i in range(1, n + 1):
            q = max(q, prices[i] + CutRod.cut_rod_brute(prices, n - i))
        return q

    # time - O(n^2)
    @staticmethod
    def memoized_cut_rod(prices, n):
        tmp = [float("-inf")] * (n + 1)
        return CutRod.memoized_cut_rod_aux(prices, n, tmp)

    @staticmethod
    def memoized_cut_rod_aux(prices, n, saved):
        if saved[n] >= 0:
            return saved[n]
        if n == 0:
            q = 0
        else:
            q = float("-inf")
            for i in range(1, n + 1):
                q = max(q, prices[i] + CutRod.memoized_cut_rod_aux(prices, n - i, saved))
        saved[n] = q
        return q

    # time - O(n^2)
    @staticmethod
    def bottom_up(prices, n):
        saved = [float("-inf")] * (n + 1)
        pieces = [0] * (n + 1)
        saved[0] = 0
        for j in range(1, n + 1):
            q = float("-inf")
            for i in range(1, j + 1):
                if len(prices) > i:
                    full_piece_price = prices[i]
                else:
                    full_piece_price = 0
                q = max(q, full_piece_price + saved[j - i])
                pieces[j] = i
            saved[j] = q
        return saved[n], pieces


class TestCutRod(unittest.TestCase):
    def test_brute(self):
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        res = CutRod.cut_rod_brute(
            prices,
            4
        )
        self.assertEqual(res, 10)
        res = CutRod.cut_rod_brute(
            prices,
            10
        )
        self.assertEqual(res, 30)
        res = CutRod.cut_rod_brute(
            prices,
            7
        )
        self.assertEqual(res, 18)

    def test_memoized(self):
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        res = CutRod.memoized_cut_rod(
            prices,
            4
        )
        self.assertEqual(res, 10)
        res = CutRod.memoized_cut_rod(
            prices,
            10
        )
        self.assertEqual(res, 30)
        res = CutRod.memoized_cut_rod(
            prices,
            7
        )
        self.assertEqual(res, 18)

    def test_bottom_up(self):
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        max_price, pieces = CutRod.bottom_up(
            prices,
            40
        )
        self.assertEqual(120, max_price)
        res, pieces = CutRod.bottom_up(
            prices,
            10
        )
        self.assertEqual(res, 30)
        res, pieces = CutRod.bottom_up(
            prices,
            7
        )
        self.assertEqual(res, 18)


if __name__ == "__main__":
    unittest.main()