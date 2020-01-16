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

    def remove(self, value):
        start = self.head
        previous = None
        found = False
        while not found:
            if start.getData() == value:
                found = True
            else:
                previous = start
                start = start.getNextNode()
        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setLink(start.getNextNode())
        return found
    
    def findMax(self):
        currentNode = self.head
        currentMax = self.head.data
        if currentNode.nextNode is None:
            return currentNode.data
        while currentNode is not None:
            if currentNode.data > currentMax:
                currentMax = currentNode.data
            currentNode = currentNode.nextNode
        return currentMax
    
    def findMin(self):
        currentNode = self.head
        currentMin = self.head.data
        if currentNode.nextNode is None:
            return currentNode.data
        while currentNode is not None:
            if currentNode.data < currentMin:
                currentMin = currentNode.data
            currentNode = currentNode.nextNode
        return currentMin

    def len(self):
        if self.head is None:
            return 0
        length = 0
        currentNode = self.head
        while currentNode is not None:
            currentNode = currentNode.nextNode
            length += 1
        return length

# a = LinkedList()
# a.append(-4) 
# a.append(7) 
# a.append(14) 
# a.append(67) 
# a.append(20) 



