from abc import ABC, abstractmethod

# Product interface
class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

# Concrete Products
class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"

# Creator (Factory)
class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass

# Concrete Factories
class CarFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Car()

class TruckFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Truck()

class BikeFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Bike()

# Demo
if __name__ == "__main__":
    carFactory = CarFactory()
    truckFactory = TruckFactory()
    bikeFactory = BikeFactory()

    myCar = carFactory.createVehicle()
    myTruck = truckFactory.createVehicle()
    myBike = bikeFactory.createVehicle()

    print(myCar.getType())    # "Car"
    print(myTruck.getType())  # "Truck"
    print(myBike.getType())   # "Bike"
