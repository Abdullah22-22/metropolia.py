num = int(input("anna numero: => "))

if num < 2:
    print("ei alkuluku")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("on alkuluku")
    else:
        print("ei alkuluku")
