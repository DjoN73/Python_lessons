my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
correct_list = []
for i in my_list:
    if i.replace("+", "").isdigit():
        if i.isdigit():
            correct_list.append(f'"{int(i):02d}"')
        else:
            correct_list.append(f'"{i[0]}{int(i[1]):02d}"')
    else:
        correct_list.append(i)
print(' '.join(correct_list))
