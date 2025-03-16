import random
while True: 
    u = input("Zadej Kámen, nůžky, nebo papír (nebo 'stop' pro ukončení):").lower()
    if u == "stop":
        print("Program ukončen")
        break
    pc = random.choice(["kámen","nůžky","papír"]).lower()
    print(f"PC = {pc}")
    if u == pc:
        print("Remíza")
    elif (u == "kámen" and pc == "nůžky" ) or \
         (u == "papír" and pc == "kámen" ) or \
         (u == "nůžky" and pc == "papír" ): 
        print("Výhra")
    else:
        print("Prohra")
        
 