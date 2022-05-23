from twttr import shorten


def test_no_vowel():
    assert shorten("wrd") == "wrd"


def test_capital_vowel():
    assert shorten("Assert") == "ssrt"


def test_lower_vowel():
    assert shorten("assert") == "ssrt"


def test_numbers():
    assert shorten("CS50") == "CS50"


def test_upper_vowel():
    assert shorten("ASSERT") == "SSRT"


def test_punctuation():
    assert shorten("CS50!") == "CS50!"