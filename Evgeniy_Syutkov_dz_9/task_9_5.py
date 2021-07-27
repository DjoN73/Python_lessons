class Stationery:
    def __init__(self, title='Что-то, что может писать'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с маркером {self.title}')


stat = Stationery()
stat.draw()
pen = Pen('Parker')
pen.draw()
pencil = Pencil('Lyra')
pencil.draw()
handle = Handle('Touch Twin')
handle.draw()
