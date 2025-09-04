import math
r=math.pi
half= (10)^2
def pizza():
    pizza_hinta= int(input("pizza_hinta: =>  "))
    pizaa_cm= int(input("pizza_cm: =>  "))

    sapse= r* half

    nelioM= sapse * pizza_hinta

    m= nelioM/1000

    print("pizza: => ",m, "m")

pizza()