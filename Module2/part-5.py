leiviska= float(input("anna leiviska : => "))
naula = float(input("anna naula : => "))
luoti = float(input("anna luoti : => "))

grammat = (leiviska * 20 * 32 * 13.3) + (naula * 32 * 13.3) + (luoti * 13.3)

kg= int(grammat // 1000)
gr= grammat % 1000

print(f"Massa nykymittojen mukaan:\n{kg} kilogrammaa ja {gr:.2f} grammaa.")
