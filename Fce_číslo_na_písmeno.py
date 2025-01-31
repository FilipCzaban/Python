def csl(zmn):
    vsldk = [ord(pismeno) for pismeno in zmn]
    return vsldk
knc = (csl("ABC"))
print(f"Převod na nubmer = {knc}")

def psm(zmn):
    vsldk ="".join(chr(pismeno) for pismeno in zmn)
    return vsldk
kncvsldk = (psm(knc))
print(f"Zpět převod na písmena = {kncvsldk}")
