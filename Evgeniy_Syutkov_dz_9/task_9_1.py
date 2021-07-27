import time


class TrafficLight:
    __color = 'Red'

    def running(self):
        while True:
            print('Красный')
            time.sleep(7)
            print('Желтый')
            time.sleep(2)
            print('Зеленый')
            time.sleep(5)
            print('Желтый')
            time.sleep(2)


trafficlight = TrafficLight()
trafficlight.running()
