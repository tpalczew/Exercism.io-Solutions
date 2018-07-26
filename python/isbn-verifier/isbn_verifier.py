import string
def verify(isbn):
    # ISBN Verifier
    
    isbn = isbn.lower() #lower case letters
    isbn = filter(lambda x: x not in string.punctuation, isbn) # no punctuation characters
    isbn = ''.join(isbn.split()) # no white spaces
    isbn = list(isbn)  # as a list
    
    if len(isbn) != 10:
        return False # we need 10 characters to have a valid isbn
    
    for element in isbn[:-1]: # loop over characters up to the one before the last one
        if not element.isdigit(): 
            return False # we can only have letters at the end (last character)
    
    if isbn[-1].isdigit():
        isbn = isbn
    else:
        if isbn[-1] is 'x': # only x in the end is ok
            isbn[-1] = 10
        else:
            return False
    
    isbn = list(map(int, isbn)) # convert list of string to list of ints
    return (isbn[0] * 10 + isbn[1] * 9 + isbn[2] * 8 +
            isbn[3] * 7 + isbn[4] * 6 + isbn[5] * 5 +
            isbn[6] * 4 + isbn[7] * 3 + isbn[8] * 2 +
            isbn[9] * 1) % 11 == 0
     
