from itertools import zip_longest
from json import dump

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:

        if len(users.readlines()) >= len(hobby.readlines()):
            with open('users_hobby.json', 'w', encoding='utf-8') as f:
                users.seek(0)
                hobby.seek(0)
                all_list = zip_longest(users, hobby, fillvalue=None)
                users_hobby = {str(el[0]).strip(): (str(el[1]).strip()) for el in all_list}

                dump(users_hobby, f, ensure_ascii=False, indent=4)
                print(users_hobby)
        else:
            exit(1)
