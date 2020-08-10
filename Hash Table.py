# Hash Table Implementation
# Implementation 1: using object-oriented programming

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set(self, newNode):
        self.next = newNode

    def get(self):
        return self.data

    def getNext(self):
        return self.next

class Hash:
    def __init__(self, slots):
        self.table = [None] * slots
        self.slots = slots 

    def insert(self, data):
        i = data % self.slots
        newNode = Node(data)
        if self.table[i] is None:
            self.table[i] = newNode
            return True
        else:
            head = self.table[i]
            while head.getNext() is not None:
                head = head.getNext()
            head.set_next(newNode)
            return True 

    def search(self, data):
        i = data % self.slots
        if self.table[i] is None:
            return False
        else:
            currentNode = self.table[i]
            while currentNode is not None:
                if currentNode.get() == data:
                    return True
                else:
                    currentNode = currentNode.getNext()
        return False

    def delete(self, data):
        if self.search(data) == False:
            return False
        else:
            i = data % self.slots
            currentNode = self.table[i]
            while currentNode is not None:
                if currentNode.get() == data:
                    currentNode.data = None
                    print("Item " + str(data) + " has been deleted")
                    return True
                else:
                    currentNode = currentNode.getNext()
        
# Testing
# Creating a new hash table
newTable = Hash(10)

# Insert a new data into the hash table
newTable.insert(25)

# Search an inserted data in the table
print(newTable.search(25))

# Search an uninserted data in the table
print(newTable.search(10))

# Delete a node from the table
newTable.delete(25)

# Search the deleted node
print(newTable.search(25))
