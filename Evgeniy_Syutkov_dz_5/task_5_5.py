src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_dist = {i: 0 for i in src}

for i in src:
    if i in my_dist:
        my_dist[i] += 1

result = [i for i in my_dist if my_dist[i] == 1]
print(result)
