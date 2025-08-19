from plates import is_valid as valid

def test_valid_lenght():
    assert valid("B") == False
    assert valid("Bbbbbbb") == False
def test_begins_letters():
    assert valid("1B") == False
    assert valid("22") == False
def test_ends_numbers():
    assert valid("BB123B") == False
    assert valid("BB0123") == False
def test_no_other_char():
    assert valid("BB1,23") == False
    assert valid("BB1 12") == False
    assert valid("AB1") == True
    assert valid("ABC123") == True
