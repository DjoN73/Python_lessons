from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Clothes.result

    def __str__(self):
        return f'{Clothes.result}'


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consumption(self):
        return round(2 * self.param + 0.3) / 100


coat = Coat(38)
print(coat.consumption)
costume = Costume(175)
print(costume.consumption)
print(coat + costume)
