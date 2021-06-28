def num_translate(word):
    in_word = word.lower()
    if word.istitle() and in_word in numbers:
        return numbers.get(in_word).title()
    return numbers.get(word)


numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
           'four': 'четыре', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь',
           'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

print(num_translate(input('Введите число на английском: ')))
