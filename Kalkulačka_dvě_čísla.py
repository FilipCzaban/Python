první = input("první číslo:")
druhé = input("druhé číslo:")
první = int(první)
druhé = int(druhé)
operace  = input("jakou operaci chceš provést (+, -, *, /): ")
if operace == "+":
    vsldk = první + druhé
elif operace == "-":
    vsldk = první - druhé
elif operace == "*":
    vsldk = první * druhé
elif operace == "/":
    if druhé != 0:
        vsldk = první / druhé
    else:
        print("Nulou nelze dělit")

else:
    ("Neplatný")
print(f"{první}{operace}{druhé} = {vsldk}")


