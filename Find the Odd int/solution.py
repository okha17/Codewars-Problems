from collections import Counter # import library that counts occurents of values in list
def find_it(seq):
    new_list = Counter(seq) # make a dictionary for keys and values which are the number and occurences
    for key in new_list:
        if (new_list.get(key)) % 2: # loop over the dictionary to find the odd occurence int
            odd_int = key
    return odd_int #return the odd int
