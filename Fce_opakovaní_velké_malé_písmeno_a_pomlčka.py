def fce(text):
    vsldk = ""
    index = 0
    for znak in text:
        if vsldk != "":
            vsldk += "-"
        vsldk += znak.upper()
        vsldk += znak.lower() * index
        index += 1
    return vsldk
d = (fce("ABCD"))

def fcee(text):
    vsldk = ""
    index = 1
    for znak in text:
        if index %2 == 1: 
            vsldk += znak.upper()
        else:
            vsldk += znak.lower()
        index += 1    
    return vsldk
print(fcee(d))


    
