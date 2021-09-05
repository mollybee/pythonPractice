#       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ QUEUES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Once we know how using Linked Lists works, that's great for building Queues
# 
# There is a specific way (first-in-first-out) for inserting and deleting data from the queue data structure. You enter the data
#   through the back, and exit through the front.
# Order is important when organizaing your data, so what are good data structures we can use to build a queue?
#       - Array? Yep - delete (pop() from the front), insert(append() to the back)
#           - But there's an issue here: it's an 0(n) algorithm; if you pop two off, then the data shifts. It's costly to keep order
#               with the shifting array
#       -Linked List? Even Better! - the front is the 'head' of the LL, 'tail' is the back. You have to add(insert) to the tail (adding a node
#               to the end of a LL, has a runtime of 0(1), great!). And when you delete (pop()), you're removing the first item, 
#               then just shifting the pointer of the head to the next item (also an 0(1), perfect!)
#

# This is your very generic Queue all coded and ready to go - can be used to keep track of interactions
#
class LinkedListNode:
    def __init__(self, data):
        self.value = data
        self.next = None

class Queue: 
    def __init__(self):
        #what do we need to keep track of in our queue? - front (head), back(tail)
        self.head = None # essentially a linked list of size nothing
        self.tail = None

    #this method is going to print our list so we can see what's going on
    def __str__(self): #this dunder function __str__ allows us to call the print function on Queue
        str = ""
        curr_node = self.head
        while curr_node:
            str += f'->{curr_node.value}' #this will print our list of nodes
            curr_node = curr_node.next
        return str

    #a queue method - to insert
    # We can have duplicates in our data, so we don't need to check if any item already exists
    def enqueue(self, value): 
        new_node = LinkedListNode(value) #creating a new node
        if self.head is None and self.tail is None:
            self.head = new_node #we're creating our new node
            self.tail = new_node #both the head and tail are pointing to the same thing because we only have 1 node
            return
        #once we've created this list, now we want to link the new node to the end of our list (the tail)
        self.tail.next = new_node #reassigning a variable that is inside the node self.tail
        #then we need to update the tail
        self.tail = new_node # this is just reassigning a variable (the pointer?)



    #a queue method - delete (return the value from the front(head) with pop(), and remove it)
    def dequeue(self):
        if self.head is None:
            return #this is because if our list is empty, there isn't anything to be removed
        old_head = self.head
        self.head = self.head.next #reassigning the next item as the head. This is creating a new pointer to a different item in memory as the head
        #if we remove the last item, we need to also update tail
        if self.head is None:
            self.tail = None
        return old_head.value





my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3) #adding all these to our queue
print(my_queue) # -- this will call that str function
print(f'Removed {my_queue.dequeue()}') # will see we removed 1

my_queue.enqueue(4)
print(my_queue) #then will see 1 removed and 4 was added

################# Here we can use arrays for the Queue as well, you just need to be sure you're appending and removing for Queue protocol (the First in First out)

class Queue:
    def __init__(self):
        self.storage = []
    
    def __str__(self):
        return str(f'front{self.storage} back')

    def enqueue(self, value):
        self.storage.append(value) #adding items to back - so the back of the queue is the back
    
    def dequeue(self): #remove item from the front of the array, .pop(defaults to removing to the back, so you have to specify the front first index)
        if len(self.storage) == 0: #if the queue is empty
            return
        return self.storage.pop(0)


############################################### STACK DATA STRUCTURE #########################################################
# "Last in First Out" - this is the only important part of building a stack structure, a LL is the most optimal ways to build this structure
# We need to know how the data enters and leaves the data structure 
# the functions of the stack, stacks on top. You have to go by the order that all the items came in, from the top
# WE can add and remove from the same spot
# we want to use LL for this data structure too
# What should the top of our stack in the linked list be? The head or the tail? 
#       - We need to remove from Top and also add to the Top
#       - Adding to the tail - easy, Removing from the tail of the singularly linked list  - NOT easy (So don't use the tail as the top)
#       - We can easily add a new node to the head (the front), just link the node to the head, then shift the head over
#           - So it matters, we can't decide to use the end of the LL as the top, we want to use the head as the top, because that's whats easier
#
class LinkedListNode:
    def __init__(self, data):
        self.value = data
        self.next = None

