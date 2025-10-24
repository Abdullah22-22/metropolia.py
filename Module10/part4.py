import random

class Car:

    def __init__(self, name, top_speed):
        self.name = name
        self.top_speed = top_speed 
        self.speed = 0
        self.distance_traveled = 0


    def accelerate(self, change):
        new_speed = self.speed + change

        if new_speed > self.top_speed:
            self.speed = self.top_speed

        elif new_speed < 0:
            self.speed = 0
        
        else:
            self.speed = new_speed


    def drive(self, hours):
        self.distance_traveled += self.speed * hours



class Race:
     
    def __init__(self, name, length, cars):
        self.name = name
        self.length = length
        self.cars = cars
        self.hour = 0

    def hour_passes(self):
        self.hour += 1

        for car in self.cars:
            change = random.randint(-10, 15) 
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\nHour {self.hour}")
        print(f"{'Car':<10} {'TopSpeed':<9} {'Speed':<7} {'Distance':<10}")
        for car in self.cars:
            print(f"{car.name:<10} {car.top_speed:<9} {car.speed:<7} {car.distance_traveled:<10.2f}")    

    def race_finished(self):
        for car in self.cars:
            if car.distance_traveled >= self.length:
                return True
        return False

car_names = ["Bolt", "Flash", "Rocket", "Lightning", "Blaze", "Storm", "Dash", "Comet", "Turbo", "Zoom"]
cars = []


for name in car_names:
    top_speed = random.randint(100, 200)
    cars.append(Car(name, top_speed))


race = Race("Formal One", 8000, cars)

while not race.race_finished():
    race.hour_passes()
    if race.hour % 10 == 0:  
        race.print_status()



race.print_status()