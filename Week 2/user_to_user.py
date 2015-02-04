a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a < b:
    while a <= b:
        print(a)
        a = a + 1
else:
    while a >= b:
        print(b)
        b+=1
