luvut= []
def anna():
    while True:
        laita= int(input("enter laita: "))
        if laita >=10:
            break
        luvut.append(laita)

    print("luvut: => ", luvut)
    luvut1 = []
    for num in luvut:
        if num  % 2 == 0:
            luvut1.append(num)

    print("luvut 1:  => ", luvut1)


anna()