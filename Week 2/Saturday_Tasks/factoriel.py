n = int(input("Enter n: "))
total = 1
start = 1

while start <= n:
    total *= start
    start+=1

if n == 0:
    print("1")
else:
    print(total)
