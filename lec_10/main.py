from vehicle import MyVehicle

class MyCar(MyVehicle):
    def __init__(self):
        super().__init__()
        print('Car ')

class MyPlane(MyVehicle):
    def __init__(self):
        super().__init__()
        print('Plane ')

class MyBoat(MyVehicle):
    def __init__(self):
        super().__init__()
        print('Boat ')

class MyRaceCar(MyCar):
    def __init__(self):
        super().__init__()
        print('RaceCar ')


vehicle = MyVehicle()
car = MyCar()
plane = MyPlane()
boat = MyBoat()
race_car = MyRaceCar()
