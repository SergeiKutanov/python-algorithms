class Stack:
    _top = -1
    _data = []

    def is_empty(self):
        if self._top == -1:
            return True
        else:
            return False

    def push(self, el):
        self._top += 1
        self._data.append(el)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow")
        else:
            self._top -= 1
            el = self._data[self._top + 1]
            self._data.remove(el)
            return el


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


if __name__ == "__main__":
    main()
