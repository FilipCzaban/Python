r = float(input("Zadej poloměr kružnice v cm:"))
v = input("Chceš počítat ('obvod') nebo ('obsah')?:")
if v == "obvod":  
    o = (2*3.14) * r
    o = round(o, 2)
    print (f"Obvod s poloměrem {r} je {o}cm")
elif v == "obsah":
    s = 3.14 * (r**2)
    s = round(s, 2)
    print (f"Obvod s poloměrem {r} je {s}cm²")
