from um import count

def test_um():
    assert count("um") == 1

def test_um_upper():
    assert count("UM") == 1

def test_char():
    assert count("Um, um") == 2

def test_word():
    assert count("Thumb") == 0
