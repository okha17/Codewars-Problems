def get_middle(s):
    if (len(s)) % 2 == 0: # check if even
        half_val = int((len(s))/2) # get halfway index
        half_val -= 1 # start at first middle index
        half = s[half_val] # save value in half
        half_val += 1 # get next middle value
        half += s[half_val] # add value to half string
        return half
    elif (len(s)) % 2: # check if odd
        half_val = int((len(s))/2) #get halfway index
        half = s[half_val] # set string to half value 
        return half
