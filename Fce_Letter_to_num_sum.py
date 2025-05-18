def fce(zvts):
    return zvts.upper()

def csl(zmn):
    vsldk = [ord(pismeno) for pismeno in zmn]
    return vsldk
knc = fce("abcdefghijklmnopqrstuvwxya")
kncn = csl(knc)
knnn = [cislo + 1 for cislo in kncn]
print(knnn)

def psm(zm):
    vsldk ="".join(chr(pismeno) for pismeno in zm)
    return vsldk
kncvsldk = (psm(knnn))
print(kncvsldk)

