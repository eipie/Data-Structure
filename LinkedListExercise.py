class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        currentNode = self.head
        while currentNode.nextNode:
            currentNode = currentNode.nextNode
        currentNode.nextNode = newNode

    def printList(self):
        currentNode = self.head
        tempList = []   
        while currentNode:
            tempList.append(currentNode.data)
            currentNode = currentNode.nextNode
        print(tempList)

    def insert(self, prevNode, data):
        if not prevNode:
            return False
        newNode = Node(data)
        newNode.nextNode = prevNode.nextNode
        prevNode.nextNode = newNode


# Creating a linked list
a = LinkedList()

# MARK I
# Append 1, 3, 5, 6 in the linked list
a.append(1)
a.append(3)
a.append(5)
a.append(6)

# MARK II
# Insert 2 after 1
a.insert(a.head, 2)

# MARK III
# Delete 5
a.printList()
