tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

result = ((tutors[idx], klasses[idx]) if len(klasses) > idx else (tutors[idx], None) for idx in range(len(tutors)))
print(type(result), *result)
print(*result)