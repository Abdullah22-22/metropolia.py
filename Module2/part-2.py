# 1 Lue Fahrenheit
# 2 Muunna Celsiusiksi
# 3 Tulosta tulos
# 4 Matematiikan vakioita
#5 π #6 e


import math

fahrenheit = float(input("Fahrenheit:=>  "))
c = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} Fahrenheit on {c:.2f} Celsius")


print(f"{'Pii':12s}:{math.pi:10.5f}")
print(f"{'Luku':12s}:{math.e:10.5f}")
