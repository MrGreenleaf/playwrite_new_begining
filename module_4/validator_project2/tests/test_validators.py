def test_valid_email(validator):
    assert validator.is_valid("john@example.com") == True

def test_invalid_email(validator):
    assert validator.is_valid("invalid-email") == False 

def test_empty_email(validator):
    assert validator.is_valid("") == False

def test_none_email(validator):
    assert validator.is_valid(None) == False

def test_email_with_spaces(validator):
    assert validator.is_valid("john doe@example.com") == False