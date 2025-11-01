kausi = ["kevät", "kesä", "syksy", "talvi"]

Valitse_kausi = int(input("Valitse kausi (1-12): => "))

if Valitse_kausi in [3, 4, 5]:
    print(kausi[0])
elif Valitse_kausi in [6, 7, 8]:
    print(kausi[1])
elif Valitse_kausi in [9, 10, 11]:
    print(kausi[2])
elif Valitse_kausi in [12, 1, 2]:
    print(kausi[3])
else:
    print("väärä numero")
