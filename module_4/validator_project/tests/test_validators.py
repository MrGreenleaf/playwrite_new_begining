import pytest
import sys
from pathlib import Path

# Добавляем src директорию в sys.path чтобы импортировать validators
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from validators import (
    EmailValidator, 
    UserValidator, 
    celsius_to_fahrenheit,
    fahrenheit_to_celsius
)


# ============================================================================
# TASK 1: TESTS FOR EMAIL VALIDATOR
# ============================================================================

class TestEmailValidator:
    """Тесты для EmailValidator с фикстурой"""
    
    def test_valid_email_simple(self, email_validator):
        """Тест валидного простого email"""
        assert email_validator.is_valid("john@example.com") is True
    
    def test_valid_email_with_numbers(self, email_validator):
        """Тест валидного email с цифрами"""
        assert email_validator.is_valid("john123@example.com") is True
    
    def test_valid_email_with_dots(self, email_validator):
        """Тест валидного email с точками"""
        assert email_validator.is_valid("john.doe@example.co.uk") is True
    
    def test_invalid_email_no_at_sign(self, email_validator):
        """Тест невалидного email без @"""
        assert email_validator.is_valid("johnexample.com") is False
    
    def test_invalid_email_empty(self, email_validator):
        """Тест невалидного пустого email"""
        assert email_validator.is_valid("") is False
    
    def test_invalid_email_none(self, email_validator):
        """Тест невалидного None"""
        assert email_validator.is_valid(None) is False
    
    def test_invalid_email_no_domain(self, email_validator):
        """Тест невалидного email без домена"""
        assert email_validator.is_valid("john@") is False
    
    def test_invalid_email_no_top_level_domain(self, email_validator):
        """Тест невалидного email без расширения домена"""
        assert email_validator.is_valid("john@example") is False
    
    def test_valid_email_with_plus(self, email_validator):
        """Тест валидного email с плюсом"""
        assert email_validator.is_valid("john+tag@example.com") is True


# ============================================================================
# TASK 2: PARAMETRIZED TESTS FOR TEMPERATURE CONVERSION
# ============================================================================

class TestTemperatureConversion:
    """Тесты для конвертации температуры с параметризацией"""
    
    @pytest.mark.parametrize("celsius,fahrenheit", [
        (0, 32),
        (100, 212),
        (-40, -40),
        (-273.15, -459.67),
        (20, 68),
        (37, 98.6),
        (1000, 1832),
    ], ids=[
        "freezing",
        "boiling",
        "equal_point",
        "absolute_zero",
        "room_temperature",
        "body_temperature",
        "very_hot",
    ])
    def test_celsius_to_fahrenheit(self, celsius, fahrenheit):
        """Параметризованный тест конвертации Цельсий -> Фаренгейт"""
        result = celsius_to_fahrenheit(celsius)
        assert abs(result - fahrenheit) < 0.01  # Допуск 0.01 градуса
    
    @pytest.mark.parametrize("fahrenheit,celsius", [
        (32, 0),
        (212, 100),
        (-40, -40),
        (-459.67, -273.15),
        (68, 20),
        (98.6, 37),
        (1832, 1000),
    ], ids=[
        "freezing_point",
        "boiling_point",
        "equal_conversion",
        "absolute_zero_f",
        "room_temp",
        "body_temp",
        "very_hot_temp",
    ])
    def test_fahrenheit_to_celsius(self, fahrenheit, celsius):
        """Параметризованный тест конвертации Фаренгейт -> Цельсий"""
        result = fahrenheit_to_celsius(fahrenheit)
        assert abs(result - celsius) < 0.01  # Допуск 0.01 градуса
    
    def test_temperature_round_trip(self):
        """Тест двойной конвертации (туда и обратно)"""
        original = 25.5
        converted = celsius_to_fahrenheit(original)
        back = fahrenheit_to_celsius(converted)
        assert abs(original - back) < 0.01


# ============================================================================
# TASK 3: PARAMETRIZED TESTS WITH MARKERS FOR USER VALIDATOR
# ============================================================================

