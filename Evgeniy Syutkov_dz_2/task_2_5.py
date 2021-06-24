prices = [8.8, 57.8, 46.51, 97, 35, 10.3, 24.56, 17, 18.3, 23.99, 7]
for idx in prices:
    price = str(idx).split('.')
    if str(idx).count('.'):
        print(f'{int(price[0])} руб {int(price[1]):02d} коп', end=', ')
    else:
        price.append('00')
        print(f'{int(price[0])} руб {int(price[1]):02d} коп', end=', ')

print()
print(prices, id(prices))
prices.sort()
print(prices, id(prices))
new_list = sorted(prices, reverse=True)
print(new_list, id(new_list))
print(sorted(prices)[-5:])
