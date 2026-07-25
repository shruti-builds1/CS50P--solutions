from bank import value

def test_hello() :
    assert value('HELLO!') == 0
    assert value('hello!') == 0
    assert value('HELLO! HOW ARE YOU') == 0
    assert value('hello! how are you') == 0
    assert value('heLLo!') == 0
    assert value('hello! HOW ARE you') == 0

def test_h() :
    assert value("HEY, WHAT'S UP!") == 20
    assert value("hey, what's up!") == 20
    assert value("hey, WHAT'S up!") == 20

def test_other() :
    assert value('GOOD MORNING!') == 100
    assert value('good morning!') == 100
    assert value('good MORNING!') == 100