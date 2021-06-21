coub_list = []
for number in range(1, 1001, 2):
    coub_list.append(number ** 3)
result = 0
for idx in range(len(coub_list)):
    number = coub_list[idx]
    sum_digits = 0
    while number:
        sum_digits += number % 10
        number //= 10
    if sum_digits % 7 == 0:
        result += coub_list[idx]
print(coub_list)
print(result)

result = 0
for idx in range(len(coub_list)):
    coub_list[idx] += 17
    number = coub_list[idx]
    sum_digits = 0
    while number:
        sum_digits = + number % 10
        number //= 10
    if sum_digits % 7 == 0:
        result += coub_list[idx]
print(coub_list)
print(result)
