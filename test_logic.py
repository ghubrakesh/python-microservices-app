from mylib.logic import wiki

def test_wiki():
    assert  "DC Comics." in wiki("wonnder Woman", 2)