import random
def noppa():
    naanin= int(input("naanin:1-6 => "))
    while True:
            rand = random.randint(1,6)
            print(rand)
            if rand == naanin:
                print("hyvää")
                break

noppa()