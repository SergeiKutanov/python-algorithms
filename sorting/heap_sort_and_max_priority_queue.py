def get_data():
    return [
        4, 1, 3, 2, 16, 9, 10, 14, 8, 7
    ]


def max_heapify(data, heap_size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < heap_size and data[left] > data[i]:
        largest = left
    if right < heap_size and data[right] > data[largest]:
        largest = right
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        max_heapify(data, heap_size, largest)


def heap_sort(data):

    heap_size = len(data)

    # build max heap
    for i in range(heap_size, -1, -1):
        max_heapify(data, heap_size, i)

    print("Max heap", data)

    # extract elements
    for i in range(heap_size - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        max_heapify(data, i, 0)


def heap_max(data):
    return data[0]


def heap_extract_max(data):
    if len(data) < 1:
        raise Exception("heap underflow")
    max = data[0]
    data.remove(max)
    max_heapify(data, len(data), 0)
    return max


def heap_increase_key(data, i, key):
    if key < data[i]:
        raise Exception("New key is smaller than current key")
    data[i] = key
    while i > 0 and data[((i + 1) // 2) - 1] < data[i]:
        data[i], data[((i + 1) // 2) - 1] = data[((i + 1) // 2) - 1], data[i]
        i = ((i + 1) // 2) - 1


def max_heap_insert(data, key):
    data.append(key)
    heap_increase_key(data, len(data) - 1, key)


def main():
    data = get_data()
    print(data)
    heap_sort(data)
    print(data)


if __name__ == "__main__":
    main()
