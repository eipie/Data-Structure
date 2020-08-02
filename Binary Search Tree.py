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

class Node:
    def __init___(self, key, data, left, right, pointer):
        self.key = key
        self.data = data
        self.left = null
        self.right = null
        self.pointer = null

    # Inorder tree walk psedocode
    def inorderTreeWalk(self):
        if self is not null:
            inorderTreeWalk(self.left)
            print(self.key)
            inorderTreeWalk(self.right)

    # Tree search psedocode (with recursion)
    def treeSearch(self, k):
        if self.data is null or k == self.key:
            return self.data
        if k < x.key:
            return treeSearch(self.left, k)
        else:
            return treeSearch(self.right, k)

    # Tree search psedocode (with iteration)
    def treeSearchV2(self, k):
        while self.data is not null and k != self.key:
            if k < self.key:
                self.data = self.data.left
            else:
                self.data = self.data.right
        return self.data

    # Finding the max psedocode
    def Max(self):
        currNode = self.data
        while currNode is not null:
            currNode = self.data.left
        return currNode
    
    # Finding the min psedecode
    def Min(self):
        currNode = self.data
        while currNode is not null:
            currNode = self.data.right
        return currNode

    def Min(self):
        currNode = self.data
        while currNode is not null:
            currNode = self.data.left
        return currNode
    
    def findSuccessor(self):
        if self.right is null:
            return Min(self.right)


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



