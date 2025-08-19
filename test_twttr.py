from twttr import shorten

def test_empty():
    assert shorten("") == ""
def test_vowels():
    assert shorten("AEIOUaeiou") == ""
def test_consonents():
    assert shorten("BCbc") == "BCbc"
def test_numbers():
    assert shorten("1234567") == "1234567"
def test_punctuation():
    assert shorten(",") == ","
def test_all():
    assert shorten("Hi, My name is Benit123") == "H, My nm s Bnt123"

if __name__ == "__main__":
    main()
