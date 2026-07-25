import pytest

import fuel

def test_fraction() :
    assert fuel.convert('0/100') == 0
    assert fuel.convert('1/100') == 1
    assert fuel.convert('3/4') == 75
    assert fuel.convert('99/100') == 99
    assert fuel.convert('4/4') == 100

def test_percent() :
    assert fuel.gauge(0) == f'E'
    assert fuel.gauge(1) == f'E'
    assert fuel.gauge(75) == f'75%'
    assert fuel.gauge(99) == f'F'
    assert fuel.gauge(100) == f'F'


def test_exception1() :
    with pytest.raises(ValueError) :
        fuel.convert('5/4')
    with pytest.raises(ValueError) :
        fuel.convert('-1/4')
    with pytest.raises(ValueError) :
        fuel.convert('1/-4')
    with pytest.raises(ValueError) :
        fuel.convert('cat/dog')

def test_exception2() :
    with pytest.raises(ZeroDivisionError) :
        fuel.convert('5/0')