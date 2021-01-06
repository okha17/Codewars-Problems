def find_outlier(integers):
    i = 0
    evenlist = [] #list for even elements
    oddlist = [] #list for odd elements 
    while i < (len(integers)): # loop through list
        if integers[i] % 2 == 0: # if value is even add to evenlist
            evenlist.append(integers[i])
        else: # if value is odd add to oddlist
            oddlist.append(integers[i])
        i += 1 # increment through list
    if len(evenlist) == 1: # if evenlist has 1 value it has the outlier
        return evenlist[0]
    elif len(oddlist) == 1: # if oddlist has 1 value it has the outlier 
        return oddlist[0]
    return None