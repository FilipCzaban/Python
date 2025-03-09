import math  
a = float(input("Zadej původní délku koleje v cm:"))
b = float(input("o kolik cm jí chceš prodloužit?:"))
c = a+b
v = math.sqrt(c**2 - a**2)
v = round(v, 2)
print(f"Koleje se zvednou o {v}cm")
