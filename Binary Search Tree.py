# Binary Search Tree

# 1. Binary search tree
    # Binary search tree is a particular type of binary tree, where in any node, 
    # the left child of the node is always greater and the right
    # child is always smaller than the node


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return
        