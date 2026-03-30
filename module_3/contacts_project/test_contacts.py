import pytest
from contacts import (
    add_contact, show_all_contacts, find_contact, find_all_by_name,
    delete_contact, get_contact_by_phone, update_contact,
    get_contacts_count, clear_all_contacts
)


class TestAddContact:
    """Тесты для функции add_contact"""
    
    def test_add_valid_contact(self):
        """Добавление валидного контакта"""
        contacts = []
        result = add_contact(contacts, "John", "1234567890", "john@email.com")
        assert result is True
        assert len(contacts) == 1
        assert contacts[0]['name'] == "John"
    
    def test_add_contact_with_empty_phone_email(self):
        """Добавление контакта с пустыми телефоном и email"""
        contacts = []
        result = add_contact(contacts, "Alice", "", "")
        assert result is True
        assert len(contacts) == 1
        assert contacts[0]['phone'] == ""
        assert contacts[0]['email'] == ""
    
    def test_add_multiple_contacts(self):
        """Добавление нескольких контактов"""
        contacts = []
        add_contact(contacts, "John", "111", "john@email.com")
        add_contact(contacts, "Jane", "222", "jane@email.com")
        add_contact(contacts, "Bob", "333", "bob@email.com")
        assert len(contacts) == 3
    
    def test_add_contact_empty_name(self):
        """Попытка добавления контакта с пустым именем"""
        contacts = []
        result = add_contact(contacts, "", "1234567890", "email@test.com")
        assert result is False
        assert len(contacts) == 0
    
    def test_add_contact_whitespace_name(self):
        """Попытка добавления контакта с пробелами вместо имени"""
        contacts = []
        result = add_contact(contacts, "   ", "1234567890", "email@test.com")
        assert result is False
        assert len(contacts) == 0
    
    def test_add_contact_none_name(self):
        """Попытка добавления контакта с None в качестве имени"""
        contacts = []
        result = add_contact(contacts, None, "1234567890", "email@test.com")
        assert result is False
        assert len(contacts) == 0
    
    def test_add_contact_with_whitespace_trimming(self):
        """Добавление контакта с пробелами, которые должны быть обрезаны"""
        contacts = []
        add_contact(contacts, "  John  ", "  123  ", "  john@email.com  ")
        assert contacts[0]['name'] == "John"
        assert contacts[0]['phone'] == "123"
        assert contacts[0]['email'] == "john@email.com"


class TestShowAllContacts:
    """Тесты для функции show_all_contacts"""
    
    def test_show_empty_contacts(self):
        """Показать пустой список контактов"""
        contacts = []
        result = show_all_contacts(contacts)
        assert result == []
    
    def test_show_single_contact(self):
        """Показать один контакт"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = show_all_contacts(contacts)
        assert len(result) == 1
        assert "John" in result[0]
        assert "111" in result[0]
        assert "john@email.com" in result[0]
    
    def test_show_multiple_contacts(self):
        """Показать несколько контактов"""
        contacts = [
            {"name": "John", "phone": "111", "email": "john@email.com"},
            {"name": "Jane", "phone": "222", "email": "jane@email.com"},
            {"name": "Bob", "phone": "333", "email": "bob@email.com"}
        ]
        result = show_all_contacts(contacts)
        assert len(result) == 3
        assert all(isinstance(line, str) for line in result)
    
    def test_show_contact_format(self):
        """Проверка формата вывода контакта"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = show_all_contacts(contacts)
        assert result[0] == "John - 111 - john@email.com"


