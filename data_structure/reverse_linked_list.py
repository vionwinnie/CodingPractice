class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

def create_slist(vals):
    assert type(vals)==list

    ## Initialize an instance of Single-linked list
    list1 = SLinkedList()

    ## Add the head node to the list
    cur_node = None
    for i,val in enumerate(vals):
        if i == 0:
            list1.headval = Node(val)
            cur_node = list1.headval
        else:
            tmp = Node(val)
            cur_node.nextval = tmp
            cur_node = tmp
    return list1

# a -> b -> c -> d
# d -> c -> b -> a
## Reverse Linked List
def reverse(slist):
    cur_node = slist.headval
    node_list = []

    while cur_node.nextval != None:
        prev_node = cur_node
        cur_node = cur_node.nextval
        node_list.append(cur_node)

    node_list.reverse()

    ## After reaching the end:
    #1. Instantiate an instance of a linked list
    new_slist = SLinkedList()
    
    #2. Set the head to be the last node
    new_slist.headval = cur_node
    
    for i,node in enumerate(node_list):
        if i >0:
            cur_node.nextval = node
            cur_node = node

    return new_slist

def check_slist(slist):
    vals = []

    cur_node = slist.headval
    while cur_node.nextval != None:
        vals.append(cur_node.dataval)
        cur_node = cur_node.nextval
    return vals

def run_all(vals):
    og_list = create_slist(vals)
    new_list = reverse(og_list)
    final_vals = check_slist(new_list)

    return final_vals

def test_answer():
    assert run_all([1,2,3])== [3,2,1]
    assert run_all(['apple','boy','cat','dog','elephant','pooh','zebra']) == ['zebra','pooh','elephant','dog','cat','boy','apple']


