## Design a queue using an array
    # Using list structure to imitate a queue

## Find maximum in a stack
import queue

q = queue.LifoQueue(maxsize=6) 
from queue import Queue 
#q = Queue(maxsize = 5) 
# Adding of element to queue
q.put(10)
q.put(30)
q.put(1000)
q.put(1)

count = 0
while not q.empty():
    if count ==0:
        max_val = q.get()
    else:
        max_val = max(max_val,q.get())
    count +=1

print(max_val)

## Implement a stack with two queues
https://stackoverflow.com/questions/688276/implement-stack-using-two-queues

## Reverse a stack
 # get size - recurse to swap
 #4,3,2,1

