def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"
	
print (open("Test_data/test.txt").read())

def test_abs3():
    text = open("Test_data/test.txt").read()
    assert "PYTEST!!!!!" == text, text