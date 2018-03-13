def get_data():
    return [5,9,1,0,3,5,12,56,-5,-1]


def main():
    data = get_data()
    print(data)
    insertion_sort(data)
    print(data)


def insertion_sort(data):
    for j in range(1, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i+1] = data[i]
            i = i-1
        data[i+1] = key


if __name__ == "__main__":
    main()