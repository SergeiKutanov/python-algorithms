import math


def get_data():
    return [
        0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68
    ]


def run_bucket_sort(data):
    n = len(data)
    b = []
    for i in range(0, n):
        b.append([])
    for i in range(0, n):
        index = math.floor(n * data[i])
        b[index].append(data[i])
    for i in range(0, n):
        insertion_sort(b[i])
    result = []
    for bucket in b:
        result = result + bucket
    return result


def insertion_sort(data):
    for j in range(1, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i+1] = data[i]
            i = i-1
        data[i+1] = key


def main():
    data = get_data()
    sorted = run_bucket_sort(data)
    print(sorted)


if __name__ == '__main__':
    main()