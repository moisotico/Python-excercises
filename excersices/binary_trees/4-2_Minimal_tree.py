import math as mth


# binary tree node
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Create a tree from an array
def createTreeNodes(arr, remain):
    # Choose the root as the one stored in the index given
    # by the ceil of len/2 or zero if there is only 1 value left
    root_index = int(len(arr)/2) if len(arr) > 1 else 0
    root = Node(arr[root_index])
    remain -= 1
    if len(arr) > 1:
        if remain > 0:
            root.left, remain = createTreeNodes(arr[:root_index], remain)
        if remain > 0 and len(arr) > 2:
            root.right, remain = createTreeNodes(arr[root_index + 1:], remain)
    return root, remain


def CompHeight(elements, Node):
    result = CalcHeigth(Node)
    compare_val = minHeigth(elements)
    if result == compare_val:
        print("Success!", "Value:", result, " Expected:", compare_val)
        return
    print("Failure!", "Value:", result, " Expected:", compare_val)


def CalcHeigth(Node, level=0):
    heigth = level - 1
    if Node is not None:
        level += 1
        new_heigth = CalcHeigth(Node.left, level)
        if new_heigth > heigth:
            heigth = new_heigth
        new_heigth = CalcHeigth(Node.right, level)
        if new_heigth > heigth:
            heigth = new_heigth
    return heigth


# Compare minHeigth
def minHeigth(val):
    est_min_heigth = mth.floor(mth.log2(val))
    return est_min_heigth


# Print tree and return heigth method
def TreeResult(Node, level=0):
    if Node is not None:
        TreeResult(Node.left, level + 1)
        if level == 0:
            print(' ' * 4 * level + '*', Node.value)
        else:
            print(' ' * 4 * level + '-->', Node.value)
        TreeResult(Node.right, level + 1)


if __name__ == "__main__":
    # order array
    arr = [2, 3, 4, 5, 6, 9]
    print("Array:", arr)
    arr.sort()
    length = len(arr)
    root, val = createTreeNodes(arr, length)
    if val == 0:
        print("Tree:")
        TreeResult(root)
        CompHeight(length, root)
    # TODO : remove
    else:
        print("There was an error!")
