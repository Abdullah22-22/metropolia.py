print("""
A= ikkunallinen hytti autokannen yläpuolella.
B= ikkunaton hytti autokannen yläpuolella.
C= ikkunaton hytti autokannen alapuolella.
LUX= parvekkeellinen hytti yläkannella.
Valitse  (A, B, C, LUX)
""")

chosen_team = input("Valitse  : =>  ").upper()

if chosen_team == "A":
    print("ikkunallinen hytti autokannen yläpuolella")
elif chosen_team == "B":
    print("ikkunaton hytti autokannen yläpuolella")
elif chosen_team == "C":
    print("ikkunaton hytti autokannen alapuolella")
elif chosen_team == "LUX":
    print("parvekkeellinen hytti yläkannella")
else:
    print("Virheellinen hyttiluokka")
