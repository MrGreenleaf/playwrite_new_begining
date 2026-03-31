from calculator import add, divide, subtract, multiply


def test_add_positive():
    assert add(2, 3) == 5

def test_add_pos_neg():
    assert add(5, -3) == 2

def test_add_both_neg():
    assert add(-4, -6) == -10

def test_add_zero_1():
    assert add(0, 7)

def test_add_big():
    assert add(30000000, 20000) == 30020000

def test_divide():
    assert divide(0, 1) == 0
    assert divide(1, 1) == 1

def test_multiply():
    assert multiply(3, 5) == 15

def test_subtract():
    assert subtract (2, 3) == -1