def partition(data, start, end):
    x = data[end]
    i = start - 1
    for j in range(start, end):
        if data[j] <= x:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[end] = data[end], data[i + 1]
    return i + 1


def quicksort(data, start, end):
    if start < end:
        q = partition(data, start, end)
        quicksort(data, start, q - 1)
        quicksort(data, q + 1, end)


def get_data():
    return [
        2, 8, 7, 1, 3, 5, 6, 4
    ]


def main():
    data = get_data()
    print(data)
    quicksort(data, 0, len(data) - 1)
    print(data)


if __name__ == "__main__":
    main()