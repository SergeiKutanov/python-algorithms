# Binary Indexed Tree or Fenwick Tree
# 1. Find the sum of first i elements in the origina array O(lgn)
# 2. Change the value in original array and keep the bit maintained
# The tree has two views - update view and sum view, difference is in the way parent is computed

def build_bit(data):
    bit = [0] * (len(data) + 1)
    for i in range(0, len(data)):
        updateBit(bit, len(data), i, data[i])
    return bit

def updateBit(bit, n, index, val):
    index = index + 1
    while index <= n:
        bit[index] += val
        index += index & (-index)

def getSum(bit, index):
    summ = 0
    index += 1
    while index > 0:
        summ += bit[index]
        index -= index & (-index)
    return summ

bit = build_bit([2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9])
print(getSum(bit, 6))