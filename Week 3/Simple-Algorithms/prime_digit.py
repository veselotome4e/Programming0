import math

n = input("Enter n: ")
n = int(n)

digits = []
while n >  0:
    digit = n % 10
    digits += [digit]
    n = n // 10

for each in digits:
    
    start = 2
    is_prime = True
    
    if each == 1:
        is_prime = False

    while start < each:
        if each % start == 0:
            is_prime = False
            break
        start = start +1

    if is_prime:
        each = True

if True in digits:
    print("At least one exist")
    
