import collections

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    logs = ((line.split()[0], line.split()[5].strip('"'), line.split()[6]) for line in f)
    my_dict = collections.Counter()
    for idx in logs:
        my_dict[idx] += 1
    ip, count = my_dict.most_common(1)[0][0], my_dict.most_common(1)[0][1]
print(f'Спамер: {ip[0]} - {count} раз')
