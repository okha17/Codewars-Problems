def count_bits(n):
    count = 0 #count total number of 1's
    bin_str ='{0:08b}'.format(n) #format the int to a binary value 
    for i in bin_str: # loop through binary string counting all the 1's
        if i == "1":
            count += 1
    return count