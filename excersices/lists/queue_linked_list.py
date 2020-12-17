# Represents the node of list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CreateList:
    # Declaring tle pointer as null.
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

    # method to add element to linked list queue
    def add(self, data):
        newNode = Node(data)
        # check if list is empty
        if self.head.next is None:
            self.tail = newNode
            self.head.next = self.tail
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

    # method to add element to linked list queue
    def remove(self):
        # pop head element
        if self.head is not None:
            self.head = self.head.next

    # show list from the top
    def peek(self):
        node = self.head.next
        while node is not None:
            print(node.data)
            node = node.next

    # show list from the top
    def isEmpty(self):
        if self.head.next is None:
            print("The queue is empty!")
        else:
            print("The queue is not empty")


if __name__ == "__main__":
    list = CreateList()
    list.add(7)
    list.add(5)
    list.add(9)
    list.add(2)
    list.remove()
    list.remove()
    list.remove()
    list.remove()
    list.peek()
    list.isEmpty()
