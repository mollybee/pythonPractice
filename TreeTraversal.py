# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CODESIGNAL QUESTION
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def treePaths(t):
    if t is None: 
        return []
    pathsArray = [] # Here we are collecting the entire path (the first and last node in the path and everything in between); but we don't want to pass             the path into the array until we have the entire path
# We're going to traverse the tree, visit all the nodes
    def traverse(current_node, prev_path):
# Given a current node, and a previous path
        if current_node.left is None and current_node.right is None:
            pathsArray.append(f'{prev_path}{current_node.value}') # a string literal adding the two together variables together 
    #either push the path to the pathsArray
        if current_node.left:
            traverse(current_node.left, f'{prev_path}{current_node.value}->')  #this is the recursive line (this connecting the current node with the previous node)         #The output is asking for an arrow between the nodes. Here we are using a string literal to add those nodes and output it with the arrow
        # or keep going through the tree (if we haven't finished our whole path)
        if current_node.right: 
            traverse(current_node.right, f'{prev_path}{current_node.value}->')
            
        
    traverse(t, "") # traverse is a function and here we are calling , t is the first root of the tree and the empty "" because there is no previous node           #to the first
    return pathsArray

# you want to write a helper function to traverse the tree - no matter what traversal or depth/breadth you decide to use, or iterative 
# because it's asking you to return an array 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CODESIGNAL BINARY SEARCH TREES TRAVERSAL PROBLEM - SUCCESSFUL SOLUTION & NOTES

# Binary trees are already defined with this interface:

# class Tree(object): ## root is a single tree node, just like a linked list node
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def binaryTreeInOrderTraversal(root): # root is passing in an instance of the class Tree
    numArray = [] #all numbers that are smaller go left, larger - right in the binary search
    #goal is to traverse the tree, get to each individual node, and then move that number into our array
    # so we'll want to have our array outside the traversal
    def addNodeToArray(currentNode): #the function that visits all the nodes, this is where we're appending to our array
       
        #inOrder Traversal - where we move left first, then come back up to go right
        if currentNode.left is not None: #adding the left first to the array, but we can change the order
            addNodeToArray(currentNode.left) #then the same code above runs
            
        numArray.append(currentNode.value) #appending our node's value (the number) to our array
            #adding the 'visiting node' (2) after going left 
            
        if currentNode.right is not None:
            addNodeToArray(currentNode.right)
        
    addNodeToArray(root) #the root is what we're passing into the binaryTreeTraversal function    
    return numArray
            


# Visiting/Processing - done w/ node once we return it, in this specific scenario the processing is the adding the node's value (the number) to our array
## Breadth - First Traversal - using queues - cannot be recursive 
# When writing traversals, consider your current Node 

# Need to build the array we'll return - it will come from traversing the tree and moving items to the array
# return statement will need to be an array 
# the numbers are being copied to the array, not removed from the tree (mutable/immutable - passing numbers to an array is immutable)
# removing items from the tree will 'break' the tree - usually don't want to modify the trees


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TREE TRAVERSAL LECTURE NOTES:

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
​
    def insert(self, value):
        if value <= self.value:
            # the new value, must go left
            if self.left is None:
                # create a new node as a left child of current node
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
​
        else:
            # the value must go right    
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # let the right hand Node figure it out
                self.right.insert(value)
​
# Pre-order traversal
def traverse_tree(root):
    print(root.value)
​
    if root.left:
        traverse_tree(root.left) 
    if root.right:
        traverse_tree(root.right)
​
# in order traversal
def traverse_tree_in_order(node):
    if node.left:
        traverse_tree_in_order(node.left) 
​
    print(node.value)
​
    if node.right:
        traverse_tree_in_order(node.right)
​
# post order traversal
def traverse_tree_post_order(node):
    if node.left:
        traverse_tree_post_order(node.left) 
​
    if node.right:
        traverse_tree_post_order(node.right)
​
    print(node.value)
​
​
def traverse_iterative(root, target):
    stack = []
    stack.append(root)
​
    while len(stack) > 0:
        # Process the top item on the stack
        current_node = stack.pop()
        
        # Do what needs to be done with the node
        print(current_node.value)
        if current_node.value == target:
            return True
​
        # how do we continue forward?
        if current_node.right:
            stack.append(current_node.right)
        
        if current_node.left:
            stack.append(current_node.left)
    
    return False
​
​
def bft_traverse_iterative(root, target):
    queue = []
    queue.append(root)
​
    while len(queue) > 0:
        # Process the top item on the stack
        current_node = queue.pop(0)
        
        # Do what needs to be done with the node
        print(current_node.value)
        if current_node.value == target:
            return True
​
        # how do we continue forward?
        if current_node.left:
            queue.append(current_node.left)
​
        if current_node.right:
            queue.append(current_node.right)
        
    return False
​
​
# Pre order search 
def search_recursive(root, target):
    if root.value == target:
        return True
    if not root.left and not root.right:
        return False   
​
    is_found_in_left = False
    is_found_in_right = False
    if root.left:
        is_found_in_left = search_recursive(root.left, target)
​
    if root.right:
        is_found_in_right = search_recursive(root.right, target)
​
    return is_found_in_right or is_found_in_left
​
# Pre-order traversal
def traverse_tree(root):
    print(root.value)
​
    if root.left:
        traverse_tree(root.left) 
    if root.right:
        traverse_tree(root.right)
    
​
​
​
root = BSTNode(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(13)
​
# print(traverse_iterative(root, 14))
​
# print(search_recursive(root, 5))
​
bft_traverse_iterative(root, 17)