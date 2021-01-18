def order(sentence):
    if not sentence: # if the sentence is empty return empty string
        return ""
    sen_list = sentence.split(" ") # split the string into a list
    solution = [] # list to hold correct order of words
    count = 1 # count that counts total number of words to add
    while len(solution) != len(sen_list): # break loop when list are equal so all words added
        for i in sen_list: 
            count = str(count) #covert value to string
            if count in i: # if the number is in the string add it to the solution list
                solution.append(i)
                count = int(count) + 1 # increase the count looking for next word
    return " ".join(solution) # return string answer
