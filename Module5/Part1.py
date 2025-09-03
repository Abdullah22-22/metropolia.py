import random

num = int(input("anna numero : => "))
total = 0
for i in range(num):
    rand1=random.randint(1,6)
    total += rand1

print( total)