import random

number = random.randint(1, 100)
print('I zagadal number from 1 to 100')
count = 0
answer = 0

while True:
    answer = int(input('Guess my number: '))
    count += 1
    if answer == number:
        print(f'Hell yeah, mf, it took {count} tries, my number was {number}')
        break
    elif answer > number:
        print('Menshe')
    elif answer < number:
        print('Bolshe')