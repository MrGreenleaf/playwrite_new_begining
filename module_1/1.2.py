prod_list = []
while True:
    print('=== List of pokupki===')
    print('(1) Add')
    print('(2) Show')
    print('(3) Delete')
    print('(4) Exit')
    action = input('Select action: ')
    if action == '1':
        new_item = input('What to add: ')
        prod_list.append(new_item)
    elif action == '2':
        print(prod_list)
    elif action == '3':
        item_to_delete = input('What to delete: ')
        prod_list.remove(item_to_delete)
    else:
        break