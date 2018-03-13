import math


def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[mid:]
        right = data[:mid]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        # merging
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i = i + 1
            else:
                data[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            data[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            data[k] = right[j]
            j = j + 1
            k = k + 1


def get_data():
    return [
        5,2,4,7,1,3,2,6, -10
    ]


def main():
    data = get_data()
    print(data)
    merge_sort(data)
    print(data)


if __name__ == "__main__":
    main()