from bank import value


def test_incorrect():
    assert value("Greetigs") == 100


def test_case_insensitivity():
    assert value("HELLO") == 0
    assert value("hello") == 0


def test_entire_phrase():
    assert value("Hello, world") == 0
    assert value("Greetings, world") == 100
    assert value("Hi, world") == 20

