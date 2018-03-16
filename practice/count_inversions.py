def get_sum(bit, max_element):
    summ = 0
    while max_element > 0:
        summ += bit[max_element]
        max_element -= max_element & (-max_element)
    return summ


def update_bit(bit, n, index, val):
    while index <= n:
        bit[index] += val
        index += index & (-index)

def countInversions(arr):
    inversions = 0
    max_element = 0
    for i in range(0, len(arr)):
        if max_element < arr[i]:
            max_element = arr[i]
    bit = [0] * (max_element + 1)
    for i in range(len(arr) - 1, -1, -1):
        inversions += get_sum(bit, arr[i] - 1)
        update_bit(bit, max_element, arr[i], 1)
    return inversions