def thesaurus(*args):
    names = {}
    for idx in sorted(args):
        letter = idx[0]
        if letter in names:
            names[letter] += [idx]
        else:
            names[letter] = [idx]
    return names


print(thesaurus("Иван", "Павел", "Мария", "Петр", "Илья", "Максим"))
