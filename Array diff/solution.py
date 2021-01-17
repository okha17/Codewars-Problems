def array_diff(a, b):
    if not a or not b: # if a is empty or b is empty return a
        return a
    new_list = [] # new list for the array difference 
    for i in a:
        if i in b: # if the value is found in b ignore it
            pass
        else: # if the value is not in the array then add it to the new one
            new_list.append(i)
    return new_list
                