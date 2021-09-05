                                    #EXAMPLE TWO - LECTURE
# class LinkedListNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None # Other LinkedListNode
# ​
# head = LinkedListNode('A')
# tail = head
# ​
# def add_node_to_next(current_node, value):
#     # Make the new node
#     new_node = LinkedListNode(value)
#     old_next = current_node.next
#     # Link current node to new node
#     current_node.next = new_node
#     # New node, should link to whatever 
#     # current_node was linked to before
#     new_node.next = old_next
#     return new_node
# ​
# def add_node_to_head(current_head, value):
#     new_head = LinkedListNode(value)
#     new_head.next = current_head
#     return new_head
# ​
# # def print_list(start_node):
#     if not start_node:
#         return
#     print(start_node.value)
#     # I want to print the next node, 
#     # I wonder if I have a function for that...
#     print_list(start_node.next)
# ​
# def print_list_iter(start_node):
#     curr_node = start_node
#     while curr_node is not None:
#         print(curr_node.value)
#         curr_node = curr_node.next
    
# def get_nth_node(start_node, n):
#     curr_node = start_node
#     current_num = 0
#     while curr_node is not None:
#         if current_num == n:
#             return curr_node
#         curr_node = curr_node.next
#         current_num += 1
# ​
# ​
# # tail = add_node_to_next(tail, 'B')
# # tail = add_node_to_next(tail, 'C')
# # add_node_to_next(head, 'E')
# # head = add_node_to_head(head, 'D')
# ​
# # fourth_node = get_nth_node(head, 3)
# # print(fourth_node.value)
# ​
# # add_node_to_next(fourth_node, 'Im between B and C')
# ​
# # print_list(head)
#################################################################################################
                            #EXAMPLE ONE - LECTURE
# """
# Given a reference to the head node of a singly-linked list, write a function
# that reverses the linked list in place. The function should return the new head
# of the reversed list.
# ​
# In order to do this in O(1) space (in-place), you cannot make a new list, you
# need to use the existing nodes.
# ​
# In order to do this in O(n) time, you should only have to traverse the list
# once.
# ​
# *Note: If you get stuck, try drawing a picture of a small linked list and
# running your function by hand. Does it actually work? Also, don't forget to
# consider edge cases (like a list with only 1 or 0 elements).*
# """
# class LinkedListNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None # Other LinkedListNode
# ​
# from objectives import add_node_to_next, print_list
# ​
# ​
# def reverse(head_of_list):
#     if not head_of_list or head_of_list.next is None:
#         return head_of_list
    
#     curr_node = head_of_list
#     prev_node = None
#     next_node = None
#     while curr_node:
#         next_node = curr_node.next
#         # Have current node point backwards
#         curr_node.next = prev_node
# ​
#         # move the curr_node along
#         prev_node = curr_node
#         curr_node = next_node
    
#     return prev_node
# ​
# ​
# head = LinkedListNode(1)
# tail = head
# ​
# tail = add_node_to_next(tail, 2)
# tail = add_node_to_next(tail, 3)
# tail = add_node_to_next(tail, 4)
# tail = add_node_to_next(tail, 5)
# ​
# print_list(head)
# print('------')
# reversed_head = reverse(head)
# print_list(reversed_head)


###########################################################
#Molly's LinkedList Notes

# Unlike arrays, linked lists can store data uncontiguously (not one slot in memory after another)
# Linked Lists can be sorted or unsorted, and any type of data can be stored in a linked list
# There can be duplicates stored in a linked list!
# There are 3 types of linked lists: ALL linked lists are made up of 'nodes' - where each node stores the data as well as info about other nodes that exist within the list
#       Singly (SLL) - each node stores the data and a pointer to where the next node in the list is at; so you can only move forward through the list, to transverse across an SLL, 
#                       you need a reference to the first node ('head'). From this head, you can visit all other nodes using the next pointers
#       Doubly (DLL) - each node also stores a refernce to the previous item, you with this kind of list you can navigate both forward and backwards. A DLL usually stores a
#                       pointer to the last items in the list ('tail')
#       Circular - this kind of list links the last node ('tail') to the first node ('head') in the list. This kind of linking causes a 'circular traversal',
#                   Meaning when you reach the end of the list, the next item will be back at the beginning of the list. 

