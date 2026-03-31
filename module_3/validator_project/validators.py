def is_valid_username(username):
    """
    Проверяет валидность имени пользователя.
        Args:
        username: Имя пользователя для проверки
        Returns:
        bool: True если имя валидно, False в противном случае
        Требования:
        - Не пустое
        - От 3 до 20 символов
        - Содержит только буквы, цифры и подчеркивание
    """
    # Проверка на пустоту
    if not username:
        return False
    
    # Проверка длины
    if len(username) < 3 or len(username) > 20:
        return False
    
    # Проверка на допустимые символы (только латинские буквы, цифры, подчеркивание)
    for char in username:
        if not (char.isascii() and (char.isalnum() or char == '_')):
            return False
    
    return True


def is_valid_phone(phone):
    """
    Проверяет валидность телефонного номера.
        Args:
        phone: Телефонный номер для проверки
        Returns:
        bool: True если номер валиден, False в противном случае
        Требования:
        - Содержит ровно 11 цифр
        - Начинается с 7 или 8 (для России)
    """
    # Проверка на пустоту
    if not phone:
        return False
    
    # Удаляем пробелы, тире и скобки (если есть)
    cleaned_phone = phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    
    # Проверяем что остались только цифры
    if not cleaned_phone.isdigit():
        return False
    
    # Проверяем длину
    if len(cleaned_phone) != 11:
        return False
    
    # Проверяем первую цифру (должна быть 7 или 8)
    if cleaned_phone[0] not in ['7', '8']:
        return False
    
    return True
