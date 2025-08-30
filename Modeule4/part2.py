while True:
    num1 = 2.54
    num2 = float(input("Anna numero (tuumaa): => "))

    if num2 < 0:
        print("Lopetetaan ohjelma.")
        break
    else:
        cm = num2 * num1
        print(f"{num2} tuumaa = {cm:.2f} cm")
