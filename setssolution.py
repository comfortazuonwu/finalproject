def letters(text):
    """Using a set, determine if there are duplicate letters in the text given. Return true if there are no duplicates and false if there are duplicates"""
    my_set = set(text)
    #find the length of the set and compare it to the length of the text.
    set_lenght = len(my_set)
    text_lenght = len(text)
    #if the text lenght and set lenght are the same, there are no duplicates
    if set_lenght == text_lenght:
        return True
    #if the text lenght and set lenght are not the same, there are duplicates   
    else:
        return False




test1 = "Pauline"  # Expect True because all letters unique
print(letters(test1))

test2 = "Comfort"  # Expect False because 'o' is repeated
print(letters(test2))