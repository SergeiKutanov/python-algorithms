class Queue:
    _tail = 0
    _head = 0
    _data = []

    def is_empty(self):
        return self._head == self._tail

    def enqueue(self, el):
        if len(self._data) > 0:
            self._data.append(0)
            for k in range(len(self._data) - 2, -1, -1):
                self._data[k + 1] = self._data[k]
            self._data[0] = el
        else:
            self._data.append(el)

    def dequeue(self):
        return self._data.pop()


def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())


if __name__ == "__main__":
    main()
