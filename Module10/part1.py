class  Elevator:
    def __init__(self, firstFloor, lastFloor):
        self.firstFloor = firstFloor
        self.lastFloor = lastFloor
        self.floor =firstFloor

    def getup(self):

        if self.floor < self.lastFloor:
            self.floor += 1
            print(f"The elevator is now on floor {self.floor}")
        else:
            print("The elevator is already on the top floor!")

    def getdown(self):

        if self.floor > self.firstFloor:
            self.floor -= 1
            print(f"The elevator is now on floor {self.floor}")

        else:
            print("The elevator is already on the first floor!")



elevator = Elevator(1, 10)

elevator.getup()
elevator.getup()
elevator.getdown()
elevator.getdown()
elevator.getdown()