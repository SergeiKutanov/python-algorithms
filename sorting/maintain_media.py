import heapq
import unittest


class MMedian:
    def __init__(self):
        self._minheap = []
        self._maxheap = []

    def _sizelower(self):
        return len(self._maxheap)

    def _sizeupper(self):
        return len(self._minheap)

    def _peekupper(self):
        if self._minheap:
            return self._minheap[0]
        else:
            return float('+inf')

    def _peeklower(self):
        if self._maxheap:
            return -self._maxheap[0]
        else:
            return float('-inf')

    def _pushlower(self, data):
        heapq.heappush(self._maxheap, -data)

    def _pushupper(self, data):
        heapq.heappush(self._minheap, data)

    def _replacelower(self, data):
        return -heapq.heapreplace(self._maxheap, -data)

    def _replaceupper(self, data):
        return heapq.heapreplace(self._minheap, data)

    def add(self, data):
        if self._sizelower() == self._sizeupper():
            if data < self._peekupper():
                self._pushlower(data)
            else:
                self._pushlower(self._replaceupper(data))
        else:
            if data > self._peeklower():
                self._pushupper(data)
            else:
                self._pushupper(self._replacelower(data))

    def median(self):
        if self._sizelower() == self._sizeupper():
            return (self._peeklower() + self._peekupper()) / 2
        else:
            return self._peeklower()


class TestMMedian(unittest.TestCase):
    def test(self):
        median = MMedian()
        current_median = 0.5
        for i in range(1, 11):
            median.add(i)
            current_median += 0.5
            self.assertEqual(current_median, median.median())


if __name__ == '__main__':
    unittest.main()
