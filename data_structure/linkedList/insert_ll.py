"""
Link list
def _init_(self, val = 0, next = none) 
    self.val = val
    self.next = next
    
    1-2-3-4-5-null
    O(n)
    
    #Prob1: Insert into kth position of a linked list
    def insert(head,k,data)
    1-2-3-4-5-null k = 2 data = 10
    1-10-2-3-4-5-null
    1-2-3-4-5-6-null k = 7 data = 10
    Prob 2:
    Intersection of Two Linked Lists. Write a program to find the node at which the intersection of
two singly linked lists begins.
"""

def insert(head,k,data):
    
    count = 0
    
    if head == None:
        # case 1 - k == 0 
        if k == 0:
            return new Node(data)
        # case 2 k >0, return -1 
        else:
            return -1 
    else:
        cur_node = head
    
    ## Traversal and stop at the kth node 
    while count<k:
        if cur_node == None:
            return -1;
        count +=1
        cur_node = cur_node.next
        
        
    ## Save the next node
    next_node = cur_node.next
    
    ## Point the current node to data
    Node insert_node = new Node(data);
    cur_node.next = insert_node
    
    ## Point the new node to the next element
    insert_node.next = next_node

