def solution(number):
    total = 0 # total value that hold the sum
    for i in range(number): # for loop that iterates until the parameter passed in
        if (i % 3 ==0) or (i % 5 == 0): # if the number is a multiple of 3 or 5 enter if statement
            total += i # add value to total
    return total
  