class TestUserValidatorUsername:
    """Тесты для проверки имени пользователя с параметризацией и маркерами"""
    
    @pytest.mark.validation
    @pytest.mark.parametrize("username,expected", [
        ("john", True),
        ("user123", True),
        ("john_doe", True),
        ("a_b_c_d", True),
        ("user_name_123", True),
        ("", False),
        ("ab", False),
        ("a" * 21, False),
        ("123user", False),
        ("john-doe", False),
        ("john@user", False),
    ], ids=[
        "valid_simple",
        "valid_with_numbers",
        "valid_with_underscore",
        "valid_multiple_underscores",
        "valid_complex",
        "invalid_empty",
        "invalid_too_short",
        "invalid_too_long",
        "invalid_starts_with_digit",
        "invalid_contains_dash",
        "invalid_contains_special_char",
    ])
    def test_is_valid_username(self, user_validator, username, expected):
        """Параметризованный тест для is_valid_username"""
        assert user_validator.is_valid_username(username) == expected


class TestUserValidatorPassword:
    """Тесты для проверки пароля с параметризацией и маркерами"""
    
    @pytest.mark.validation
    @pytest.mark.parametrize("password,expected", [
        ("SecurePass1!", True),
        ("MyPassword123!", True),
        ("Test@Pass99", True),
        ("StrongSecret#5", True),
        ("Complex$Password8", True),
        ("", False),
        ("Short1!", False),
        ("nolowercase123!", False),
        ("NOUPPERCASE123!", False),
        ("NoNumbers!", False),
        ("NoSpecialChar123", False),
    ], ids=[
        "valid_strong",
        "valid_mixed_case",
        "valid_with_special_chars",
        "valid_hash_symbol",
        "valid_dollar_symbol",
        "invalid_empty",
        "invalid_too_short",
        "invalid_no_lowercase",
        "invalid_no_uppercase",
        "invalid_no_digits",
        "invalid_no_special",
    ])
    def test_is_valid_password(self, user_validator, password, expected):
        """Параметризованный тест для is_valid_password"""
        assert user_validator.is_valid_password(password) == expected
    
    @pytest.mark.validation
    @pytest.mark.slow
    def test_password_strength_validation(self, user_validator):
        """Медленный тест проверки надежности пароля"""
        weak_passwords = ["abc123!", "Pass1!", "Test@1!"]
        for pwd in weak_passwords:
            # Проверяем, что короткие пароли отклоняются
            assert user_validator.is_valid_password(pwd) is False


class TestUserValidatorAge:
    """Тесты для проверки возраста с параметризацией и маркерами"""
    
    @pytest.mark.validation
    @pytest.mark.parametrize("age,expected", [
        (18, True),
        (25, True),
        (65, True),
        (120, True),
        (50, True),
        (17, False),
        (121, False),
        (0, False),
        (-5, False),
        (10, False),
    ], ids=[
        "valid_minimum_age",
        "valid_adult",
        "valid_senior",
        "valid_maximum_age",
        "valid_middle_aged",
        "invalid_too_young",
        "invalid_too_old",
        "invalid_zero",
        "invalid_negative",
        "invalid_child",
    ])
    def test_is_valid_age(self, user_validator, age, expected):
        """Параметризованный тест для is_valid_age"""
        assert user_validator.is_valid_age(age) == expected
    
    @pytest.mark.validation
    def test_is_valid_age_not_float(self, user_validator):
        """Тест что возраст должен быть целым числом, не float"""
        assert user_validator.is_valid_age(25.5) is False
    
    @pytest.mark.validation
    def test_is_valid_age_not_boolean(self, user_validator):
        """Тест что булев тип не принимается как возраст"""
        assert user_validator.is_valid_age(True) is False


class TestUserValidatorIntegration:
    """Интеграционные тесты для всего UserValidator"""
    
    @pytest.mark.validation
    def test_complete_valid_user(self, user_validator):
        """Тест полностью валидного пользователя"""
        assert user_validator.is_valid_username("john_doe") is True
        assert user_validator.is_valid_password("SecurePass1!") is True
        assert user_validator.is_valid_age(25) is True
    
    @pytest.mark.validation
    def test_partially_invalid_user(self, user_validator):
        """Тест частично невалидного пользователя"""
        assert user_validator.is_valid_username("123") is False  # Starts with digit
        assert user_validator.is_valid_password("SecurePass1!") is True
        assert user_validator.is_valid_age(25) is True
    
    @pytest.mark.validation
    @pytest.mark.slow
    def test_edge_cases(self, user_validator):
        """Тест граничных случаев"""
        # Username edge cases
        assert user_validator.is_valid_username("abc") is True  # Min length
        assert user_validator.is_valid_username("a" * 20) is True  # Max length
        
        # Age edge cases
        assert user_validator.is_valid_age(18) is True  # Min valid age
        assert user_validator.is_valid_age(120) is True  # Max valid age
