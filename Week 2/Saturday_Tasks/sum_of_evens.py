number = int(input("Enter number: "))
start = 1
total = 0

while start <= number:
    if start % 2 == 0:
        total += start
    start+=1

print(str(total))
