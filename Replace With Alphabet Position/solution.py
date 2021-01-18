def alphabet_position(text):
    mylist = [] # list to hold the solution
    text = text.replace(" ", "") # replace spaces with none
    text = text.lower() # lower all the text
    for i in text:
        if i.isalpha(): # check if the text is a letter
            mylist.append(str(ord(i) - 96)) # convert to correct position through ascii math
    solution = " ".join(mylist)
    return solution