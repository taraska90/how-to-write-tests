from hash_function import hash_function


def test_general():
    # this number '416' will change after the next time os loading up
    assert hash_function("Test") == 1784

def test_output():
    # output should be int
    types = [3.14, True, "Test", ["a", "b"], {1: 2}]
    for ty in types:
        assert isinstance(hash_function(ty), int)

def test_distinct_object():
    # testing that 3.14 and "3.14" it is a different object and not
    # should not be the same
    pi_float = 3.14
    pi_string = "3.14"
    hash_from_float = hash_function(pi_float)
    hash_from_string = hash_function(pi_string)
    assert hash_from_float is not hash_from_string

def test_anagram():
    str1 = hash_function("Loren")
    str1_anagram = hash_function("Loner")
    assert str1 is not str1_anagram

def test_input():
    pass
    # input could any type
    #assert hash_function(123) == "Error. Input should be string"
