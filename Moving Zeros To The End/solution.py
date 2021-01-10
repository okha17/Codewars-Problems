def move_zeros(array):
    new_array = [] # array to rearrange values
    count = 0 # count the number of 0 
    for i in array: 
        if i == 0 and i is not False: # if the value is 0 and not False increment count
            count += 1
        else: # else if the value is appended to the new array since it is not 0
            new_array.append(i)
    while count > 0: # while the count is not 0
        new_array.append(0) # append the zeros to the end of the array
        count -= 1
    return new_array
    #your code here