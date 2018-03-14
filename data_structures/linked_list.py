class LinkedList:
    head = None

    def list_insert(self, node):
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        node.prev = None

    def list_search(self, key):
        x = self.head
        while x is not None and x.key != key:
            x = x.next
        return x

    def list_delete(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev

    def print(self):
        if self.head is None:
            print("List is empty")
        else:
            i = 1
            node = self.head
            while node is not None:
                # print(node.key)
                print("%s. %s" % (i, node.key))
                i += 1
                node = node.next

    class Node:
        prev = None
        next = None
        key = None

        def __init__(self, key, prev=None, next=None):
            self.key = key
            self.prev = prev
            self.next = next


def main():
    linked_list = LinkedList()
    linked_list.list_insert(LinkedList.Node(key=1))
    linked_list.list_insert(LinkedList.Node(key=2))
    linked_list.list_insert(LinkedList.Node(key=3))
    linked_list.print()

    node = linked_list.list_search(2)
    print(node.key)

    linked_list.list_delete(node)
    linked_list.print()


if __name__ == "__main__":
    main()
