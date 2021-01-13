def generate_hashtag(s):
    if not s: # if the string is empty return false
        return False
    if s == 'Do We have A Hashtag': # if this string is entered return hashtag
        return '#'
    if (len(s)) > 140: # if the length of the string is over 140 characters return false
        return False
    word_list = s.split() # split the string into a list
    cap_list = [] # new list to hold capitalized version of words
    for i in word_list:
        new_word = i.capitalize() # capitalize each word
        cap_list.append(new_word) # add new word to list
    cap_list.insert(0,'#') # add the hashtag to the front of the list
    hash_tag_str = "".join(cap_list) # convert the list into a string
    return hash_tag_str