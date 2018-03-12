
def main():
    run_activity_selection_recursive()


def activity_selection_iterative(index, data):
    length = len(data)
    result = [data[index]]
    k = 0
    for m in (range(1, length)):
        if data[m][0] >= data[k][1]:
            result.append(data[m])
            k = m
    return result


def activity_selection_recursive(index, data):
    m = index + 1
    while m < len(data) and data[m][0] < data[index][1]:
        m = m + 1
    if m < len(data):
        res = activity_selection_recursive(m, data)
        if res:
            return [data[m]] + activity_selection_recursive(m, data)
        else:
            return [data[m]]
    else:
        return []


def run_activity_selection_recursive():
    data = [
        [1, 4],
        [3, 5],
        [0, 6],
        [5, 7],
        [3, 9],
        [5, 9],
        [6, 10],
        [8, 11],
        [8, 12],
        [2, 14],
        [12, 16]
    ]

    init_key = 0
    result_recursive = [data[init_key]] + activity_selection_recursive(init_key, data)
    result_iterative = activity_selection_iterative(init_key, data)
    print(result_recursive)
    print(result_iterative)


if __name__ == "__main__":
    main()
