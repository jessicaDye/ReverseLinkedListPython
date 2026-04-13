#Jessica Dye, CIS 490*
# Do a Doubly linked list A-->B-->C
# Flip linked list to C-->B-->A


class Node:
    def __init__(self): #constructor
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self): #constructor
        self.head = None

    def __str__(self): #do not allow print of the linked list to print the memory ID
        s = 'data: ' + str(self.data) + "\n"
        s += 'next:' + str(self.next) + "\n"
        return s
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.head)
            current_node = current_node.next


# Test 
#A->B->C
n1 = Node()
n1.data = 'A'
n2 = Node()
n2.data = 'B'
n3 = Node()
n3.data = 'C'

print(n1.data) #A
print(n2.data) #B
print(n3.data) #C

