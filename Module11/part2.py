class Car:
    def __init__(self,number,max_speed):
        self.number = number
        self.max_speed = max_speed
        self.speed = 0   
        self.KM = 0  
        
    def set_speed(self,speed):
        self.speed = min(speed,self.max_speed)

    def drive(self,h):
        self.KM += self.speed * h

class Electric_car(Car):
    def __init__(self, number, max_speed, battery_capacity):
        super().__init__(number, max_speed)
        self.battery_capacity = battery_capacity

class Combustion (Car):
     def __init__(self, number, max_speed, tank_size):
        super().__init__(number, max_speed)
        self.tank_size=tank_size




electric_car = Electric_car("ABC-15", 180, 52.5)
ombustion = Combustion("ACD-123", 165, 32.3)



electric_car.set_speed(150)
ombustion.set_speed(120)


electric_car.drive(3)
ombustion.drive(3)


print(f"Electric car km: {electric_car.KM} km")
print(f"Combustion car km: {ombustion.KM} km")