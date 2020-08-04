# Binary Tree

# Building a binary search tree
# Every node of the binary tree is an object, which has a few attribtes:
    # The key
    # The data: can be any kind of data type, including strings and doubles
    # left: the left child of the node, if the node does not have a left child, then the attribute will be null
    # right: the right child of the node, if the node does not have a right child, then the attribute will be null
    # pointer: that points to the nodes corresponding to its left child, right child and parent

# Binary Tree Traveral
# Inorder tree walk: left child, root, then right child
# Preorder tree walk: root, left child, then right child
# Postorder tree walk: left child, right child, then root

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
arr = [i for i in range (1,6)]
for a in arr:
    newTree.add(a)
newTree.breadthTraveral()


            

        

