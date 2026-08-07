from working import convert
import pytest

def test_format() :
    assert convert('9 AM to 5 PM') == f'09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == f'09:00 to 17:00'
    assert convert('9 AM to 5:00 PM') == f'09:00 to 17:00'
    assert convert('9:00 AM to 5 PM') == f'09:00 to 17:00'
    assert convert('5 PM to 9 AM') == f'17:00 to 09:00'
    assert convert('5:00 PM to 9:00 AM') == f'17:00 to 09:00'
    assert convert('5:00 PM to 9 AM') == f'17:00 to 09:00'
    assert convert('5 PM to 9:00 AM') == f'17:00 to 09:00'

def test_raise() :
    with pytest.raises(ValueError) :
        convert('12:60 PM to 2:00 PM')

    with pytest.raises(ValueError) :
        convert('12:60 PM 2:00 PM')