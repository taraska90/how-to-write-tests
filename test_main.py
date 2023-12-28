def f():
    return 4

def test_function():
    assert f() == 4

def test_always_passes():
    assert True


def test_always_failes():
    assert True

def test_upper_case():
    assert "small_register".upper() == "SMALL_REGISTER"

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }