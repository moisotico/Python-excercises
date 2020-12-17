# Represents the node of list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CreateList:
    # Declaring head pointer as null.
    def __init__(self):
        self.tail = Node(None)
        self.head = Node(None)

    # method to add element to linked list
    def add(self, data):
        newNode = Node(data)
        # check if list is empty
        if self.tail.next is None:
            self.head = newNode
            self.tail.next = self.head
        else:
            self.head.next = newNode
            self.head = self.head.next

    def getMax(self, max_val=0):
        node = self.tail.next
        while node is not None:
            if node.data > max_val:
                max_val = node.data
            node = node.next
        return max_val

    def getMin(self, min_val=None):
        node = self.tail.next
        if node.data is not None:
            min_val = node.data
        while node is not None:
            if node.data < min_val:
                min_val = node.data
            node = node.next
        return min_val


if __name__ == "__main__":
    list = CreateList()
    list.add(7)
    list.add(5)
    list.add(9)
    list.add(2)
    max_val = list.getMax()
    min_val = list.getMin()
    print(max_val, min_val)
