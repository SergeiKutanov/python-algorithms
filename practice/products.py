def product_except_self(data):
    length = len(data)
    result = [1] * length
    left = 1
    for x in range(length - 1):
        left *= data[x]
        result[x + 1] *= left
    right = 1
    for x in range(length - 1, 0, -1):
        right *= data[x]
        result[x - 1] *= right
    return result


def spiral_matrix(data):
    if not data:
        return []
    up = 0
    left = 0
    down = len(data) - 1
    right = len(data[0]) - 1
    direct = 0
    res = []
    while True:
        if direct == 0:
            for i in range(left, right + 1):
                res.append(data[up][i])
            up += 1
        if direct == 1:
            for i in range(up, down + 1):
                res.append(data[i][right])
            right -= 1
        if direct == 2:
            for i in range(right, left - 1, -1):
                res.append(data[down][i])
            down -= 1
        if direct == 3:
            for i in range(down, up - 1, -1):
                res.append(data[i][left])
            left += 1
        if up > down or left > right: return res
        direct = (direct + 1) % 4


def main():
    # data = [1, 2, 3, 4]
    # result = product_except_self(data)

    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = spiral_matrix(data)
    print(result)

if __name__ == '__main__':
    main()