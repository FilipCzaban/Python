suma = 0.01  
print(f'Den 1: {suma} Kč')
for den in range(2, 31):  
    suma *= 2
    print(f'Den {den}: {suma} Kč')
