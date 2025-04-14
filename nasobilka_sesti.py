soucet = 0
for cislo in range(1,61):
    if cislo % 6 == 0:
        soucet += cislo
        print(cislo)
        print(f"Soucet je {soucet}")