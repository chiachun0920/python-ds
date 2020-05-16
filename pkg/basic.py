class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
