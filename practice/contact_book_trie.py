import unittest


class Node:
    def __init__(self):
        self.count = 0
        self.children = {}
        self.value = None


class ContactBook:

    def __init__(self):
        self.root = Node()

    def add_contact(self, contact):
        node = self.root
        node.count += 1
        i = 0
        while i < len(contact):
            if contact[i] in node.children:
                node = node.children[contact[i]]
                node.count += 1
                i += 1
            else:
                break
        while i < len(contact):
            node.children[contact[i]] = Node()
            node = node.children[contact[i]]
            node.count += 1
            i += 1
        node.value = contact

    def search(self, query):
        node = self.root
        for ch in query:
            if ch in node.children:
                node = node.children[ch]
            else:
                return 0

        return node.count

    def look_for_leafs(self, node, counter):
        if node.value:
            counter[0] += 1
        for child in node.children:
            self.look_for_leafs(node.children[child], counter)


class TestContactBook(unittest.TestCase):
    def test(self):
        cb = ContactBook()
        cb.add_contact('hack')
        cb.add_contact('hackerrank')
        f = cb.search('hac')
        self.assertEqual(2, f)
        f = cb.search('hak')
        self.assertEqual(0, f)


class ContactBookCounter:
    def __init__(self):
        self.counter = {}

    def add(self, contact):
        i = 1
        while i < (len(contact) + 1):
            if contact[:i] in self.counter:
                self.counter[contact[:i]] += 1
            else:
                self.counter[contact[:i]] = 1
            i += 1

    def search(self, query):
        if query in self.counter:
            return self.counter[query]
        else:
            return 0


class TestContactBookCounter(unittest.TestCase):
    def test(self):
        cb = ContactBookCounter()
        cb.add('hack')
        cb.add('hackerrank')
        f = cb.search('hac')
        self.assertEqual(2, f)
        f = cb.search('hak')
        self.assertEqual(0, f)


if __name__ == '__main__':
    unittest.main()