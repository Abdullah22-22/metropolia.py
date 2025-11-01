nimi=[]
nimi_set = set()

while True:
    anna_nimi=str(input("anna nimi:=>  "))
    if anna_nimi=="":
        break
    if anna_nimi in nimi:
        print("nimi on listalla")
    else:
        nimi.append(anna_nimi)
        nimi_set.add(anna_nimi)

print("Kaikki nimet:=> ", nimi)