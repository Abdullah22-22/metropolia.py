print("""Tervetuloa, kalastaja! 
Olet nyt kalassa Suomessa.
Muista seuraavat ohjeet:
1) Kuha on alamittainen, jos sen pituus on alle 37 cm.
2) Jos kuha on alamittainen, se täytyy laskea takaisin järveen.
3) Noudata aina Suomen kalastuslainsäädäntöä ja kunnioita luontoa.""")

kala_pituus = float(input("Kalan pituus (cm): " ))

if kala_pituus >= 37:
    print("Voit ottaa kalan mukaasi.")
else:
    x = 37 - kala_pituus
    print("Kala on alamittainen, laske se takaisin järveen.")
    print("Kala on", x, "cm liian lyhyt.")