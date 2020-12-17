# Represents the node of list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CreateList:
    # Declaring head pointer as null.
    def __init__(self):
        self.head = Node(None)

    # method to add element to linked list
    def add(self, data):
        newNode = Node(data)
        # check if list is empty
        if self.head.data is not None:
            self.tail.next = newNode
            self.tail = newNode
            self.tail


if __name__ == "__main__":
    list = CreateList()
    list.add(7)
    list.add(5)
    list.add(9)
    list.add(2)
