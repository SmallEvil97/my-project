import math
number = 1000
lst = [2] * number
for i in range (2, int(math.sqrt(number))):
    for l in range (i * 2, number, i):
        lst[l] = False
        prime_number = [i for i in range (2, number) if lst[i]]
        kol = len(prime_number)
print(prime_number)
