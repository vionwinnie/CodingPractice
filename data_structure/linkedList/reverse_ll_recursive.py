class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def traverse(self):
        ## return the last node
        cur_node = self.headval
        while cur_node.nextval != None:
            next_node = cur_node.nextval
            cur_node = next_node
        return cur_node

    def append(self,val):
        ## Set the first element
        if self.headval == None:
            self.headval = Node(val)
        else:
            last_node = self.traverse()
            last_node.nextval = Node(val)

    def print_val(self):
        all_val = []
        cur_node = self.headval
        all_val.append(cur_node.dataval)
        while cur_node.nextval != None:
            next_node = cur_node.nextval
            all_val.append(next_node.dataval)
            cur_node = next_node
        print(all_val)

    def reverse_utils(self,prev,cur):
        
        next_ = cur.nextval
        ## a->b -> c --> c -> b -> a
        cur.nextval = prev
        
        if next_ == None:
            ## Setting the head pointer
            self.headval = cur
            return
        else:
            self.reverse_utils(cur,next_)

    def reverse(self):
        if self.headval == None:
            print("this is an empty list")
        else:
            prev = None
            cur = self.headval
            self.reverse_utils(prev,cur)

list1 = SLinkedList()
vals = ['a','b','c']
for val in vals:
    list1.append(val)
list1.print_val()
list1.reverse()
list1.print_val()


list2 = SLinkedList()
vals2 = [4,5,6,7]
for val in vals2:
    list2.append(val)

list2.print_val()
list2.reverse()
list2.print_val()
