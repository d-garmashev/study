class Car:
    fuel = None # litres
    current_speed = 0 # km/h
    position = 0 # km

    def __init__(self, position):
        self.position = position
        super().__init__()

    def start(self):
        print('Wroom')

    def accelerate(self, value):
        self.current_speed += value

    def steer(self, hours):
        self.position = self.current_speed * hours

    def break_car(self):
        self.current_speed = 0

    def stop(self):
        print('Stopped')

# car0 = Car
# print(type(car0))
#
# car1 = Car()
# print(type(car1))
# print(car1)
#
#
# car2 = Car()
# print(car2)
#
# print(car1 is car2)
#
# car0 = Car()
# print(car0.current_speed)
# car0.start()
# car0.accelerate(10)
# print(car0.current_speed)
#
# print(car1.__dict__)
# car1.current_speed = 20
# print(car1.__dict__)

car0 = Car(2)
car1 = Car(10)
print(car0.__dict__)
print(car1.__dict__)

class SportCar(Car):
    mass = 0 # kg
    pass

class AutoTransmissionCar(Car):
    transmission = 'auto'

    def __init__(self, position, gear):
        self.gear = gear
        super().__init__(position)

class ManualTransmissionCar(Car):
    transmission = 'manual'


sportcar0 = SportCar(12)
print(sportcar0.__dict__)


car4 = AutoTransmissionCar(4, 10)
print(car4.__dict__)