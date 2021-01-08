def odd(floor): # Function that converts number to odd value
    floor = (2*floor) + 1
    return floor

def tower_builder(n_floors):
    tower_list = [] #list used to build tower
    tower_block = '*' # tower element 
    floor_value = 0 # used to calculate how many tower blocks needed for each floor
    odd_value = n_floors - 1 # used to calculate  number of spaces added to tower
    while n_floors > 0: # loop as long as number of floors is greater than 0
        tower_level = odd(floor_value) * tower_block # string for tower is multiplied by odd number
        tower_level = tower_level.replace(" ", "") # replaces spaces when you repeat string
        if n_floors > 1: # for floors that are not the base floor they need padding
            temp = odd(odd_value)
            tower_level = tower_level.center(temp) # add spaces to floor to match bottom floor length
        tower_list.append(tower_level)
        floor_value += 1
        n_floors -= 1
    return tower_list
    # build here