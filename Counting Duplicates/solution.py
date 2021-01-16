from collections import Counter # import library that counts occurrences of values in list
def duplicate_count(text):
    count = 0
    text = text.lower() # lower all character since case does not matter 
    mylist = Counter(text) # convert string into dictionary that contains count of each character
    for key in mylist:
        if (mylist.get(key)) > 1: # if the occurrence of the value is more than 1 increment count
            count += 1
    return count

     