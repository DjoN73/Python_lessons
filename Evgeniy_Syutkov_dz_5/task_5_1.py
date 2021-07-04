def nums_generator(n):
    for num in range(1, n + 1, 2):
        yield num


n = nums_generator(5)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
