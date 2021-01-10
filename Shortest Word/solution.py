def find_short(s):
    word_list = s.split() # split string into list of words
    len_list = [] # list to save length of strings into
    for i in word_list: 
        len_list.append(len(i)) # add lengths to list
    l = min(len_list) # get the smallest length 
    return l # l: shortest word length