class TestFindContact:
    """Тесты для функции find_contact"""
    
    def test_find_existing_contact(self):
        """Найти существующий контакт"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = find_contact(contacts, "John")
        assert result is not None
        assert result['name'] == "John"
    
    def test_find_contact_case_insensitive(self):
        """Поиск контакта без учета регистра"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = find_contact(contacts, "john")
        assert result is not None
        assert result['name'] == "John"
        
        result = find_contact(contacts, "JOHN")
        assert result is not None
    
    def test_find_nonexistent_contact(self):
        """Поиск несуществующего контакта"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = find_contact(contacts, "Jane")
        assert result is None
    
    def test_find_contact_empty_name(self):
        """Поиск с пустым именем"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = find_contact(contacts, "")
        assert result is None
    
    def test_find_contact_none_name(self):
        """Поиск с None в качестве имени"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = find_contact(contacts, None)
        assert result is None
    
    def test_find_contact_in_empty_list(self):
        """Поиск в пустом списке контактов"""
        contacts = []
        result = find_contact(contacts, "John")
        assert result is None


class TestFindAllByName:
    """Тесты для функции find_all_by_name"""
    
    def test_find_all_exact_match(self):
        """Найти контакты с точным совпадением имени"""
        contacts = [
            {"name": "John", "phone": "111", "email": "john@email.com"},
            {"name": "John", "phone": "222", "email": "john2@email.com"}
        ]
        result = find_all_by_name(contacts, "John")
        assert len(result) == 2
    
    def test_find_all_partial_match(self):
        """Найти контакты с частичным совпадением"""
        contacts = [
            {"name": "John", "phone": "111", "email": "john@email.com"},
            {"name": "Johnny", "phone": "222", "email": "johnny@email.com"},
            {"name": "Jane", "phone": "333", "email": "jane@email.com"}
        ]
        result = find_all_by_name(contacts, "John")
        assert len(result) == 2
        assert any(c['name'] == "John" for c in result)
        assert any(c['name'] == "Johnny" for c in result)
    
    def test_find_all_no_matches(self):
        """Поиск без совпадений"""
        contacts = [
            {"name": "John", "phone": "111", "email": "john@email.com"},
            {"name": "Jane", "phone": "222", "email": "jane@email.com"}
        ]
        result = find_all_by_name(contacts, "Bob")
        assert len(result) == 0
    
    def test_find_all_case_insensitive(self):
        """Поиск без учета регистра"""
        contacts = [
            {"name": "John", "phone": "111", "email": "john@email.com"},
            {"name": "JOHN", "phone": "222", "email": "john2@email.com"}
        ]
        result = find_all_by_name(contacts, "john")
        assert len(result) == 2
    
    def test_find_all_empty_list(self):
        """Поиск в пустом списке"""
        contacts = []
        result = find_all_by_name(contacts, "John")
        assert len(result) == 0
    
    def test_find_all_empty_search_name(self):
        """Поиск с пустым именем"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = find_all_by_name(contacts, "")
        assert len(result) == 0


class TestDeleteContact:
    """Тесты для функции delete_contact"""
    
    def test_delete_existing_contact(self):
        """Удалить существующий контакт"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = delete_contact(contacts, "John")
        assert result is True
        assert len(contacts) == 0
    
    def test_delete_from_multiple_contacts(self):
        """Удалить контакт из нескольких контактов"""
        contacts = [
            {"name": "John", "phone": "111", "email": "john@email.com"},
            {"name": "Jane", "phone": "222", "email": "jane@email.com"},
            {"name": "Bob", "phone": "333", "email": "bob@email.com"}
        ]
        result = delete_contact(contacts, "Jane")
        assert result is True
        assert len(contacts) == 2
        assert not any(c['name'] == "Jane" for c in contacts)
    
    def test_delete_nonexistent_contact(self):
        """Попытка удалить несуществующий контакт"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = delete_contact(contacts, "Jane")
        assert result is False
        assert len(contacts) == 1
    
    def test_delete_case_insensitive(self):
        """Удаление без учета регистра"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = delete_contact(contacts, "john")
        assert result is True
        assert len(contacts) == 0
    
    def test_delete_empty_name(self):
        """Попытка удаления с пустым именем"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = delete_contact(contacts, "")
        assert result is False
        assert len(contacts) == 1
    
    def test_delete_from_empty_list(self):
        """Удаление из пустого списка"""
        contacts = []
        result = delete_contact(contacts, "John")
        assert result is False


class TestGetContactByPhone:
    """Тесты для функции get_contact_by_phone"""
    
    def test_get_contact_by_valid_phone(self):
        """Получить контакт по válидному номеру телефона"""
        contacts = [{"name": "John", "phone": "1234567890", "email": "john@email.com"}]
        result = get_contact_by_phone(contacts, "1234567890")
        assert result is not None
        assert result['name'] == "John"
    
    def test_get_contact_by_invalid_phone(self):
        """Попытка получить контакт по неверному номеру"""
        contacts = [{"name": "John", "phone": "1234567890", "email": "john@email.com"}]
        result = get_contact_by_phone(contacts, "0987654321")
        assert result is None
    
    def test_get_contact_by_phone_empty_phone(self):
        """Поиск с пустым номером телефона"""
        contacts = [{"name": "John", "phone": "1234567890", "email": "john@email.com"}]
        result = get_contact_by_phone(contacts, "")
        assert result is None
    
    def test_get_contact_by_phone_in_empty_list(self):
        """Поиск по телефону в пустом списке"""
        contacts = []
        result = get_contact_by_phone(contacts, "1234567890")
        assert result is None
    
    def test_get_contact_with_whitespace_trimming(self):
        """Поиск с обрезкой пробелов"""
        contacts = [{"name": "John", "phone": "123", "email": "john@email.com"}]
        result = get_contact_by_phone(contacts, "  123  ")
        assert result is not None


