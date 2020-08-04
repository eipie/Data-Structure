# Binary Search Tree

# 1. Binary search tree
    # Binary search tree is a particular type of binary tree, where in any node, 
    # the left child of the node is always greater and the right
    # child is always smaller than the node

# Binary Search Tree Property
    # Let x be a node in a binary search tree. If y is a node in the left subtree
    # of x, then y.key <= x,key. If y is a node in the right subtree of x, then
    # y.key >= x.key

# Successor and Predessor
    # The successor of a node is the node with the smallest key greater than the node's key

# 2. Binary search tree algorithms
# Finding Maximum and Minimum Algorithm
    # A pair of symmetric algorithm that starts from the root and constantly looking for the left/right child until it's null
    # Time Complexity: O(n)
# Insert a node into the binary tree algorithm
    # 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, currentNode):
        if data < currentNode.data:
            if currentNode.left is None:
                currentNode.left = Node(data)
            else:
                self._insert(data, currentNode.left)
        if data > currentNode.data:
            if currentNode.right is None:
                currentNode.right = Node(data)
            else:
                self._insert(data, currentNode.right)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
        
    def _print_tree(self, currentNode):
        if currentNode is not None:
            self._print_tree(currentNode.left)
            print(str(currentNode.data))
            self._print_tree(currentNode.right)
        
newTree = BinarySearchTree()
arr = [33, 1, 45]
for a in arr:
    newTree.insert(a)






        