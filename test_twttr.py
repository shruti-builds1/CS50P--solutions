from twttr import shorten

def test_lowercase() :
    assert shorten('s 1hruti.') == 's 1hrt.'
    assert shorten('twit123 ,ter') == 'twt123 ,tr'


def test_uppercase() :
    assert shorten('LOW,  E5R') == 'LW,  5R'
    assert shorten('UPP,,E67R') == 'PP,,67R'

def test_mixed() :
    assert shorten('S1HR  UTi') == 'S1HR  T'
    assert shorten('pal ,1aK') == 'pl ,1K'