n = input("Enter n: ")
n = int(n)

divisors = []
start = 1

while start < n:
    if n % start == 0:
        divisors += [start]
    start+=1

print("Divisors are: ")
for divisor in divisors:
    print(divisor)
