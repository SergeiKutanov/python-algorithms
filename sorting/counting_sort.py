def get_data():
    return [
        2, 5, 3, 0, 2, 3, 0, 3
    ], [None] * 8, 5


def counting_sort(data, sorted_data, max_value):
    c = [0] * (max_value + 1)
    for j in range(0, len(data)):
        c[data[j]] = c[data[j]] + 1
    for i in range(1, max_value + 1):
        c[i] = c[i] + c[i - 1]
    for j in range(len(data) - 1, -1, -1):
        sorted_data[c[data[j]] - 1] = data[j]
        c[data[j]] = c[data[j]] - 1


def main():
    data, sorted_data, max_value = get_data()
    print(data)
    counting_sort(data, sorted_data, max_value)
    print(sorted_data)


if __name__ == "__main__":
    main()