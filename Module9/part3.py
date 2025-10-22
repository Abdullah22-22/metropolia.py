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

    def kulje(self,T):
        self.kuljettu_matka += self.nopeus *  T



car = Auto("ABC-123", 142)



car.kiihdytä(60)
print(f"nopeus nyt  ==>  {car.nopeus} KM")

car.kulje(1.5)
print(f"kuljettu_matka nyt  ==>  {car.kuljettu_matka} KM")
