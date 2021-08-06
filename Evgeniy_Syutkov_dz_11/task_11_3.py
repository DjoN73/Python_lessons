class OwnError(Exception):
    pass


my_list = []
while True:
    try:
        value = input('Введите число: ')
        if value == 'stop':
            break
        if not value.isdigit():
            raise OwnError('Не является числом')
        my_list.append(value)
    except OwnError as err:
        print(err)
print(my_list)
