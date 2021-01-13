def digital_root(n):
    total = n # set the total to value passed in
    while total > 9: # while the total is greater than 9 so it is double digit
        temp_list = [int(i) for i in str(total)] # convert number to list of strings
        values = [int(i) for i in temp_list] # convert list to ints
        total = 0 # set total to 0 for new values to be stored
        for i in values: # loop through list to add values
            total += i
    return total
    # ...