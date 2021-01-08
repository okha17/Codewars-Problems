def disemvowel(string):
    new_str = ""
    i = 0
    for i in string:
        if i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "I" or i == "o" or i == "O" or i == "u" or i == "U":
            pass
        else:
            new_str += i
    return new_str