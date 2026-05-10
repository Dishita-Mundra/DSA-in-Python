class Node:
    # constructor
    # info is the data part of the node and next is the pointer to the next node.
    # next is set to None by default
    # when a new node is created, the data part is set to info and the next pointer is set to next
    # if next is not provided, it will be set to None
    
    def __init__(self,info,next=None):
        self.data=info
        self.next=next

class SinglyLinkedlist:
        # constructor
        # head is the pointer to the first node of the linked list
        # when a new linked list is created, the head is set to None
    
    def __init__(self,head=None):
            self.head=head
        # method to add a new node at the end of the linked list
    
    def insertAtEnd(self,value): # value is the data part of the new node to be added
            temp=Node(value) # create a new node with the given value and next pointer set to None
            
            if(self.head!=None): # if the linked list is not empty, traverse the linked list to find the last node and set its next pointer to the new node
                t1=self.head # t1 is a temporary pointer to traverse the linked list
                
                while(t1.next!=None): # traverse the linked list until the last node is reached
                    t1=t1.next # move the temporary pointer to the next node
                t1.next=temp # set the next pointer of the last node to the new node
            
            else:
                self.head=temp # if the linked list is empty, set the head pointer to the new node
    
    def insertAtBeg(self,value):
         temp=Node(value) # create a new node with the given value and next pointer set to None
         temp.next=self.head # set the next pointer of the new node to the current head of the linked list
         self.head=temp # set the head pointer to the new node

    def insertInMid(self,value,x):
         temp=Node(value) # create a new node with the given value and next pointer set to None
         t1=self.head # t1 is a temporary pointer to traverse the linked list
         while(t1.next!=None): # traverse the linked list until a node with data part equal to x is found
             if(t1.data==x): # if a node with data part equal to x is found, set the next pointer of the new node to the next pointer of the current node and set the next pointer of the current node to the new node
                 temp.next=t1.next
                 t1.next=temp
             t1=t1.next # move the temporary pointer to the next node

    def deleteLL(self,value):
         t1=self.head # t1 is a temporary pointer to traverse the linked list
         prev=t1 # prev is a pointer to keep track of the previous node while traversing the linked list
         if(t1.data==value): # if the head node has data part equal to value, set the head pointer to the next node and delete the head node
              self.head=t1.next
         else:
            while(t1.next!=None): # traverse the linked list until a node with data part equal to value is found
                if(t1.data==value): # if a node with data part equal to value is found, set the next pointer of the previous node to the next pointer of the current node and delete the current node
                    prev.next=t1.next
                    break # exit the loop after deleting the node
                else:
                    prev=t1 # move the previous pointer to the current node
                    t1=t1.next # move the temporary pointer to the next node
            if(t1.data==value): # if the last node has data part equal to value, set the next pointer of the previous node to None and delete the last node
                prev.next=None
              

             
             
    def printLL(self): # method to print the linked list
        t1=self.head # t1 is a temporary pointer to traverse the linked list
        
        while(t1.next!=None): # traverse the linked list until the last node is reached
            print(t1.data) # print the data part of the current node
            
            t1=t1.next # move the temporary pointer to the next node
        
        print(t1.data) # print the data part of the last node

obj = SinglyLinkedlist() # call the constructor to create a new linked list object

obj.insertAtEnd(10) # add a new node with value 10 at the end of the linked list

obj.insertAtEnd(20) # add a new node with value 20 at the end of the linked list

obj.insertAtEnd(30) # add a new node with value 30 at the end of the linked list

obj.insertAtBeg(5) # add a new node with value 5 at the beginning of the linked list

obj.insertInMid(40,20) # add a new node with value 15 after the node with value 20

obj.deleteLL(30) # delete the node with value 30 from the linked list

obj.printLL() # print the linked list 

