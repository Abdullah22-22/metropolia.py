class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        uusi_nopeus= self.nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0 :
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus


car = Auto("ABC-123", 142)

car.kiihdytä(30)
print(f"nopeus nyt  ==>  {car.nopeus} KM 30")
car.kiihdytä(50)
print(f"nopeus nyt  ==>  {car.nopeus} KM  50")
car.kiihdytä(70)
print(f"nopeus nyt  ==>  {car.nopeus} KM   70")
car.kiihdytä(-200)
print(f"nopeus nyt  ==>  {car.nopeus} KM   -200")