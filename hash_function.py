# make my first hash function


def hash_function(text):
    if type(text) is not str:
        return("Error. Input should be string")
    return sum(ord(character) for character in text)
