class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        print(f'Новая машина: {name}, {color} цвет')

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        return (f'Скорость автомобиля: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превышаете скорость')
        else:
            print(f'Скорость автомобиля: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f'Скорость автомобиля: {self.speed}'


class PoliceCar(Car):
    def __init__(self, name, color, speed, in_police=True):
        super().__init__(name, color, speed, in_police)


work_car = WorkCar('Газель', 'желтый', 65)
work_car.go()
print(work_car.show_speed())
work_car.turn('налево')
work_car.stop()

print()
police_car = PoliceCar('Police', 'белый', 125)
police_car.go()
print(police_car.show_speed())
police_car.turn('направо')
police_car.stop()
