# AVL Tree
# 1. Balanced 
#     - Binary search trees support insert, delete, min, max, next_Large and next_Smaller
#     in O(h) time, where h is the height of the tree 
#     - h is between log(n) and n
#     - Balanced BST maintains h = O(log(n)) => all operations run at O(log(n)) time

# 2. AVL trees
#     - for every node, require heights of left and right children to differ by at most +- 1
#     - treat nill tree as height -1
#     - each node stores its height

import BST

def height(node):
    if node is None:
        return -1
    else:
        return node.height

def updateHeight(node):
    return max(height(node.left), height(node.right)) + 1

class AVL(BST.BST):
    def leftRotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        updateHeight(x)
        updateHeight(y)

    def rightRotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        updateHeight(x)
        updateHeight(y)

    def rebalance(self, node):
        while node is not None:
            updateHeight(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.rightRotate(node)
                else:
                    self.leftRotate(node.left)
                    self.rightRotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.leftRotate(node)
                else:
                    self.rightRotate(node.right)
                    self.leftRotate(node)
            node = node.parent

    def insert(self, k):
        node = super(AVL, self).insert(k)
        self.rebalance(node)

    def delete(self, k):
        node = super(AVL, self).delete(k)
        self.rebalance(node.parent)
