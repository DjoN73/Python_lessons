nums_generator = (num for num in range(1, int(input('Введите число: ')) + 1, 2))

print(*nums_generator, sep=' ')
