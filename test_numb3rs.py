from numb3rs import validate

def test_digits() :
    assert validate('0.0.0.0') == True
    assert validate('1.23.34.45') == True
    assert validate('159.0.4.45') == True
    assert validate('255.255.255.255') == True
    assert validate('100.001.167.196') == False
    assert validate('459.234.34.45') == False
    assert validate('1.23.34.45.78') == False
    assert validate('01.23.34.05') == False
    assert validate('1.23.34') == False
    assert validate('10.89.010.000') == False
    assert validate('1.23.34.00') == False
    assert validate('45.2034.34.495') == False

def test_mixed() :
    assert validate('1.23.34.cat') == False
    assert validate('dog') == False
    assert validate('1009.23.3e4.45.78ae') == False
    assert validate('1.23.3A4.7/8') == False