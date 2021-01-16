def persistence(n):
    if n <= 9: # if value is already single digit return 0
        return 0
    total = n # set the total to value passed in
    count = 0 # count the number of times we must multiply to get to a single digit
    while total > 9: # while the total is greater than 9 so it is double digit
        temp_list = [int(i) for i in str(total)] # convert number to list of strings
        values = [int(i) for i in temp_list] # convert list to ints
        total = 1 # set total to 0 for new values to be stored
        for i in values: # loop through list to multiply values
            print(i)
            total *= i
        count += 1
    return count
    # your code