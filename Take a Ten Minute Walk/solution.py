def is_valid_walk(walk):
    if len(walk) != 10: # if the count is not 10 it is false
        return False
    perpcount = 0 # count for west and east
    parcount = 0 # count for north and south
    for i in walk: # loop checks values and adds subtracts the difference of movements
        if i == 'n':
            parcount += 1
        if i == 's':
            parcount -= 1
        if i == 'w':
            perpcount += 1
        if i == 'e':
            perpcount -= 1
    if perpcount == 0 and parcount == 0: # if we are back to the starting point return true
        return True
    else:
        return False
  