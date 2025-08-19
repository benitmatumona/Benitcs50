from fuel import gauge

def test_Full():
    assert gauge(100) == "F"
    assert gauge(90) == "F"

def test_between():
    assert gauge(50) == "50%"
    assert gauge(11) == "11%"

def test_empty():
    assert gauge(10) == "E"
    assert gauge(0) == "E"
