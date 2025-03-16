
# Tahák na programování v Pythonu
- [Proměnné](#promenne)
- [Aritmetické operace](#aritmeticke-operace)
- [Podmínky a logické operace](#podminky-a-logicke-operace)
- [Cykly](#cykly)
- [Funkce](#funkce)
- [Texty](#texty)
- [Výstupy](#vystupy)
- [Vstupy](#vstupy)
## Proměnné
***Proměnné v Pythonu slouží k uchovávání hodnot, které lze během běhu programu měnit a používat v různých výpočtech nebo podmínkách.***

| Datový typ | Popis | Příklad |
|------------|--------|-----------|
| int | Celé číslo | `x = 10` |
| float | Desetinné číslo | `y = 3.14` |
| str | Řetězec | `name = "Alice"` |
| bool | Pravda/Nepravda | `is_lower = True` |
| list | Seznam hodnot | `numbers = [1, 2, 3]` |
| tuple | Neměnitelný seznam | `coordinates = (4, 5)` |
| dict | Slovník | `person = {"name": "Alice", "age": 25}` |
| set | Množina | `numbers = {1, 2, 3}` |


## Aritmetické operace
***Aritmetické operace jsou základní matematické operace, které zahrnují sčítání, odčítání, násobení, dělení, celočíselné dělení, zbytek po dělení a mocniny. V Pythonu se používají následující operátory:***
```python
a = 10 + 5  # Sčítání
b = 10 - 5   # Odčítání
c = 10 * 5   # Násobení
d = 10 / 5   # Dělení (výsledek je float)
e = 10 // 3  # Celé dělení
f = 10 % 3   # Zbytek po dělení
g = 2 ** 3   # Mocnina

import math
math.sqrt(9) # Odmocnina
```

## Podmínky a logické operace
### Podmínky
|Podmínka| Výzanm| Příklad | Výsledek |
|------------|--------|-----------| ---------------
| `==` | Je rovno| `5 == 5`|`True`|
| `!=` | Není rovno| `5 != 3`|`True`|
| `>`  | Vetší než| `10 > 3` |`True`|
| `<`  | Menší než| `2 < 5` |`True`|
| `>=` | Větší nebo rovno| `4 >= 4`|`True`|
| `<=` | Menší nebo rovno| `3 <= 7` |`True`|

```python
# Podmínky
if x > 0:
    print("x je kladné")
elif x == 0:
    print("x je nula")
else:
    print("x je záporné")
```

### **Logické operace**
|Podmínka| Výzanm| Příklad | Výsledek |
|------------|--------|-----------| ---------------| 
| `and` | obě musí platit| `True and False`|`False`|
| `or`| minimalně jedna musí platit| `True or False`|`True`|
| `not` | negace podmínky|`not True`|`False`|


```python
# Logické operace
if a > 0 and b > 0:
    print("Obě čísla jsou kladná")

if a > 0 or b < 0:
    print("Alespoň jedno číslo je kladné")
```

## Cykly
***Cykly v Pythonu umožňují opakování kódu, dokud není splněna určitá podmínka. Existují dva hlavní typy cyklů:***

**For cyklus: Používá se k opakovaní přes sekvenci (např. seznam, řetězec, rozsah) a vykonání kódu pro každý prvek v sekvenci :**

```python
# Cyklus for
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
# Tento cyklus vytiskne čísla od 0 do 4.
```

**While cyklus: Opakuje kód, dokud je splněna daná podmínka.**
```python
x = 0
while x < 5:
    print(x)
    x += 1
# Tento cyklus rovněž vytiskne čísla od 0 do 4.
``` 

## Funkce
***Funkce v Pythonu jsou bloky kódu, které provádějí určitou činnost a lze je opakovaně volat. Definují se pomocí klíčového slova  `def`, mohou přijímat argumenty a vracet hodnotu pomocí `return`.***
```python
# Příklad 1
def soucet(a, b):
    return a + b
print(soucet(5, 5))  # 10

# Příklad 1
def absoltní_hodnota(n):
    if n < 0:
        n = n * -1
    return n
print(absolutni_hodnota(-5))  # Výstup: 5
print(absolutni_hodnota(3))   # Výstup: 3
```

## Texty
***V Pythonu jsou texty (řetězce) reprezentovány jako datový typ `str`. Můžeme je vytvářet pomocí uvozovek (`"text"` nebo `'text'`) a poté s nimi pracovat – spojovat je, měnit jejich obsah nebo je rozdělovat.***
```python
text = "Zítra, venku!"
print(text.upper())  # "ZÍTRA, VENKU!"
print(text.lower())  # "zítra, venku"
print(text.replace("Zítra", "Potom"))  # "Potom, venku!"
print(len(text))  #Výstup: 13 (Délka řetězce)
```

## Výstupy
***Výstupy v Pythonu slouží k zobrazování informací na obrazovku nebo ukládání dat do souborů. Nejčastěji se k tomu používá funkce `print()`, která vypisuje hodnoty do konzole.***
```python
# Základ
print("Výsledek je:", 42)

#Příklad 1
jmeno = "Filip"
vek = 15
print("Jméno:", jmeno, "| Věk:", vek) # Výstup: Jméno: Petr | Věk: 15


# Příklad 2

```

## Vstupy
```python
jmeno = input("Jak se jmenuješ? ")
print("Ahoj, " + jmeno)