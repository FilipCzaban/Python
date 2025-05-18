def fce(znamky):
    soucet = 0
    váha_celkem = 0
    for znamka,váha in znamky:
        if type(znamka) == int:  
            soucet += znamka * váha 
            váha_celkem += váha
            vsldk = soucet / váha_celkem 
    return round(vsldk, 2)
známky = [[1,5],[5,2],[3,4],["N",5]]
print(fce(známky))

