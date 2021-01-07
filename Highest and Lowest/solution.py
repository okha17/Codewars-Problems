def high_and_low(numbers):
    # converts string of numbers into a list of ints
    num_list = [int(s) for s in numbers.split(' ')] #split numbers by spaces
    largest_num = max(num_list) 
    smallest_num = min(num_list)
    return str(largest_num) + " " + str(smallest_num)