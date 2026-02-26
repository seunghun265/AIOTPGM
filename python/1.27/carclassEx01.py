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
    def __str__(self):
        return f"차량 = {self.make},{self.model},{self.color},{self.price}"
    
class ElectricCar(Car):           #부모꺼 다받겠다
    def __init__(self,make,model,color,price,batterySize):
        super().__init__(make,model,color,price)
        self.batterySize = batterySize
    def setBatterySize(self,batterySize):
        self.batterySize = batterySize
    def getBatterySize(self):
        return self.batterySize
    
myCar = ElectricCar("Hyundai","Model H", "White", "5000",0)
myCar.setBatterySize(240)
print(myCar)
print(myCar, end=" ")
print(myCar.getBatterySize())