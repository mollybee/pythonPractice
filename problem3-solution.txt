def csRemoveDuplicateWords(input_str):
    wordsArray = input_str.split()
    uniqueWordsArray = []
    
    while len(wordsArray) > 0:
        nextWord = wordsArray.pop(0)    # Remove next word from front of array
        
        # If we haven't already encountered this word, add it to our array
        if nextWord not in uniqueWordsArray:
            uniqueWordsArray.append(nextWord)
    
    # Smoosh all of our unique words back together, separated by a space, to create our unique word string
    freeFromDuplicateWordsString = ' '.join(uniqueWordsArray)
    
    return freeFromDuplicateWordsString
         