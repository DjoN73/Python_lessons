MINUTE = 60
HOUR = 60 * 60
DAY = 60 * 60 * 24

duration = int(input('Введите продолжительность времени: '))
if duration < MINUTE:
    print(duration, 'сек')
elif duration >= MINUTE and duration < HOUR:
    print(duration // MINUTE, 'мин', duration % MINUTE, 'сек')
elif duration >= HOUR and duration < DAY:
    print(duration // HOUR, 'час', duration % HOUR // MINUTE, 'мин', duration % HOUR % MINUTE, 'сек')
else:
    print(duration // DAY, 'дн', duration % DAY // HOUR, 'час', duration % DAY % HOUR // MINUTE, 'мин',
          duration % DAY % HOUR % MINUTE, 'сек')
