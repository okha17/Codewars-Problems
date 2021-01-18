def create_phone_number(n):
    i = 0
    phone_num = "" # string that holds number
    while i < 10: # loop for 10 digit number
        if i == 0:
            phone_num += "(" # add to start of string
        if i == 3:
            phone_num += ")" # before 4th number is added we need to add the parantheses and space
            phone_num += " "
        if i == 6:
            phone_num += "-" # before the 7th number is added we need to add the dash
        phone_num += str(n[i])
        i += 1
    return phone_num