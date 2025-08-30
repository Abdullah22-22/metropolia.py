
oikea_tunnus = "abd"
oikea_salasana = "fcb"
yritykset = 0

while yritykset < 5:
    käytä_tuunes = input("Anna Sun Tunnis: =>  ")
    Salasana_tuunes = input("Anna Sun Salasana: =>  ")
    if   käytä_tuunes == oikea_tunnus and Salasana_tuunes == oikea_salasana:
          print("Tervetuloa")
          break
    else:
        yritykset += 1
        print("Väärä tunnus tai salasana, yritä uudelleen.")


if yritykset == 5:
    print("Liian monta yritystä")