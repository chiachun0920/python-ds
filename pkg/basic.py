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

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.next
        return count

    def search(self, value):
        current = self.head
        while current != None:
            if current.data == value:
                return True
            current = current.next
        return False

    def remove(self, value):
        previous = None
        current = self.head
        while current != None:
            if current.data == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
