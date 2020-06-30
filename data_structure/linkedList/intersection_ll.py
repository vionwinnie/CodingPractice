"""
Check intersection of two list

1. Traverse both list
2. Find length of both
3. Start with the pointer with the shorter length and move together, and compare pointer to pointer
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

list_a = create_linked_list([1,2,3,4,5,7,8])
list_b = create_linked_list([9,2,10])

list_b.extend(list_a[4:])
list_b[2].next_=list_b[3]
print('length A:{}'.format(len(list_a)))
print('length B:{}'.format(len(list_b)))
assert list_a[4] ==list_b[3]

## Traverse both lists
def traverse(head_node):
 #   print('traverse now')
    if type(head_node)== Node:
        count = 1
        cur_node = head_node
        while cur_node.next_ != None:
 #           print(cur_node.val)
            cur_node = cur_node.next_
            count +=1
 #       print(cur_node.val)
        return count
    else:
        return 0
    
def find_intersection(list_a,list_b):
    len_a = traverse(list_a[0])
    len_b = traverse(list_b[0])
    
    if len_a ==0 or len_b ==0:
        print("one list is empty")
        return []
    else:
        diff = len_a-len_b
        if diff >=0:
            print(' A>B')
            cur_a_node = list_a[diff]
            cur_b_node = list_b[0]
        else:
            print('B > A')
            cur_a_node = list_a[0]
            cur_b_node = list_b[abs(diff)]
        
        common_node = []
        
        while cur_a_node and cur_b_node:
            check = cur_a_node ==cur_b_node
            if check:
                common_node.append(cur_a_node)
            cur_a_node = cur_a_node.next_
            cur_b_node = cur_b_node.next_
        
        print("Number of common nodes:{}".format(len(common_node)))
        
        for node in common_node:
            print(node.val)
        
        return common_node
    
## Test Cases

# len(List A) > len(List B)
print("Case 1")
common_node = find_intersection(list_a,list_b)

# len(List B) > len(List C)
print("Case 2")
list_c = list_a
common_node_2 = find_intersection(list_b,list_c)

# One list is None
print("Case 3")
common_node_3 = find_intersection([None],list_a)

# Both list is None
print("Case 4")
common_node_4 = find_intersection([None],[None])

# None intersection
print("Case 5")
list_d = create_linked_list([20,22,24,28])
common_node_5 = find_intersection(list_a,list_d)

