import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        uusi_nopeus = self.nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, t):
        self.kuljettu_matka += self.nopeus * t


autot = []

for i in range(1, 11):
    rekisteri = f"ABC-{i}"
    huippu = random.randint(100, 200)
    auto = Auto(rekisteri, huippu)
    autot.append(auto)

kilpailu_kaynnissa = True
t = 0

while kilpailu_kaynnissa:
    t += 1

    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break

print(f"{'Rekisteri':<10} {'Huippu':<7} {'Nopeus':<7} {'Matka':<10}")
print("-" * 40)

for auto in autot:
    print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:<7} {auto.nopeus:<7} {auto.kuljettu_matka:<10.2f}")
