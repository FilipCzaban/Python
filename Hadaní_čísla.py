import random 
pokusy = 0
print("vyber obtížnost: 1 = Lehká (50), 2 = Střední (100), 3 = Těžká (150)")
Obtížnost = input("Zadej číslo obtížnosti(1/2/3):")

if Obtížnost == "1":
    číslo = random.randint(0,50)
elif Obtížnost == "2":
    číslo = random.randint(50,100)
elif Obtížnost == "3":
    číslo = random.randint(100,150)
else:
    print("Nepltaná obtížnost")
    Obtížnost = input("Zadej číslo obtížnosti(1/2/3):")



while pokusy < 7:
    zadane_číslo = input("uhodni číslo:")
    if not zadane_číslo.isdigit():
        print("zadaná hodnota není číslo, napiš číslo!")
        continue
    zadane_číslo = int(zadane_číslo)

    if zadane_číslo == číslo:
        print("Spravně")
        break
    elif zadane_číslo > číslo:
        print(f"Špatné číslo, číslo je menší, Pokus {pokusy}/7")
        pokusy += 1
    elif zadane_číslo < číslo:
        print(f"Špatné číslo, číslo je větší, Pokus {pokusy}/7")  
        pokusy += 1  
    if pokusy == 7:
        print("Moc pokusů") 
    

    



