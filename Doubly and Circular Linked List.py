class Node: # Node class for Doubly Linked List.
    def __init__(self , value = None): # Constructor to initialize the node with data and pointers.
        self.data = value # Data part of the node.
        self.next = None # Pointer to the next node.
        self.prev = None # Pointer to the previous node.

class DoublyLL: # Doubly Linked List Class
    def __init__(self):
        self.head = None # Initialize the head of the list to None.

    def insertAtEnd(self , value): # Method to insert a node at the end of the list
        temp = Node(value) # Create a new node with the given value
        if(self.head == None): # If the list is empty, set the new node as the head
            self.head = temp # Set the new node as the head of the list
            return # Exit the method after inserting the node
        
        t=self.head # Start from the head of the list
        while(t.next != None): # Traverse the list until the end
            t = t.next # Move to the next node
        
        t.next = temp # Set the next pointer of the last node to the new node.
        temp.prev =t # Set the previous pointer of the new node to the last node.

    def insertAtBeg(self , value): # Method to insert a node at the beginning of the list.
        temp=Node(value) # Create a new node with the given value
        if(self.head == None): # If the list is empty, set the new node as the head
            self.head = temp # Set the new node as the head of the list
            return # Exit the method after inserting the node
        temp.next = self.head # Set the next pointer of the new node to the current head 
        self.head.prev = temp # Set the previous pointer of the current head to the new node
        self.head = temp # Set the new node as the head of the list    

    def insertAtMid(self,value,x): # Method to insert a node at a specific position in the list
        t=self.head # Start from the head of the list

        #SEARCHING CODE(upto line 41)
        while(t.next != None): # Traverse the list until the end
            if(t.data == x): # If the current node's data matches the given value x
                break # Exit the loop to insert the new node at this position
            else:
                t = t.next # Move to the next node


        temp=Node(value) # Create a new node with the given value
        temp.next = t.next # Set the next pointer of the new node to the next node of the current node
        t.next.prev = temp # Set the previous pointer of the next node to the new node
        t.next = temp # Set the next pointer of the current node to the new node
        temp.prev = t # Set the previous pointer of the new node to the current node


    def printDLL(self):
        t1=self.head # t1 is a temporary pointer to traverse the linked list
        
        while(t1.next!=None): # traverse the linked list until the last node is reached 
            print(t1.data , end = " <--> ") # print the data part of the current node
            
            t1=t1.next # move the temporary pointer to the next node
        
        print(t1.data) # print the data part of the last node

    def deletionDLL(self,value): # Method to delete a node with a specific value from the list
        if(self.head == None): # If the list is empty, print a message and return
            print("Linked List is empty") # Print a message indicating that the list is empty
            return # Exit the method 

        t=self.head # Start from the head of the list

        if(t.data == value): # If the head node's data matches the given value
            self.head = t.next # Set the head to the next node
            self.head.prev = None # Set the previous pointer of the new head to None

        while(t.next != None): # Traverse the list until the end

            if(t.data == value): # If the current node's data matches the given value
                t.prev.next = t.next # Set the next pointer of the previous node to the next node
                t.next.prev = t.prev # Set the previous pointer of the next node to the previous node
                return # Exit the method after deleting the node
            
        if (t.data == value): # If the last node's data matches the given value
            t.prev.next = None # Set the next pointer of the previous node to None
            
obj = DoublyLL() # Create an object of the DoublyLL class

obj.insertAtEnd(10) # Insert a node with value 10 at the end of the list

obj.insertAtEnd(20) # Insert a node with value 20 at the end of the list

obj.insertAtEnd(30) # Insert a node with value 30 at the end of the list

obj.insertAtEnd(40) # Insert a node with value 40 at the end of the list

obj.insertAtBeg(5) # Insert a node with value 5 at the beginning of the list

obj.insertAtMid(50,20) # Insert a node with value 25 after the node with value 20

obj.deletionDLL(5) # Delete the node with value 30 from the list

obj.printDLL() # Print the elements of the list
