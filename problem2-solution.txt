def csCheckPalindrome(input_str):
    
    # FOR Loop answer
    # i = len(input_str) - 1
    # for x in input_str:
    #     if x != input_str[i]:
    #         return False
    #     i -= 1
        
    # return True
    
    # WHILE Loop answer
    input_str_array = list(input_str)
    while len(input_str_array) > 1:
        # Remove first and last item from the array
        frontChar = input_str_array.pop(0)
        backChar = input_str_array.pop() 
        
        # Compare them
        if frontChar != backChar:
            return False
    
    # Our array is either empty, or there is one character left
    # All chars matched, so we can safely return true
    return True
        