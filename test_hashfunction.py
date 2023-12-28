from hash_function import hash_function


def test_general():
    # this number '416' will change after the next time os loading up
    assert hash_function("Test") == 416

def test_output():
    # when input string, output should be int
    assert isinstance(hash_function("Test"), int)


def test_input():
    # input should be str
    assert hash_function(123) == "Error. Input should be string"
