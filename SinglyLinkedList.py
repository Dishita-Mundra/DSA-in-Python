# jab array ke ander memory ka allocation hota h vo contigous hota h
# LinkedList hume ek option provide kar sakta h kya ki hum runtime p memory allocation kar sakte h
# agar program chal rha hota h toh uss time if we need memory to store data so we can add in memory in runtime


# linkedList = hum normally ek block allocate karate h jisko NODE bola jata h
# then node ke do part hote h
# 1.isme information store hoti h  [ zaruri nhi ki value store karo ek objject bhi store kar sakte h jisme ki mainly sari information hoti h ]
# 2.isme hota h next wali memory ka address
# [i love u dishita]
# Pointer = it is a variable which points to a position / an address
# jaise blaock ke ander do partition h toh hum likhenge ki jaise plhe wale box ko humne Head bol diya jo ki define kar rha h ki humne plhe wale dubbe ki location ki toh hum likhenege ki Head.info  ya fir Head.next .


# SINGLYLINKEDLIST CODE

class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def InsertAtEnd(self, value):
        temp = Node(30)
        if 