class LLStack: # we only need the head here, because with stacks, that's how we're both adding and removing our items
    def __init__(self):
        self.head = None

    # !!!!! If you don't have this str method here in your class, then when you 'print' to the console, you will get an error
    def __str__(self):
        str = 'TOP '
        curr_node = self.head
        while curr_node:
            str += f'-> {curr_node.value} '
            curr_node = curr_node.next
        return str

    def push(self, value):
        # Add a new node to the head & shift the pointer
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    def pop(self): # all we're doing here is removing from the head and move the head over
        if self.head is None:
            return
        old_head = self.head
        self.head = self.head.next
        return old_head.value


# Here is how we would write this SAME data structure, using a vanilla JS array versus the Linked List. 
# It's much quicker and simpler to write - this might be easier to execute in interviews
# it still makes sense to the keep the top of the stack, as the back of the array (it's easier, because we have the append method)
class Stack:
    def __init__(self):
        self.storage = []
    
    def __str__(self):
        return str(self.storage)

    def push(self, value):
        self.storage.append(value)
    
    def pop(self):
        if len(self.storage) == 0: #if the stack is empty
            return
        return self.storage.pop() # if you decided to add items from the end, you need to remove them from the same place (by nature of stacks)
                                    # so you then need to use .pop() to take the off 
                                    # Arrays are essentially already Stacks​, arrays are still perfectly valid for stacks, because it's still the LIFO principal

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack)
print(f'Popped {my_stack.pop()}')
print(f'Popped {my_stack.pop()}')
print(f'Popped {my_stack.pop()}')
my_stack.push('banana')
print(f'Popped {my_stack.pop()}')


########################### TWO STACKS EXAMPLE ################################################
# We have 2 stacks existing in QueueTwoStacks
# To access data from certain points in the stack, you have to use .pop() every item until you reach the item you want. 
# What do we do with our items we're popping off along the way? We put them over in the 2nd stack. 
# Once we get and remove the item we wanted, we then need to shift all the items back into the first stack. 

"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.
​
As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.
​
The Stack class that you will use has been provided to you.
"""
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)
​
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"
​
class QueueTwoStacks:
    def __init__(self):
        self.in_stack = Stack() #The stack we ADD items into
        self.out_stack = Stack() #the stack we remove items from before we do any shuffling - the out stack becomes the 'active stack'
​-
    def enqueue(self, value): # a constant runtime
        self.in_stack.push(value)
​
    def dequeue(self): #we have to move all items over, and then back. So it's linear 0(n). But we don't actually have to put all of them back to keep dequeuing. 
        # Check the length of out stack,
        # if its not empty, pop from out stack
        if len(self.out_stack.data) > 0:
            return self.out_stack.pop()
        # Otherwise, shuffle items from in stack to outstack
        while len(self.in_stack.data) > 0:
            # Pop item from in stack
            # push to out stack
            popped_item = self.in_stack.pop()
            self.out_stack.push(popped_item)
        # pop top item from stack
        if len(self.out_stack.data) > 0:
            return self.out_stack.pop()
​
​
my_queue = QueueTwoStacks()
​
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print(f'Removed {my_queue.dequeue()}')
​
my_queue.enqueue(4)
print(f'Removed {my_queue.dequeue()}')
print(f'Removed {my_queue.dequeue()}')
print(f'Removed {my_queue.dequeue()}')
​
my_queue.enqueue(1)
my_queue.enqueue('banana')
print(f'Removed {my_queue.dequeue()}')
print(f'Removed {my_queue.dequeue()}')
