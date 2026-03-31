import re


# ============================================================================
# TASK 1: EmailValidator
# ============================================================================

class EmailValidator:
    """Валидатор для проверки email адресов"""
    
    def is_valid(self, email):
        """
        Проверяет валидность email адреса.
        
        Args:
            email (str): Email адрес для проверки
            
        Returns:
            bool: True если email валиден, False в противном случае
        """
        if not email or not isinstance(email, str):
            return False
        
        # Простая регулярная выражение для проверки email
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_pattern, email))


# ============================================================================
# TASK 2: Temperature Conversion
# ============================================================================

def celsius_to_fahrenheit(celsius):
    """
    Конвертирует температуру из Цельсия в Фаренгейт.
    
    Args:
        celsius (float): Температура в Цельсиях
        
    Returns:
        float: Температура в Фаренгейтах
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Конвертирует температуру из Фаренгейта в Цельсий.
    
    Args:
        fahrenheit (float): Температура в Фаренгейтах
        
    Returns:
        float: Температура в Цельсиях
    """
    return (fahrenheit - 32) * 5/9


# ============================================================================
# TASK 3: UserValidator
# ============================================================================

class UserValidator:
    """Валидатор для проверки данных пользователя"""
    
    def is_valid_username(self, username):
        """
        Проверяет валидность имени пользователя.
        
        Требования:
            - Не пустое
            - От 3 до 20 символов
            - Содержит только буквы, цифры и подчеркивание
            - Начинается с буквы
            
        Args:
            username (str): Имя пользователя для проверки
            
        Returns:
            bool: True если имя валидно, False в противном случае
        """
        if not username or not isinstance(username, str):
            return False
        
        if len(username) < 3 or len(username) > 20:
            return False
        
        if not username[0].isalpha():
            return False
        
        for char in username:
            if not (char.isalnum() or char == '_'):
                return False
        
        return True
    
    def is_valid_password(self, password):
        """
        Проверяет валидность пароля.
        
        Требования:
            - Не пустой
            - Минимум 8 символов
            - Содержит минимум одну заглавную букву
            - Содержит минимум одну строчную букву
            - Содержит минимум одну цифру
            - Содержит минимум один специальный символ (!@#$%^&*)
            
        Args:
            password (str): Пароль для проверки
            
        Returns:
            bool: True если пароль валиден, False в противном случае
        """
        if not password or not isinstance(password, str):
            return False
        
        if len(password) < 8:
            return False
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in '!@#$%^&*' for c in password)
        
        return has_upper and has_lower and has_digit and has_special
    
    def is_valid_age(self, age):
        """
        Проверяет валидность возраста.
        
        Требования:
            - Целое число
            - От 18 до 120 лет
            
        Args:
            age (int): Возраст для проверки
            
        Returns:
            bool: True если возраст валиден, False в противном случае
        """
        if not isinstance(age, int) or isinstance(age, bool):
            return False
        
        return 18 <= age <= 120
