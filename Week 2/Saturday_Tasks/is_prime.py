import math

n = int(input("Enter n: "))

prime = True
start = 2

while start <= math.sqrt(n):
    if n % start == 0:
        prime = False
        break
    start +=1

if prime:
    print("The number is prime!")
else:
    print("The number is not prime!")      
