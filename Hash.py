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
        i = data % slots
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

    def search(self):
        return

    def delete(self):
        return 
    


        