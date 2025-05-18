def fce(text):
    vsldk = ""
    index = 1
    for znak in text:
        if index %2 == 1: 
            vsldk += znak.upper()
        else:
            vsldk += znak.lower()
        index += 1    
    return vsldk
print(fce("abCDefGHI")) 

    
