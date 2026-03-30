def add_contact(contacts, name, phone, email):
    """
    Добавляет новый контакт в список.
    
    Args:
        contacts (list): Список контактов
        name (str): Имя контакта
        phone (str): Номер телефона
        email (str): Email адрес
    
    Returns:
        bool: True если контакт добавлен, False если имя пустое
    """
    if not name or not name.strip():
        return False
    
    contact = {
        "name": name.strip(),
        "phone": phone.strip() if phone else "",
        "email": email.strip() if email else ""
    }
    contacts.append(contact)
    return True


def show_all_contacts(contacts):
    """
    Возвращает список всех контактов в формате строк.
    
    Args:
        contacts (list): Список контактов
    
    Returns:
        list: Список строк с информацией о контактах
    """
    if not contacts:
        return []
    
    result = []
    for contact in contacts:
        line = f"{contact['name']} - {contact['phone']} - {contact['email']}"
        result.append(line)
    return result


def find_contact(contacts, name):
    """
    Ищет контакт по имени (без учета регистра).
    
    Args:
        contacts (list): Список контактов
        name (str): Имя для поиска
    
    Returns:
        dict or None: Найденный контакт или None
    """
    if not name or not name.strip():
        return None
    
    search_name = name.strip().lower()
    for contact in contacts:
        if contact['name'].lower() == search_name:
            return contact
    
    return None


def find_all_by_name(contacts, name):
    """
    Ищет все контакты, содержащие имя (частичный поиск).
    
    Args:
        contacts (list): Список контактов
        name (str): Имя для поиска
    
    Returns:
        list: Список найденных контактов
    """
    if not name or not name.strip():
        return []
    
    search_name = name.strip().lower()
    result = []
    for contact in contacts:
        if search_name in contact['name'].lower():
            result.append(contact)
    
    return result


def delete_contact(contacts, name):
    """
    Удаляет контакт по имени (без учета регистра).
    
    Args:
        contacts (list): Список контактов
        name (str): Имя контакта для удаления
    
    Returns:
        bool: True если контакт удален, False если не найден
    """
    if not name or not name.strip():
        return False
    
    search_name = name.strip().lower()
    original_length = len(contacts)
    
    # Удаляем контакт с совпадающим именем
    contacts[:] = [
        contact for contact in contacts 
        if contact['name'].lower() != search_name
    ]
    
    return len(contacts) < original_length


def get_contact_by_phone(contacts, phone):
    """
    Ищет контакт по номеру телефона.
    
    Args:
        contacts (list): Список контактов
        phone (str): Номер телефона
    
    Returns:
        dict or None: Найденный контакт или None
    """
    if not phone or not phone.strip():
        return None
    
    search_phone = phone.strip()
    for contact in contacts:
        if contact['phone'] == search_phone:
            return contact
    
    return None


def update_contact(contacts, name, phone=None, email=None):
    """
    Обновляет информацию контакта.
    
    Args:
        contacts (list): Список контактов
        name (str): Имя контакта
        phone (str): Новый номер телефона (опционально)
        email (str): Новый email (опционально)
    
    Returns:
        bool: True если контакт обновлен, False если не найден
    """
    if not name or not name.strip():
        return False
    
    search_name = name.strip().lower()
    for contact in contacts:
        if contact['name'].lower() == search_name:
            if phone is not None:
                contact['phone'] = phone.strip()
            if email is not None:
                contact['email'] = email.strip()
            return True
    
    return False


def get_contacts_count(contacts):
    """
    Возвращает количество контактов.
    
    Args:
        contacts (list): Список контактов
    
    Returns:
        int: Количество контактов
    """
    return len(contacts)


def clear_all_contacts(contacts):
    """
    Удаляет все контакты.
    
    Args:
        contacts (list): Список контактов
    
    Returns:
        None
    """
    contacts.clear()
