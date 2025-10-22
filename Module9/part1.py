class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

car = Auto("ABC-123", 142)

print(f"rekisteritunnus ==>  {car.rekisteritunnus} \n"
      f" huippunopeus  ==> {car.huippunopeus} KM  \n"
      f" nopeus ==>  {car.nopeus}:KM \n"
      f"kuljettu_matka ==>  {car.kuljettu_matka} KM " )