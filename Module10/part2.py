class Building:

    def __init__(self, firstFloor, lastFloor, numElevators):

        self.firstFloor = firstFloor
        self.lastFloor = lastFloor
        self.numElevators =numElevators

        self.elevators =[firstFloor for _ in range(numElevators)]

    def getup(self,elevator_number):

        if self.elevators[elevator_number] < self.lastFloor:

            self.elevators[elevator_number] += 1
            print(f"Elevator {elevator_number} is now on floor {self.elevators[elevator_number]}")

        else:
            print(f"Elevator {elevator_number} is already on the top floor!")

    def getdown(self,elevator_number):

        if  self.elevators[elevator_number] > self.firstFloor:
            self.elevators[elevator_number] -=1

            print(f"Elevator {elevator_number} is now on floor {self.elevators[elevator_number]}")

        else:
            print(f"Elevator {elevator_number} is already on the first floor!")



    def move_elevator(self,elevator_number, target_floor):
          
        current = self.elevators[elevator_number]
        print(f"\nMoving elevator {elevator_number} from floor {current} to floor {target_floor}:")

        if  target_floor > current :

            for _ in range(target_floor - current ):
                self.getup(elevator_number)

        elif target_floor < current :
            for _ in range(current - target_floor):
                 self.getdown(elevator_number)
        
        else:
            print(f"Elevator {elevator_number} is already on floor {target_floor}")



building = Building(1, 10, 3) 

building.move_elevator(0, 5)
building.move_elevator(1, 8)  
building.move_elevator(2, 2)  