# SPACE/TIME COMPLEXITY OF LINKED LISTS:
#   LookUp (an item by index): Linear time (0(n)) - the distance in memory between one item and the next is varied and unknown
#   Append (add item to list): Constant time (0(1)) - because we always have a refernce point to the tail, to easily insert an item AFTER the tail
#   Insert (in the worst case): Linear time (0(n)) - to insert an item at a specific spot, we'll have to traverse - starting at the head - until we reach the spot we want
#   Delete (worst case) : Linear time (0(n)) - Same reasoning as insertion
#   Space: Linear (0(n)) - each item in the list will take up memory space

# Strengths of LL
#   They're fast because they always have a reference to the head and tail. Doing anything on the head or tail is a constant time operation no matter how many items are in the list
#   Great for if you don't know the size of the data you're working with or if data size will change over time. Since each item is not store contiguously,  you don't have 
#       the 'double appends' as you need in a dynamic array. Whenever you instantiate a LL, you don't need to set a capacity.
# Weakness of LL
#   Not effecient at accessing middle indices

# Differences and Benefits versus Arrays
#   Arrays hold data contiguously, which makes for an easy mathematical lookup. But this can be a problem when you create an array, you either need to know how much space in memory
#       you will need beforehand, or set aside a bunch of extra memory you might not need just in case.
#   However with Linked Lists, the elements are NOT store side-by-side in memory, each element can be stored ANYWHERE in memory. In addition to storing the data for that element,
#       each element also stores a pointer to the memory location of the next element in the list. The elements in a LL do NOT have an index for this reason. 
#       So to get a specific element in a linked list you need to start at the head, and work your way through the entire list (linear time) one at a time until you reach your 
#       search element.

#  OTHER NOTES:
#   You know you're at the end of the linked list when that node (a.k.a element/item) does not have a pointer

# BUILDING A SINGLY LINKED LIST
#  Step 1: Create a class for each element in the linked list:

class LinkedListNode: #for each item
    def __init__(self, data=None, next=None):
        self.data = data #data item
        self.next = next #the pointer

# Step 2: build the class for the LinkedList itself: This so far only includeds the initialization method
class LinkedList: #the class for entire list
    def __init__(self, head=None):  
        self.head = head

# Step 3: Add an append method - so we can add nodes to the end of our list
    def append(self, data):
        new_node = LinkedListNode(data)

        if self.head:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node
        else:
             self.head = new_node

# Step 4: Using our new classes "LinkedListNode" and "LinkedList", lets create a list of elements (1 ,2 , 3): 

a = LinkedListNode(1) #creating the head
my_ll = LinkedList(a) #setting our LinkedList class to this variable, and having our LinkedList take in LinkedListNode(1)
my_ll.append(2) #adding next item
my_ll.append(3) #adding next item
print(my_ll.head.data)



###########################################################################################

                # CODE-SIGNAL LINKED LIST ASSIGNMENT
                #Problem 1
#'You have a singly linked list l, which is sorted in strictly increasing order, and an integer value. Add value to the list l, preserving its original sorting.'

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def insertValueIntoSortedLinkedList(l, value):

#Attempt:

def insertValueIntoSortedLinkedList(l, value):

    class ListNode:
        def __init__(self, x):
            self.value = x
            self.next = None
                
    head = ListNode(value)
    tail = head

    def add_node_to_next(l, value):
        new_node = ListNode(value)
        old_next = l.next #creating the pointer
        
        l.next = new_node
        
        new_node.next = old_next
        print(new_node)
        return new_node
    
    def add_node_to_head(current_head, value):
        new_head = ListNode(value)
        new_head.next = current_head
        print(new_head)
        return new_head
    
    #printing our list
    def print_list(start_node):
        if not start_node:
            return print(start_node.value)
        print_list(start_node.next)
    
    #what is this doing?
    def print_list_iter(start_node):
        curr_node = start_node
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next
    
    #return sorted('something') ----- IDK WHAT TO RETURN
        
insertValueIntoSortedLinkedList([1, 3, 4, 6], 5)
#The 'l' variable is taking an array of numbers as the input
# the 'value' parameter is taking the new value as the input

#The objective is to return the new list with the items sorted ascending
