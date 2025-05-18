částka = float(input("Napiš částku:"))
délka = float(input("Jak dlouho se bude zhodnocovat:"))
roční_zhodnocení = 12.5
vs = částka / 100 
vsld = vs * roční_zhodnocení * délka
print(f"Zhodnocení po {délka} letech bude {vsld}")

