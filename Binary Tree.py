# Binary Search Tree

# Building a binary search tree
# Every node of the binary tree is an object, which has a few attribtes:
    # The key
    # The data: can be any kind of data type, including strings and doubles
    # left: the left child of the node, if the node does not have a left child, then the attribute will be null
    # right: the right child of the node, if the node does not have a right child, then the attribute will be null
    # pointer: that points to the nodes corresponding to its left child, right child and parent

# Binary Search Tree Property
    # Let x be a node in a binary search tree. If y is a node in the left subtree
    # of x, then y.key <= x,key. If y is a node in the right subtree of x, then
    # y.key >= x.key

# Binary Search Tree Traveral
# Inorder tree walk: prints the key of the root of a subtree between printing the values in its left subtree 
#                    and printing those in its right subtree.
# Preorder tree walk: prints the root before the values in either subtree
# Postorder tree walk: prints the root after the values in its subtrees

# Binary Search Tree Query
# Search Algorithm
    # Given the a pointer to the root of the tree and a key k, tree-search
    # returns a pointer to a node with key k if one exists; otherwise, it returns NIL.
    # Time Complexity: O(n)

# Finding Maximum and Minimum Algorithm
    # A pair of symmetric algorithm that starts from the root and constantly looking for the left/right child until it's null
    # Time Complexity: O(n)

# Successor and Predessor
    # The successor of a node is the node with the smallest key greater than the node's key

# Insertion and deletion

# -------------------------------------------------------------------------------------------------------------
# Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def add(self, item):
        newNode = Node(item)
        if self.root is None:
            self.root = newNode
            return 
        queue = [self.root]
        while len(queue) != 0:
            currentNode = queue.pop(0)
            if currentNode.left is None:
                currentNode.left = newNode
                return
            else:
                queue.append(currentNode.left)
            if currentNode.right is None:
                currentNode.right = newNode
                return
            else:
                queue.append(currentNode.right)

    def breadthTraveral(self):
        if self.root is None:
            return 
        queue = [self.root]
        while queue:
            currentNode = queue.pop(0)
            print(currentNode.data)
            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)

newTree = Tree()
newTree.add(1)
newTree.add(2)
newTree.add(3)
newTree.add(4)
newTree.add(5)
newTree.add(6)
newTree.breadthTraveral()


            

        

