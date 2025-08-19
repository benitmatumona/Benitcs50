from bank import value

def test_hello_upper():
    assert value("HELLO Benit") == 0
def test_ello_lower():
    assert value("hello Benit") == 0
def test_capitalise_hello():
    assert value("Hello Benit") == 0
def test_h_upper():
    assert value("HI Benit") == 20
def test_h_lower():
    assert value("hi Benit") == 20
def test_capitalise_h():
    assert value("Hi Benit") == 20
def test_empty():
    assert value("") == 100
def test_other_string():
    assert value("Good day Benit") == 100

