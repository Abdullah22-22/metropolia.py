data = {

}

while True:
    print("""
    1) anna Lentokenttä 
    2) Valitse Lentokenttä
    3) jos haluat lopeta laitaa 
    """)
    valitas = int(input("valitas 1 tai 2 tai 3: "))

    if valitas == 1:
        Key = input("Key:=> ")
        Value = input("Value:=> ")
        data[Key] = Value

    elif valitas == 2:
        code = input("Anna Key :=>  ")
        if code  in data:
            print(data[code])
        else:
            print("Lentokenttä ei löytynyt.")
    elif valitas == 3:
        break
