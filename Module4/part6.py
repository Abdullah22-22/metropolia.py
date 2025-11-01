import  random

num=int(input("Anna numero: =>  "))

n=0
i=0

while i < num:
    x= random.uniform(-1,1)
    y= random.uniform(-1,1)

    if x**2 + y**2 < 1:
        n += 1
    i += 1

pi= 4 * n /num

print(pi)