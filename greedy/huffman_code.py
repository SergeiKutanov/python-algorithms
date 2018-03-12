import heapq


def build_huffman_code():
    data = get_freq_data()
    root = huffman(data)


def huffman(data):
    n = len(data)
    # min priority queue
    q = MyHeap(data)
    for letter in range(1, n):
        node = TreeNode()
        node.left = x = q.pop()
        node.right = y = q.pop()
        node.value = {
            'letter': None,
            'freq': x.value['freq'] + y.value['freq']
        }
        q.push(node)
    return q.pop()


def get_freq_data():
    return [
        TreeNode(value={'freq': 45, 'letter': 'a'}),
        TreeNode(value={'freq': 13, 'letter': 'b'}),
        TreeNode(value={'freq': 12, 'letter': 'c'}),
        TreeNode(value={'freq': 16, 'letter': 'd'}),
        TreeNode(value={'freq': 9, 'letter': 'e'}),
        TreeNode(value={'freq': 5, 'letter': 'f'})
    ]


class MyHeap(object):
    def __init__(self, initial=None, key=lambda x: x.value['freq']):
        self.key = key
        if initial:
            self._data = [(key(item), item) for item in initial]
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self._data)[1]


class TreeNode(object):
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value


def main():
    build_huffman_code()


if __name__ == "__main__":
    main()