n = int(input("Enter n: "))
m = int(input("Enter m: "))

while n <= m:
    number = n
    total = 0
    while number >  0:
        digit = int(number % 10)
        total += digit
        number = int(number / 10)
    print("Sum of digits of %d = % d"%(n,total))
    n+=1
    

 
