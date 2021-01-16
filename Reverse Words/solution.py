def spin_words(sentence):
    word_list = sentence.split(" ") # split string into a list
    i = 0 # count for looping
    while i < len(word_list): # loop for count of words in list
        if len(word_list[i]) >= 5: # if the word is 5 or more characters reverse it
            reversedstring=''.join(reversed(word_list[i])) #reverses the word
            word_list[i] = reversedstring # replace the word with reversed version
        i += 1
    reverse = " ".join(word_list) # store the word list in a string
    return reverse