##Using Stacks in recursive functions
def print_hello_world_n_times(n):
    if n == 0:
        return #we don't 'return' until n equals 0
    print("Hello world")
    print_hello_world_n_times(n - 1)


print_hello_world_n_times(3)
## the stack grows until the recursion meets the base case
#Anything recursive, you can do with iteration, and vice versa
#You can assume 


##NOTES on STACKS
def print_b():
    print("B") # --> B gets popped off
    return

def print_a():
    print_b() # if you call this four times, you'll add three "B"'s to the stack
    print_b()
    print_b()
    print("A")
    return


print_a()

## When you 'call' a function, it adds something to the top of the stack
## When you a function 'returns', that item is popped off the stack

##########################################################################

#Linear Search Notes

# # Is an item in our array? return true or false

def linear_search(array, target):
    # Loop through our array
    for item in array:
        print("Try searching")
        if item == target:
            return True
    
    return False

def search_in_current_spot(array, target, current_spot):
    if current_spot >= len(array):
        return False

    if array[current_spot] == target:
        return True

    found = search_in_current_spot(array, target, current_spot + 1)
    return found
##################################################################################################
#You can search by creating a midpoint -->  Ask yourself a question that greatly reduces your search space.
    # What is the middle point? Is our search value greater or less than that midpoint number?
        # So at worst, we're always splitting our search in half


def binary_search(arr, target):
    #get the middle of the arr
    counter = 0 
    start = 0
    end = len(arr)
    while not end < start:
        counter += 1 #
        middle_index = (start + end) // 2
        #compare the value in the middle, to the target
        #if the value == target:
        if arr[middle_index] == target:
            print(counter)
            return True
        # if the value is smaller:
        elif arr[middle_index] > target:
            #repeat over the array from start to middle
            end = middle_index -1
        # if the value is target:
        else:
            # repeat over array from the middle to end
            start = middle_index + 1
    return False

our_array = list(range(20))
print(our_array)
print(binary_search(our_array, 19)) # searching for the number 19 in our_array

    ###### This whole process is splitting the array 

## This process creates a new runtime - What we've been doing is if we have 5 items, it creates 5 steps (this is linear)
### This new process, the relationship between input and number of steps in the function. doubling the input only increases the number of steps by an increase of 1
    ## Double the input, only moves the number of steps by the linear amount of 1 --> This is a 'log' runtime (like in math)

### Logarithmic functions (and constant) are the BEST and most effecient runtime functions