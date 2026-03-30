import json
import os

while True:
    print('(1) - add contact')
    print('(2) - show all contacts')
    print('(3) - find by name')
    print('(4) - delete')
    print('(5) - exit')
    action = input('Select action: ')

    if action == '1':
        # Загружаем существующие контакты
        if os.path.exists('contacts.json'):
            with open('contacts.json', 'r', encoding='utf-8') as file:
                contacts = json.load(file)
        else:
            contacts = []

        name = input('name: ').strip()
        if not name:
            print("Name cannot be empty!")
            continue

        phone = input('phone: ')
        email = input('email: ')
        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }
        contacts.append(contact)

        with open('contacts.json', 'w', encoding='utf-8') as file:
            json.dump(contacts, file, ensure_ascii=False, indent=2)
        print("Contact added.")

    elif action == '2':
        if not os.path.exists('contacts.json'):
            print("No contacts yet.")
            continue
        with open('contacts.json', 'r', encoding='utf-8') as file:
            contacts = json.load(file)
        if not contacts:
            print("No contacts.")
        else:
            for contact in contacts:
                print(f"{contact['name']} - {contact['phone']} - {contact['email']}")

    elif action == '3':
        if not os.path.exists('contacts.json'):
            print("No contacts yet.")
            continue
        name = input('Enter name to search: ').strip()
        if not name:
            print("Please enter a name!")
            continue
        with open('contacts.json', 'r', encoding='utf-8') as file:
            contacts = json.load(file)
        found = False
        for contact in contacts:
            if contact['name'].lower() == name.lower():  # поиск без учёта регистра
                print(f"{contact['phone']} - {contact['email']}")
                found = True
        if not found:
            print("Not found.")

    elif action == '4':
        if not os.path.exists('contacts.json'):
            print("No contacts yet.")
            continue
        name = input('Enter name to delete: ').strip()
        if not name:
            print("Please enter a name!")
            continue
        with open('contacts.json', 'r', encoding='utf-8') as file:
            contacts = json.load(file)
        original_count = len(contacts)
        contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
        if len(contacts) < original_count:
            with open('contacts.json', 'w', encoding='utf-8') as file:
                json.dump(contacts, file, ensure_ascii=False, indent=2)
            print("Deleted.")
        else:
            print("Name not found.")

    elif action == '5':
        break
    else:
        print("Invalid action, try again.")