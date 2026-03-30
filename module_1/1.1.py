a = int(input('enter a '))
b = int(input('enter b '))
operation = input('enter operation (+, -, *, /) or n to exit ')
if operation == '+':
    result = a + b
    print(result)
elif operation == '-':
    result = a - b
    print(result)
elif operation == '*':
    result = a * b
    print(result)
elif operation == '/':
    result = a / b
    print(result)
else:
    print('you are exited')