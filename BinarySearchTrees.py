######## BINARY SEARCH TREES NOTES ################

# If you know the tree's HEIGHT (h), you can calculate the number of nodes there are in a binary tree and plugging it into this formula:
#   n = 2^h - 1
# If you know the number of nodes (n) in a tree, then you can use this formula to calculate the tree's height:
#   log_2(n + 1) = h
# The left subtree of a node contains only nodes with keys lesser than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# A BST is 'balanced' when if the heights of its left and right subtrees differ by at most one, and both of the subtrees are also balanced.




# CREATING A BINARY SEARCH TREE

# Step 1. Instantiate(create) a Binary Search Tree Node class (BSTNode). An instance of BST should include: 'value', 'right node', and 'left node'
class BSTNode:
    def __init__(self, value): #this is our initilization method
        self.value = value
        self.left = None
        self.right = None

# Step 2. Now we must define our BST class; this class will have an 'initialization' method and an 'insert' method
class BST:
    def __init__(self, value):
        self.root = BSTNode(value)

    def insert(self, value):
        self.root.insert(value)

# Step 3. Next, add an 'insert' method onto the BSTNode class, since our BST class expects it to have one
class BSTNode:
    ....
    #THIS IS STEP 3 (below)
    #This bit goes right under the instaniation method on the BSTNode
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

# Step 4. Now we can insert nodes into our binary tree! So next we should create a 'search' method so we can lookup values
class BST:
    
    .....
        #THIS IS STEP 4 (below)
    def search(self, value):
        self.root.search(value)

# Step 5. Our BST class expects a 'search' method on the BSTNode, so we now need to create that
    
    class BSTNode...
        ....
    #THIS IS THE 'search' METHOD YOU ADD ONTO THE BSTNode
        def search(self, target):
                if self.value == target:
                    return self
                elif target < self.value:
                    if self.left is None:
                        return False
                    else:
                        return self.left.search(target)
                else:
                    if self.right is None:
                        return False
                    else:
                        return self.right.search(target)

#### Notes: If you need to delete a node, keep these three things in mind: 
# 1.If the BSTNode to be deleted is a leaf (has no children), we can remove that node from the tree.
# 2.If the BSTNode to be deleted has only one child, we copy the child node to be deleted and delete it.
# 3.If the BSTNode to be deleted has two children, we have to find the "in-order successor". 
#   The "in-order successor" is the next highest value, the node that has the minimum value in the right subtree.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CODESIGNAL CHALLENGE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# You are given a binary tree and you need to write a function that can determine if it is height-balanced.

# A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ in height by a maximum of 1.
#Given the following tree [5,10,25,None,None,12,3]: return 'True'
    5
   / \
 10  25
    /  \
   12   3


# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def balancedBinaryTree(root):


# Objective: Determine if it is height balanced
# If it's height balanced, then the left side and the right side should be equal or no different by one node
# So we'll need to compare the 'left' and the 'right' 
# We'll need to create a loop where we are both calculating the height of each subtree. 
# If we loop through the entire tree where there are equal or 1 different in height, then you return true
# Then comparing them until we get no nodes on one side - in which we return false
#
# Step 1. create a binary search tree, instantiating the right and left
# 

##
##
## ~~~~~~~~~~~~~~~ Melanie's solution


class Height:
    def __init__(self):
        self.height = 0

def height(root):
    if root is None:
        return 0
        
    return max(height(root.left), height(root.right)) + 1

def balancedBinaryTree(root):
    if root is None:
        return True

    left_height = Height()
    right_height = Height()
    
    left_height.height = height(root.left)
    right_height.height = height(root.right)
    
    left = balancedBinaryTree(root.left)
    right = balancedBinaryTree(root.right)
    
    if (left_height.height - right_height.height) <= 1:
        return True
    
    return False

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Artem's lecture notes: from 9/8
# this is using recursive techniques. 
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None # like the .next from the LL
        self.right = None # same as the self.left 
​
    def insert(self, value):
        if value <= self.value:
            # the new value, must go left
            if self.left is None:
                # create a new node as a left child of current node
                self.left = BSTNode(value)
            else:
                self.left.insert(value) # - this is the recursion 
​
        else:
            # the value must go right    
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # let the right hand Node figure it out
                self.right.insert(value)
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

# Questions for meeting with Artem: 
# Could you walk me through a simple binary tree, and what the pieces of code mean? i.e. 'self.left', and how it's used recursively?
# How is data stored in a 'tree' structure? Are we accessing this tree-shaped data using the Binary Search? I'm struggling to visualize what's happening.
# In what scenario does it make sense to store/access(?) using a binary search? Most efficient runtime (logarithmic)
# I've noticed there are variations to writing a binary tree, where we don't have separate Node and Tree classes, why is this?
# what is the primary differences between a traversal and a binary search tree? Or how are these related?
# Could we go over one of the binary search tree problems? - 

# Traversal - we're jumping back and forth around between sides - we're still going back to previous functions


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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