from plates import is_valid


def test_check_start():
    assert is_valid("CS50") == True
    assert is_valid("50") == False
    assert is_valid("a") == False
    assert is_valid("1") == False
    assert is_valid("CS") == True


def test_length():
    assert is_valid("AA") == True
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False
    assert is_valid("AAAAAA") == True


def test_numbers():
    assert is_valid("12345") == False
    assert is_valid("11AA") == False
    assert is_valid("AA11") == True
    assert is_valid("AA11A1") == False
    assert is_valid("AAA11A") == False


def test_zero():
    assert is_valid("00") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_symbols():
    assert is_valid("CS50!") == False
    assert is_valid("3.14") == False