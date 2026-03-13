import os

if os.path.exists('data.txt'):
    while True:
        print('(1) - show content')
        print('(2) - add new name')
        print('(3) - delete name')
        print('(4) - exit')
        action = input('Select action: ')
        if action == '1':
            with open("data.txt", "r") as file:
                print(file.read())
        elif action == '2':
            new_name = input('Which name do you want to add? ')
            with open("data.txt", "a") as file:
                file.write(f"{new_name}\n")
        elif action == '3':
            name_to_delete = input('name to delete: ')
            with open("data.txt", "r") as file:
                lines = file.readlines()
            with open("data.txt", "w") as file:
                for line in lines:
                    if line.strip() != name_to_delete:
                        file.write(line)
        else:
            break
else:
    with open("data.txt", "w") as file:
        file.write('Vasya\n')
        file.write('Petya\n')
        file.write('Slava\n')