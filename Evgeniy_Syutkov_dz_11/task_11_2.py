class OwnError(Exception):
    pass


num = int(input('Введите число: '))
try:
    if num == 0:
        raise OwnError('На 0 делить нельзя')
    else:
        res = 100 / num
except OwnError as err:
    print(err)
else:
    print(f'res = {res}')
