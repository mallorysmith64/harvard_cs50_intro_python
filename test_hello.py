from hello import hello
    
def test_default():
    assert hello() == "Hello, world!"
    
def test_argument():
    assert hello("David") == "Hello, David!"

def test_another_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"Hello, {name}!"