from plates import is_valid

def test_length() :
    assert is_valid('HELLO') == True
    assert is_valid('HELLO WORLD') == False
    assert is_valid('GOODBYE') == False
    assert is_valid('CS') == True


def test_alpha() :
    assert is_valid('PA12') == True
    assert is_valid('11') == False

def test_alnum() :
    assert is_valid('PI.3') == False
    assert is_valid('PIK3') == True

def test_digit() :
    assert is_valid('CS50P') == False
    assert is_valid('CS05P') == False
    assert is_valid('CS059') == False
    assert is_valid('CSP50') == True