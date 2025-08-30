luvut = []

while True:
    num1= input("Anna numero: (tyhjä lopettaa) : =>  ")
    if num1 == "":
        break
    num1 = float(num1)
    luvut.append(num1)
    if luvut:
        x1= min(luvut)
        x2= max(luvut)

        print(f"tämä on min luvut =>  {x1}\n tämä on max luvut =>  {x2}")
    else:
        print("ei ole luku")
