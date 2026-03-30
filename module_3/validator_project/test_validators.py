import pytest
from validators import is_valid_username, is_valid_phone


class TestIsValidUsername:
    """Тесты для функции is_valid_username"""
    
    # Позитивные сценарии (валидные имена)
    def test_valid_username_simple(self):
        """Простое валидное имя из букв"""
        assert is_valid_username("john") is True
    
    def test_valid_username_with_numbers(self):
        """Валидное имя с буквами и цифрами"""
        assert is_valid_username("user123") is True
    
    def test_valid_username_with_underscore(self):
        """Валидное имя с подчеркиванием"""
        assert is_valid_username("john_doe") is True
    
    def test_valid_username_complex(self):
        """Сложное валидное имя с буквами, цифрами и подчеркиванием"""
        assert is_valid_username("user_123_name") is True
    
    def test_valid_username_min_length(self):
        """Валидное имя минимальной длины (3 символа)"""
        assert is_valid_username("abc") is True
    
    def test_valid_username_max_length(self):
        """Валидное имя максимальной длины (20 символов)"""
        assert is_valid_username("abcdefghij1234567890") is True
    
    # Негативные сценарии (невалидные имена)
    def test_invalid_username_empty(self):
        """Пустое имя"""
        assert is_valid_username("") is False
    
    def test_invalid_username_none(self):
        """None вместо имени"""
        assert is_valid_username(None) is False
    
    def test_invalid_username_too_short(self):
        """Имя короче 3 символов"""
        assert is_valid_username("ab") is False
    
    def test_invalid_username_single_char(self):
        """Имя из одного символа"""
        assert is_valid_username("a") is False
    
    def test_invalid_username_too_long(self):
        """Имя длиннее 20 символов"""
        assert is_valid_username("abcdefghij12345678901") is False
    
    def test_invalid_username_with_space(self):
        """Имя с пробелом"""
        assert is_valid_username("john doe") is False
    
    def test_invalid_username_with_dash(self):
        """Имя с дефисом"""
        assert is_valid_username("john-doe") is False
    
    def test_invalid_username_with_special_char(self):
        """Имя со специальным символом"""
        assert is_valid_username("john@doe") is False
    
    def test_invalid_username_cyrillic(self):
        """Имя с кириллицей"""
        assert is_valid_username("иван") is False


class TestIsValidPhone:
    """Тесты для функции is_valid_phone"""
    
    # Позитивные сценарии (валидные номера)
    def test_valid_phone_simple_7(self):
        """Валидный номер начинающийся с 7"""
        assert is_valid_phone("79991234567") is True
    
    def test_valid_phone_simple_8(self):
        """Валидный номер начинающийся с 8"""
        assert is_valid_phone("89991234567") is True
    
    def test_valid_phone_with_spaces(self):
        """Валидный номер с пробелами"""
        assert is_valid_phone("7 999 123 45 67") is True
    
    def test_valid_phone_with_dashes(self):
        """Валидный номер с дефисами"""
        assert is_valid_phone("7-999-123-45-67") is True
    
    def test_valid_phone_with_brackets(self):
        """Валидный номер со скобками"""
        assert is_valid_phone("7 (999) 123-45-67") is True
    
    # Негативные сценарии (невалидные номера)
    def test_invalid_phone_empty(self):
        """Пустой номер"""
        assert is_valid_phone("") is False
    
    def test_invalid_phone_none(self):
        """None вместо номера"""
        assert is_valid_phone(None) is False
    
    def test_invalid_phone_too_short(self):
        """Номер короче 11 цифр"""
        assert is_valid_phone("7999123456") is False
    
    def test_invalid_phone_too_long(self):
        """Номер длиннее 11 цифр"""
        assert is_valid_phone("799912345678") is False
    
    def test_invalid_phone_starts_with_wrong_digit(self):
        """Номер начинающийся не с 7 или 8"""
        assert is_valid_phone("69991234567") is False
    
    def test_invalid_phone_with_letters(self):
        """Номер с буквами"""
        assert is_valid_phone("7999abc4567") is False
    
    def test_invalid_phone_plus_sign(self):
        """Номер с плюсом (не очищается)"""
        assert is_valid_phone("+79991234567") is False
