import random
while True:
    a = random.choice([2, 4, 6, 8])   
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    d = random.randint(1, 4)
    if a + b + c + d == 21:
        break

kod = [a, b, c, d]
Pokusy = 0
while True:
    první = int(input("první číslo:"))
    if první == a:
        print(f"správně, {a}- ")
        Pokusy += 1 
        break
    else:
        print("znovu")
        Pokusy += 1 
    
while True:
    druhý = int(input("druhý číslo:"))
    if druhý == b:
        print(f"správně, {a}-{b}-")
        Pokusy += 1 
        break
    else:
        print("znovu")
        Pokusy += 1 
    
while True:    
    třetí = int(input("třetí číslo:"))
    if třetí == c:
        print(f"správně, {a}-{b}-{c}-")
        Pokusy += 1 
        break
    else:
        print("znovu")
        Pokusy += 1 

while True:       
    čvrtý = int(input("čtvrtý číslo:"))
    if čvrtý == d:
        Pokusy += 1 
        print(f"správně, kod je {a}-{b}-{c}-{d} na {Pokusy} pokusů")
        break
    else:
        print("znovu")
        Pokusy += 1 