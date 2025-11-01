print("vuratan hemoglobiini naisle js mihella")




sukupuoli = input("Syötä sukupuoli (mies m/nainen n): ").lower()
hemoglobiini = float(input("Syötä hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen" or sukupuoli =="n":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvo on alhainen")
    elif hemoglobiini > 175:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")


elif sukupuoli == "mies" or sukupuoli == "m":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hemoglobiini > 195:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")

