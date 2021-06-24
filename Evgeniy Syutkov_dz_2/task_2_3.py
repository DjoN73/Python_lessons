my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i, val in enumerate(my_list):
    if val.replace('+', '').isdigit():
        if val.isdigit():
            my_list[i] = f'"{int(val):02d}"'
        else:
            my_list[i] = f'"{val[0]}{int(val):02d}"'

print(my_list)
print(' '.join(my_list))
