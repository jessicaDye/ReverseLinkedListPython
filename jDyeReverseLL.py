#Jessica Dye, CIS 490*
# Do a Doubly linked list A-->B-->C
# Flip linked list to C-->B-->A


class Node:
    def __init__(self, d): #constructor
        self.data = d
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.data)

  

class LinkedList:
    def __init__(self): #constructor
        self.head = None
        self.tail = None


    
    def addNodeAtHead(self, d): #creates a new node and adds to head
        new_node = Node(d)

        if self.head is not None:
            self.head.prev = new_node

        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def __str__(self): 
        cur_node = self.head
        s = ""
    
        while cur_node:
            s += str(cur_node.data) + " -> "
            cur_node = cur_node.next
    
        return s + "None"
     
    # Print the linked list in reverse order
    
    def print_reverse(self):
        current_node = self.tail        
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.prev  
        print("None")
    

# Test 
#A->B->C
n1 = Node('A')
#n1.data = 'A'
n2 = Node('B')
#n2.data = 'B'
n3 = Node('C')
#n3.data = 'C'

print(n1.data) #A
print(n2.data) #B
print(n3.data) #C

# Test Linked List class
ll = LinkedList()
ll.addNodeAtHead('C')
ll.addNodeAtHead('B')
ll.addNodeAtHead('A')
print(ll) #output should be A->B->C

## Reverse ll -> return a new doubly linked list in which all elements are reversed.
ll2 = LinkedList() 
ll2.addNodeAtHead('C')
ll2.addNodeAtHead('B')
ll2.addNodeAtHead('A')
ll2.print_reverse() #output should be C->B->A