class TestUpdateContact:
    """Тесты для функции update_contact"""
    
    def test_update_phone(self):
        """Обновить номер телефона контакта"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = update_contact(contacts, "John", phone="999")
        assert result is True
        assert contacts[0]['phone'] == "999"
        assert contacts[0]['email'] == "john@email.com"
    
    def test_update_email(self):
        """Обновить email контакта"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = update_contact(contacts, "John", email="newemail@test.com")
        assert result is True
        assert contacts[0]['email'] == "newemail@test.com"
        assert contacts[0]['phone'] == "111"
    
    def test_update_both_phone_and_email(self):
        """Обновить телефон и email"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = update_contact(contacts, "John", phone="999", email="new@email.com")
        assert result is True
        assert contacts[0]['phone'] == "999"
        assert contacts[0]['email'] == "new@email.com"
    
    def test_update_nonexistent_contact(self):
        """Попытка обновить несуществующий контакт"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = update_contact(contacts, "Jane", phone="999")
        assert result is False
        assert len(contacts) == 1
    
    def test_update_case_insensitive(self):
        """Обновление без учета регистра"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = update_contact(contacts, "john", phone="999")
        assert result is True
        assert contacts[0]['phone'] == "999"
    
    def test_update_empty_name(self):
        """Попытка обновления с пустым именем"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        result = update_contact(contacts, "", phone="999")
        assert result is False


class TestGetContactsCount:
    """Тесты для функции get_contacts_count"""
    
    def test_count_empty_list(self):
        """Количество контактов в пустом списке"""
        contacts = []
        assert get_contacts_count(contacts) == 0
    
    def test_count_single_contact(self):
        """Количество для одного контакта"""
        contacts = [{"name": "John", "phone": "111", "email": "john@email.com"}]
        assert get_contacts_count(contacts) == 1
    
    def test_count_multiple_contacts(self):
        """Количество для нескольких контактов"""
        contacts = [
            {"name": "John", "phone": "111", "email": "john@email.com"},
            {"name": "Jane", "phone": "222", "email": "jane@email.com"},
            {"name": "Bob", "phone": "333", "email": "bob@email.com"}
        ]
        assert get_contacts_count(contacts) == 3
    
    def test_count_after_adding(self):
        """Количество после добавления контакта"""
        contacts = []
        add_contact(contacts, "John", "111", "john@email.com")
        assert get_contacts_count(contacts) == 1


class TestClearAllContacts:
    """Тесты для функции clear_all_contacts"""
    
    def test_clear_empty_list(self):
        """Очистить пустой список"""
        contacts = []
        clear_all_contacts(contacts)
        assert len(contacts) == 0
    
    def test_clear_with_contacts(self):
        """Очистить список с контактами"""
        contacts = [
            {"name": "John", "phone": "111", "email": "john@email.com"},
            {"name": "Jane", "phone": "222", "email": "jane@email.com"},
            {"name": "Bob", "phone": "333", "email": "bob@email.com"}
        ]
        clear_all_contacts(contacts)
        assert len(contacts) == 0
        assert contacts == []


class TestIntegration:
    """Интеграционные тесты для проверки работы функций вместе"""
    
    def test_add_find_delete_workflow(self):
        """Сценарий: добавить, найти, удалить"""
        contacts = []
        
        # Добавляем контакт
        add_contact(contacts, "John", "111", "john@email.com")
        assert get_contacts_count(contacts) == 1
        
        # Находим контакт
        found = find_contact(contacts, "John")
        assert found is not None
        
        # Удаляем контакт
        assert delete_contact(contacts, "John") is True
        assert get_contacts_count(contacts) == 0
    
    def test_multiple_operations(self):
        """Сценарий: несколько операций подряд"""
        contacts = []
        
        # Добавляем контакты
        add_contact(contacts, "John", "111", "john@email.com")
        add_contact(contacts, "Jane", "222", "jane@email.com")
        add_contact(contacts, "Johnny", "333", "johnny@email.com")
        
        assert get_contacts_count(contacts) == 3
        
        # Ищем по фамилии
        found_all = find_all_by_name(contacts, "John")
        assert len(found_all) == 2
        
        # Обновляем контакт
        assert update_contact(contacts, "Jane", phone="999") is True
        
        # Проверяем количество
        assert get_contacts_count(contacts) == 3
        
        # Удаляем контакт
        assert delete_contact(contacts, "Johnny") is True
        assert get_contacts_count(contacts) == 2
    
    def test_show_contacts_after_operations(self):
        """Показать контакты после различных операций"""
        contacts = []
        
        add_contact(contacts, "Alice", "111", "alice@email.com")
        add_contact(contacts, "Bob", "222", "bob@email.com")
        
        display = show_all_contacts(contacts)
        assert len(display) == 2
        
        delete_contact(contacts, "Alice")
        display = show_all_contacts(contacts)
        assert len(display) == 1
