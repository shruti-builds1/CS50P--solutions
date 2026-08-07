from um import count

def test_case() :
    assert count('hello,um,world') == 1
    assert count('hello,Um?world') == 1
    assert count('hello,uM,world') == 1
    assert count('hello,UM world') == 1

def test_words() :
    assert count('albums') == 0
    assert count('yummmy') == 0
    assert count('Mum') == 0

def test_mixed() :
    assert count('hello um world') == 1
    # assert count('hello45um78world') == 1
    assert count('hello ummm, world') == 0