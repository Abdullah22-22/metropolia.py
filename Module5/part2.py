luvut = []

while True:
    num1 = input("anna a numero: =>  ")
    if num1 == "":
        break
    luvut.append(int(num1))

luvut.sort(reverse=True)
x = luvut[0:5]

print(x)
