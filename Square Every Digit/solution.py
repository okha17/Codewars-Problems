def square_digits(num):
    values = [int(i) for i in str(num)] #Converts num value into list of ints to iterate
    sqr_str = "" # string that will hold squared values
    for i in values:
        square = str(i*i) # holds squared valued
        sqr_str += square # add newly squared value to our string
    return int(sqr_str)