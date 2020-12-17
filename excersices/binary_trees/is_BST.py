# Importing dependancies
import sys


# A tree node
class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Print tree and return heigth method
def TreeResult(Node, level=0):
    if Node is not None:
        TreeResult(Node.left, level + 1)
        if level == 0:
            print(' ' * 4 * level + '*', Node.value)
        else:
            print(' ' * 4 * level + '-->', Node.value)
        TreeResult(Node.right, level + 1)


# A function to check if a binary tree is BST.
def isBST(node, mini, maxi):
    if node is None:
        return 1
    # Checking if a key is outside the permitted range.
    if node.value < mini:
        return 0
    if node.value > maxi:
        return 0
    # Sending in updates ranges to the right and left subtree
    return isBST(node.right, node.value, maxi) and \
        isBST(node.left, mini, node.value)


# Creating a BST
root = Tree(6)
root.left = Tree(3)
root.right = Tree(9)
root.left.left = Tree(1)
root.left.right = Tree(5)
root.right.left = Tree(7)
root.right.right = Tree(11)
# Passing in the word size of the machine
mini = -sys.maxsize - 1
maxi = sys.maxsize
TreeResult(root)
if(isBST(root, mini, maxi)):
    print("This binary tree is a BST.")
else:
    print("This binary tree is not a BST.")
