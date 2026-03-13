def rub_to_usd(rub):
    """rubli to dollary"""
    bablo = rub * 100
    return bablo

def rub_to_eur(rub):
    """"rubli to euros"""
    bablo = rub * 110
    return bablo

def rub_to_gbr(rub):
    """rubli to nemeckoe bablo"""
    bablo = rub * 10
    return bablo

print('Hello, i am converter')
print('I can convert from roubles(RUB) to')
to_currency = input('USD or EUR or GBR: ').upper()

if to_currency == 'USD':
    rub = int(input('How much roubles do you want to convert: '))
    print(f'RUB to USD is: {rub_to_usd(rub)}')
elif to_currency == 'EUR':
    rub = int(input('How much roubles do you want to convert: '))
    print(f'RUB to EUR is: {rub_to_eur(rub)}')
elif to_currency == "GBR":
    rub = int(input('How much roubles do you want to convert: '))
    print(f'RUB to GBR is: {rub_to_gbr(rub)}')
else:
    print('You are stupid!')