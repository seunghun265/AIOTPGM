class Car:
    def __init__(self,make,model,color,price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
    def setMake(self,make):
        self.make = make
    def getMake(self):
        return self.make
    def displayCarInfo(self):
        return f"차량 = {self.make}, {self.model}, {self.color}, {self.price}"
        

class ElectricCar(Car):
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make,model,color,price)
        self.batterySize = batterySize
    def setBatterSize(self, batterySize):
        self.batterySize = batterySize
    def getBatterSize(self):
        return self.batterySize
    def displayElectricCarInfo(self):
         return super().displayCarInfo() + f", 배터리 = {self.batterySize}kWh"
car1 = Car("Hyundai","model H", "Gray", 6000)
eCar1 = ElectricCar("Hyundai", "model H", "white", 5000, 240)
print(car1.displayCarInfo())
print(eCar1.displayElectricCarInfo())
