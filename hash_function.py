# make my first hash function
import sys

def hash_function(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key), start=1)
    )


if __name__ == "__main__":
    arg = sys.argv[1]
    print(hash_function(arg))
