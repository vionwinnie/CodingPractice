"""
Problem:  Detect and Remove a Loop in a Linked List1.

https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/

Clarify:  
Singly-linked list?  Yes.  
Doesn’t this seem like a bad idea?  Yes.
Handle empty list?  Yes.

2.Example (see other slide)
3.Algorithm:Floyd’s algorithm to detect presence/absence of a loop (use fast = 2 * slow)

Count the size of the loop (move fast while holding slow fixed)

Send fast “loopsize” nodes ahead of slow, then advance both until they meet

Blast the offending “next” pointer


12345->2
12345-> NULL

https://stackoverflow.com/questions/2936213/explain-how-finding-cycle-start-node-in-cycle-linked-list-work

"""

class Node:
    def __init__(self,val=0,next_node=None):
        self.val=val
        self.next_=next_node


## Create two lists
def create_linked_list(list_int):
    all_nodes = []
    head_node = Node(list_int[0])
    all_nodes.append(head_node)
    cur_node = head_node
    for i,cur_int in enumerate(list_int):
        if i >0:
            new_node = Node(cur_int)
            cur_node.next_ = new_node
            cur_node = new_node
            all_nodes.append(new_node)
    return all_nodes


list_a = create_linked_list([2,3,4,6,7,8,9])
list_a[-1].next_ = list_a[3]

cur_node = list_a[0]
count = 0
while count <15:
    print(cur_node.val)
    count +=1
    cur_node = cur_node.next_


## First Pass - find where turtle and hare meets
fast_pointer = list_a[0]
slow_pointer = list_a[0]

## Fast pointer reachs NULL
cond1 = fast_pointer.next_ is not None
## Slow pointer reachs NULL
cond2 = slow_pointer.next_ is not None
## Slow == Next
cond3 = False

while cond1 and cond2:
    if cond3:
        break
    fast_pointer = fast_pointer.next_.next_
    slow_pointer = slow_pointer.next_
    print("fast:{}".format(fast_pointer.val))
    print("slow:{}".format(slow_pointer.val))

    ## Fast pointer reachs NULL
    cond1 = fast_pointer.next_ is not None
    ## Slow pointer reachs NULL
    cond2 = slow_pointer.next_ is not None
    ## Slow == Fast
    cond3 = slow_pointer.next_ == fast_pointer.next_
    
## Check whether it is because no loop present or 
if not cond1 and not cond2:
    print("No Loop Present, Traversal is finished")
elif cond3:
    print("Turtle and Hare meet")

## Second Step - Find the beginning of the loop
slow_pointer = list_a[0]

cond3 = False

while True:
    print("slow",slow_pointer.val) 
    print("fast",fast_pointer.val)
    if slow_pointer.next_ == fast_pointer.next_:
        break
    slow_pointer = slow_pointer.next_
    fast_pointer = fast_pointer.next_

print("loop starts here",slow_pointer.next_.val)

## Third Step - Modify the last pointer to NULL
fast_pointer.next_ = None
print("Checking Travesals for loop detection")

cur_node = list_a[0]
while cur_node :
    print(cur_node.val)
    cur_node = cur_node.next_
