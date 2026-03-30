from calculator import add, subtract, multiply, divide

def test_add():
    """Test the add function with positive, negative, and zero values."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test the subtract function with positive, negative, and zero values."""
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 0) == 0

def test_multiply():
    """Test the multiply function with positive, negative, and zero values."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0

def test_divide():
    """Test the divide function with positive, negative, and zero numerator."""
    assert divide(6, 2) == 3
    assert divide(1, 1) == 1
    assert divide(0, 1) == 0