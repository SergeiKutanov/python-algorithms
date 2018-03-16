def solve(arr, money):
    data = {}
    for i in range(0, len(arr)):
        complement = money - arr[i]
        if complement in data and data[complement] != i:
            first_index = i
            second_index = data[complement]
            if second_index < first_index:
                first_index, second_index = second_index, first_index
            print("%d, %d" % (first_index + 1, second_index + 1))
            return
        data[arr[i]] = i


if __name__ == "__main__":
    solve([1, 4, 5, 3, 2], 4)
    solve([2, 2, 4, 3], 4)