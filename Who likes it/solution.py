def likes(names):
    if len(names) == 0:
        no_one = "no one likes this"
        return no_one
    if len(names) == 1:
        one_person = names[0] + " likes this"
        return one_person
    if len(names) == 2:
        two_people = names[0] + " and " + names[1] + " like this"
        return two_people
    if len(names) == 3:
        three_people = names[0] + ", " + names[1] + " and " + names[2] + " like this"
        return three_people
    if len(names) > 3:
        total_minus_two = (len(names)) - 2
        mul_people = names[0] + ", " + names[1] + " and " + str(total_minus_two) + " others like this"
        return mul_people
    
    
    