class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("Engine started")

my_car = Car("Toyota", "Corolla")
my_car.start_engine()

# Przypisanie nowego atrybutu
my_car.speed = 60
print('Speed:', my_car.speed)

my_car.drive()
