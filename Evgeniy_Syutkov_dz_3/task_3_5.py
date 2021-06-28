from random import choice, randrange


def get_jokes(quantity, repeat=True):
    """
        Функция возвразает случайные шутки, из собранных слов из трех списков
    :param quantity: список случайных шуток
    :param repeat: уникальность
    :return: список случайных шуток
    """
    jokes = []
    while quantity and len(nouns):
        if repeat:
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        else:
            jokes.append(f'{nouns.pop()} {adverbs.pop()} {adjectives.pop()}')
        quantity -= 1

    return jokes


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

num = int(input('Введите количество шуток: '))

print(get_jokes(num, False))
