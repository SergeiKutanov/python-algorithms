def get_data():
    return [
        10, 155, -10, 0, 3, -56, 4.5, 9
    ]


def do_sort(data):
    for i in range(0, len(data)):
        for j in range(len(data) - 1, i, -1):
            if data[j] < data[j - 1]:
                tmp = data[j]
                data[j] = data[j - 1]
                data[j - 1] = tmp


def main():
    data = get_data()
    print(data)
    do_sort(data)
    print(data)


if __name__ == "__main__":
    main()