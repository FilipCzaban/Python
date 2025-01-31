def csl(zmn):
    vsldk = [ord(pismeno) for pismeno in zmn]
    return vsldk
knc = csl("ABC")
knnn = [cislo + 3 for cislo in knc]
print(knnn)

def psm(zm):
    vsldk ="".join(chr(pismeno) for pismeno in zm)
    return vsldk
kncvsldk = (psm(knnn))
print(kncvsldk)


