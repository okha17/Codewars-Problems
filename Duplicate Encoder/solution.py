from collections import Counter # import library that counts occurrences of values in list
def duplicate_encode(word):
    text = word.lower() # lower all character since case does not matter 
    mylist = Counter(text) # convert string into dictionary that contains count of each character
    str_list = [] # list that will contain parentheses
    for key in text: # loop for length of string
        if (mylist.get(key)) > 1: # if the occurrence of the value is more than 1 set it as )
            str_list.append(")")
        else:
            str_list.append("(") # else it is set as (
    solution = "".join(str_list)
    return solution