import pytest
from seasons import age

def test_no_dash():
    with pytest.raises(SystemExit, match = "Invalid date"):
        age("2000 10 12")

def test_invalid_order():
    with pytest.raises(SystemExit, match = "Invalid date"):
        age("12-10-2000")

def test_invalid_day():
    with pytest.raises(SystemExit, match = "Invalid date"):
        age("2000-02-30")

def test_invalid_month():
    with pytest.raises(SystemExit, match = "Invalid date"):
        age("2000-13-30")

def test_invalid_format():
    with pytest.raises(SystemExit, match = "Invalid date"):
        age("2000 october 12")

def test_valid():
    assert age("2000-01-01") == "Thirteen million, four hundred eighty-one thousand, two hundred eighty minutes"
