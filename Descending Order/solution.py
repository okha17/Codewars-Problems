def descending_order(num):
    temp_list = [int(i) for i in str(num)] #Convert passed int into a list of values
    values = [int(i) for i in temp_list] #Converts the list of string values into int values
    values.sort(reverse = True) #Sorts the list of ints in descending order
    temp_str = "" # string that holds values
    for i in values:
        temp_str += str(i) 
    return int(temp_str) # return as an int
