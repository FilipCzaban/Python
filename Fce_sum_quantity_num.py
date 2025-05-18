def fce(numbers, number):
    čsl = 0
    for n in numbers:
        if n == number:
            čsl += 1 
    return čsl
print(fce([1,2,2,2,3,99,1,5,65,41,15,1,5,1,545,1,41,65,4,25,5,5,5,511,1], 1))
