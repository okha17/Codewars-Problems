def positive_sum(arr):
    value = 0
    for i in arr:
        if i < 0:
            value += 0
        else:
            value += i
    # Your code here
    return value
